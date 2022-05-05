

.PHONY : env
env : 
	bash -i envsetup.sh

raw_%_data : 
	cd data/pums/raw; wget https://www2.census.gov/programs-surveys/acs/data/pums/$*/1-Year/csv_pus.zip -O $*_census.zip
	cd data/pums/raw; unzip -o $*_census.zip


# load all raw data, relabel 2018 csv files to be consistent 
.PHONY : raw_pums_data
raw_pums_data :  raw_2010_data raw_2012_data raw_2014_data raw_2016_data raw_2018_data
	cd data/pums/raw; mv psam_pusa.csv ss18pusa.csv
	cd data/pums/raw; mv psam_pusb.csv ss18pusb.csv

.PHONY : extract_grad_data
all_grad_data : compile_raw_pums_data.py raw_pums_data
	conda activate hw7env
	python code/compile_raw_pums_data.py


.PHONY : compute_major_stats
major_stats : genearte_majors_stats.py all_grad_data
	conda activate hw7env
	python code/genearte_majors_stats.py