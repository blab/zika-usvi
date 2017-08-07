# Predictor data for phylogeographic GLM.

### Currently planned predictors

* **Great circle distances between population-weighted country centroids.** Generating code in [Mathematica notebook](https://github.com/blab/zika-usvi/blob/master/scripts/weighted-centroids.nb) and file [here](https://github.com/blab/zika-usvi/blob/master/data/predictors/pop-weighted-centroids.tsv).

* **Origin country population size.** Source: [CIA World Factbook](https://www.cia.gov/library/publications/the-world-factbook/rankorder/2119rank.html) and [UNdata](http://data.un.org/). Reformatted World Factbook data [available in this file](https://github.com/blab/zika-usvi/blob/master/data/predictors/cia-world-fact-book-popsizes.txt)

* **Fraction of population living in an urban center**: Source: Data downloaded as CSV from [The World Bank | Data.](http://data.worldbank.org/indicator/SP.URB.TOTL.IN.ZS)

* **Destination country population size.** Source: CIA World Factbook and UNdata, same as above.

* **Degree of air traffic between countries.** Source: Bluedot. _Please note that due to licensing agreements with IATA, this predictor cannot be made publicly available on Github._

* **Vector abundance of country.** Possible source: Messina et al paper.

* **Latitudinal direction of ZIKV migration.** This pairwise predictor has a `1` value for the cell if the origin's population-weighted centroid is north of the destination's, and a `-1` if origin is south of the destination.


### Possible other predictors
* Country population size that is native-born or foreign-born (available from UNdata) as a possible measure of population-level migrancy?

### Workflow for data standardization and making predictor matrices in BEAST format.

1) Standardize country names. See [`indexed-countries-50.tsv`](https://github.com/blab/zika-usvi/blob/master/data/phylo-glm/indexed-countries-50.tsv) for canonical project names. Cleaned up data are written to `tsv`.

> Importantly, at this point there are two types of `tsv` files, those that contain data that is not pairwise (e.g. country population size) or data that is inherently pairwise (e.g. amount of air traffic passengers flowing between countries). Pairwise predictor `tsv` files are written to the following format:

>`origin \t destination \t predictor_value`

> Non-pairwise `tsv` files are written as:

> `country \t value`

2) All `tsv` files that are not pairwise, are collated within a single dataframe by left-joining on `indexed-countries-45.tsv`. This allows filtering out of countries that are not included in the analysis.

3) Make pairwise-format `tsv` files from the non-pairwise data by assigning either the origin value to the destination value to all origin-destination pairs.

4) Import all origin-destination pair data from each of the `tsv` files, then make flattened matrices. _Note that matrix indexing for GLM predictor matrices is unique. We've accounted for this in our code_.

5) Take natural log of all values in the matrix, then standardize the log transformed values by doing the following for each value in the matrix.

>(value - mean)/(standard deviation)

6) Export log-transformed and standardized flattened matrices to `tsv`.
