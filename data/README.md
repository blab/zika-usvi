# Data

## Protocols and pipelines

[All experimental protocols and bioinformatic pipelines are fully specified in the `zika-seq` repository](https://github.com/blab/zika-seq/).

## Samples from the USVI

Sample metadata is specified in `zika_usvi_samples.tsv`.

## Consensus genomes for USVI samples

Genomes are collected into FASTAS with "good" coverage (>80%) in `zika_usvi_good.fasta` and with "partial" coverage (50%-80%) in `zika_usvi_partial.fasta`. Genomes that have less than 50% coverage are in `zika_usvi_poor.fasta`, however they are not used in any analyses. FASTA headers are in the following format:

strain      | sample_id | collection_date | country | division    | location  | seq_platform |
----------- | --------- | --------------- | ------- | ----------- | --------- | ------------ |
USVI/1/2016 | VI1       | 2016-09-28      | usvi    | saint_croix | saint_croix | minion |

## Data sync to access and align all publicly available Zika genomes

1) Download all publicly available Zika genomes from `nextstrain/fauna`.

    * `cd` into nextstrain-fauna repo
    * set `$RETHINK_HOST` with `source environment_rethink.sh`
    * download zika sequences with `python vdb/zika_download.py -db vdb -v zika --fstem zika`
    fasta file will write to `data/zika.fasta`

    ** (AB - last download 08/15/2017)

2) Run sequences through `nextstrain/augur` to filter out problematic genomes, and align and strip to WHO Zika reference genome.

    * `cd` into nextstrain-augur repo, then into `zika` directory.
    * Prepare for augur processing by running `python zika.prepare.py -v 0`. Default subsampling is turned off with `-v 0`.
    * Process with augur by running `python zika.process.py --clean`. Allow augur to run fully to completion, which allows filtering of outlier clades, genomes with too much terminal branch length, or genomes that demonstrate large deviations from the molecular clock. This filtering of the alignment will occur after the alignment has been written to disk, hence why augur should be run to completion.
    * Alignment is written to `processed/zika_aligned_stripped.mfa`.
    * As a QC step, you can visualize the augur-built trees via [auspice](https://github.com/nextstrain/auspice). Make sure the tree and the tmrca look appropriate. To visualize your augur build locally via auspice move JSONs from `augur/zika/auspice/` to `auspice/data/`, then do:

      `npm install`

      `npm run start:local` and visualize on local-host 4000.
