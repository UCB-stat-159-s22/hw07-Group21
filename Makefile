raw_%_data : 
	cd data/census/raw; wget https://www2.census.gov/programs-surveys/acs/data/pums/$*/1-Year/csv_pus.zip -O $*_census.zip
	cd data/census/raw; unzip -o $*_census.zip


# load all raw data, relabel 2018 csv files to be consistent 
.PHONY : raw_pums_data
raw_pums_data :  raw_2010_data raw_2012_data raw_2014_data raw_2016_data raw_2018_data
	cd data/census/raw; mv psam_pusa.csv ss18pusa.csv
	cd data/census/raw; mv psam_pusb.csv ss18pusb.csv

.PHONY : get_grad_data
get_grad_data : 