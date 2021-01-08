# Genetic characterization of the Zika virus epidemic in the US Virgin Islands

#### Allison Black<sup>1,2</sup>, Barney Potter<sup>1</sup>, Leora Feldstein<sup>1</sup>, M. Elizabeth Halloran<sup>1</sup>, Jorge L. Munoz-Jordan, Gilberto A. Santiago, Nathan D. Grubaugh<sup>4</sup>, Kristian G. Andersen<sup>4</sup>, Brett R. Ellis<sup>5</sup>, Esther M. Ellis<sup>5</sup>, Trevor Bedford<sup>1</sup>

<sup>1</sup>Vaccine and Infectious Disease Division, Fred Hutchinson Cancer Research Center, Seattle, WA, USA.

<sup>2</sup>Department of Epidemiology, University of Washington, Seattle, WA, USA.

<sup>3</sup>Centers for Disease Control and Prevention, Dengue Branch, San Juan, Puerto Rico.

<sup>4</sup>Department of Immunology and Microbial Science, The Scripps Research Institute, La Jolla, CA, USA,

<sup>5</sup>United States Virgin Islands Department of Health, Christiansted, USVI.

## Abstract

## Using this repo to reproduce analyses in the paper.

First things first you can clone this repo by running the following command in your terminal.

`git clone https://github.com/blab/zika-usvi.git`

The analyses and scripts available in this repo require `conda environments` as well as `nextstrain`. Instructions for how to install conda and nextstrain components can be found [here](https://docs.nextstrain.org/en/latest/guides/install/local-installation.html).

If you follow the above install instructions you will have made a nextstrain conda environment. To run the scripts I wrote for this project you'll need to make another conda environment: the `zika-usvi-env` environment in the [`envs` directory linked here](./envs). If you are in this top level directory then you can make this environment by running the following command in your terminal:

`conda env create -f envs/zika-usvi-env.yaml`

Then, whenever you want to do something you'll need to activate the environment. To do so, run the following command in your terminal:

`conda activate zika-usvi-env`

You can find a ton of information about the data we generated, and the process of collating the contextual sequence data, in [the data directory README](data/README.md).

While the paper's analyses are done in BEAST, there is also a Nextstrain build for this dataset as well. If you want to explore that build it's available at [`nextstrain.org/community/blab/zika-usvi`](https://nextstrain.org/community/blab/zika-usvi).

Alternatively, you could also run the build locally. The pipeline is fully specified in the `Snakefile`, however please note that you'll need to have the nextstrain tools installed for the build to work.   
