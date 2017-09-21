## Alignment QC:

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
