

.PHONY : env
env : 
	bash -i envsetup.sh


%_census.zip : 
	cd data/pums/raw; wget https://www2.census.gov/programs-surveys/acs/data/pums/$*/1-Year/csv_pus.zip -O $*_census.zip
	cd data/pums/raw; unzip -o $*_census.zip


# load all raw data, relabel 2018 csv files to be consistent 
.PHONY : raw_pums_data
raw_pums_data :  2010_census.zip 2012_census.zip 2014_census.zip 2014_census.zip 2016_census.zip 2018_census.zip
	cd data/pums/raw; mv psam_pusa.csv ss18pusa.csv
	cd data/pums/raw; mv psam_pusb.csv ss18pusb.csv

.PHONY : all_grad_data
all_grad_data : collegetools/compile_raw_pums_data.py 
	python collegetools/compile_raw_pums_data.py


.PHONY : major_stats
major_stats : collegetools/generate_major_stats.py 
	python collegetools/generate_major_stats.py


.PHONY : grad_stats
grad_stats : collegetools/generate_grad_stats.py 
	python collegetools/generate_grad_stats.py

