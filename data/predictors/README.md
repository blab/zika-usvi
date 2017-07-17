# Predictor data for phylogeographic GLM.

### Currently planned predictors

* **Great circle distances between population-weighted country centroids.** Generating code in [Mathematica notebook](https://github.com/blab/zika-usvi/blob/master/scripts/weighted-centroids.nb) and file [here](https://github.com/blab/zika-usvi/blob/master/data/predictors/pop-weighted-centroids.tsv).
* **Origin country population size.** Source: [CIA World Factbook](https://www.cia.gov/library/publications/the-world-factbook/rankorder/2119rank.html) and [UNdata](http://data.un.org/). Reformatted World Factbook data [available in this file](https://github.com/blab/zika-usvi/blob/master/data/predictors/cia-world-fact-book-popsizes.txt)
* **Destination country population size.** Source: CIA World Factbook and UNdata, same as above.
* **Degree of air traffic between countries.** Source: Bluedot.
* **Vector abundance of country.** Source: Kraemer eLife paper?
* **Northward direction of ZIKV migration.**
* **Southward direction of ZIKV migration.**

### Possible other predictors
* Country population size that is native-born or foreign-born (available from UNdata) as a possible measure of population-level migrancy?
