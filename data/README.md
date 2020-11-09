# Data

## Protocols and pipelines

[All experimental protocols and bioinformatic pipelines are fully specified in the `zika-seq` repository](https://github.com/blab/zika-seq/).

## Samples from the USVI

Sample metadata is specified in `samples.tsv`.

## Consensus genomes for USVI samples

Genomes are collected into FASTAS with "good" coverage (>80% of sites have non-ambiguous base calls) in `ZIKA_USVI_complete_goodQual.fasta` and with "partial" coverage (50%-80% of sites have non-ambiguous base calls) in `ZIKA_USVI_complete_partialQual.fasta`. Genomes that have less than 50% coverage (over half the sites in the genomes have ambiguous basecalls) are in `ZIKA_USVI_complete_poorQual.fasta`, however they are not used in any analyses.

For some samples there are multiple consensus genomes. This occurred in instances where we sequenced the sample differently, either on MiSeq or MinION, using different MinION sequencing chemistries, or using different multiplexing (either multiplexing 6 samples or 12). This information is contained in the fasta header. So while a single sample might have multiple consensus genomes each fasta header is unique.

While we have shared `ZIKA_USVI_complete_poorQual.fasta` online, we *do not* use these genomes in any of our main analyses. The genomes here have so little unambiguous sequence data that they will not cluster appropriately in a phylogeny. While VI24 has slightly more than 50% unambiguous basecalls, it was sequenced on 2D chemistry after ONT pulled the kit and the bioinformatic pipelines. It is therefore not nanopolished, and we are wary of the demuxing as well as this sample was demuxed by an early version of ONT's built-in demuxer.

## Notes about single clinical isolates that were sequenced multiple times

If you are going through the `ZIKA_USVI_complete_<>Qual.fasta` files you'll notice that some isolates have multiple sequences. We wanted to release _all_ of the data we generated, which is why multiple sequences from a single isolate are available in these files. For the actual analysis however, we only want to use one sequence per clinical isolate. To choose which sequence should be the representative sequence for an isolate we used the following criteria:

1. The selected sequence must have been stringently demuxed.
2. The selected sequence must have been nanopolished.
3. If both of the above criteria were met for multiple sequences, then the sequence with the greatest number of informative base calls was selected to include in the analysis.

The USVI sequences used for downstream analyses (one sequence per isolate) are in `finalized-usvi-seqs-for-use-in-analyses.fasta`.

## The broad process for generating the input data files

Here is the broad strokes process I used to finalize the dataset that I used in the paper (with more details following).

1. From all of of the samples that we sequenced from the USVI, I picked one high quality sequenced to represent each sample (described above).

2. For contextual sequence data from other countries, I downloaded all Zika genomes available from Nextstrain/Fauna.

3. I removed any background contextual sequences that were not published on, or for which I didn't have permission to use in our analysis. I also removed any background sequences that were from geographic areas that I didn't want to include (e.g. Singapore). I did all this within the "make-input-fastas.ipynb" script.

4. Once I had pruned the dataset down to geographic areas of interest, high quality sequences of sufficient length, and published/permitted sequences, I had a dataset of 437 sequences. These are contained within the "usvi-and-high-qual-americas-input-data.fasta" file.

5. The "usvi-and-high-qual-americas-input-data.fasta" is my input file into a Nextstrain build that I ran to do some additional dataset QC, such as looking for excessive terminal branch length, deviation from the molecular clock, etc. Using Nextstrain also allowed me to infer dates for some genomes that lacked full year/month/date information, as well as do some bioinformatics such as making the multiple sequence alignment. You can explore the Nextstrain build at: [nextstrain.org/community/blab/zika-usvi].(https://nextstrain.org/community/blab/zika-usvi@fresh-start)

6. The output file from the Nextstrain build is a JSON file (it lives within the "auspice" directory in the top level of this repo). For my BEAST analyses in the paper I used the final dataset that is specified within the "zika-usvi.json" file. However, so that it could be read in to BEAST, I did have to combine some of the information from the JSON with sequences pulled from the multiple sequence alignment generated within the Nextstrain pipeline. All of the code that I wrote to do that parsing is also in the "make-input-fastas.ipynb" notebook.

7. The final generated dataset that is outputted from the "make-input-fastas.ipynb" notebook is a dataset of 429 aligned genomes, and it is written to "zika-beast-input-2020-02-20.fasta". This is the fasta file that I used to generate my BEAST XML files.    

## More detailed notes about dataset QC:

Here I outline the exclusion criteria for genomes in the analysis. Genomes that should be excluded from the phylogeographic analysis have been hardcoded in to `Nextstrain/augur` in the `dropped_strains` section of the `zika.prepare.py` script.

These QC steps were either carried out in `nextstrain-augur`, or in my [make-input-fastas.ipynb](scripts/make-input-fastas.ipynb) script.

1) The genome has too few informative bases.

The first constraint that I'm imposing on my alignment is that the genome must have a minimum of 5000 informative bases (ie A, C, G, or T) in order to be included in the analysis alignment. `Nextstrain/fauna` grabs all publicly available sequences, so I've looked through these sequences and determined which genomes

2) The genome has excessive terminal branch length.

Excessive terminal branch length accrues when many mutations within a single genome are not shared with any other genomes. This is often and indication that the genome is poor quality or has many sequencing errors, which is why we remove these.

3) The genome may have contamination.

Sequencing Zika from clinical samples is challenging and prone to contamination due to generally low viral titers in PCR positive samples. Since contamination during PCR amplification is a very real risk, we remove genomes if we see possible signatures of contamination in the genome.

4) The genome deviates significantly from the molecular clock.

Pronounced deviation from the molecular clock may be indicative that the stated sampling date of the genome is incorrect, or that there may be errors in the genome. Given that temporal signal is very important to BEAST analyses, these genomes are excluded.

5) The genome is a duplicate.

Some isolates may be sequenced multiple times. We drop strains such that a single isolate is only ever represented by one genome sequence.
