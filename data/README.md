# Data

## Protocols and pipelines

[All experimental protocols and bioinformatic pipelines are fully specified in the `zika-seq` repository](https://github.com/blab/zika-seq/).

## Samples

Sample metadata is specified in `zika_usvi_samples.tsv`.

## Consensus genomes

Genomes are collected into FASTAS with "good" coverage (>80%) in `zika_usvi_consensus_good.fasta` and with "partial" coverage (50%-80%) in `zika_usvi_consensus_partial.fasta`. FASTA headers are in the following format:

strain      | sample_id | collection_date | country | division    | location
----------- | --------- | --------------- | ------- | ----------- | --------
USVI/1/2016 | VI1       | 2016-09-28      | usvi    | saint_croix | saint_croix
