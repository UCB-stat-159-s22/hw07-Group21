census_data_10 : 
	cd data/census; wget https://www2.census.gov/programs-surveys/acs/data/pums/2010/1-Year/csv_pus.zip -O 2010_census.zip
	cd data/census; unzip -o 2010_census.zip

census_data_11 : 
	cd data/census; wget https://www2.census.gov/programs-surveys/acs/data/pums/2011/1-Year/csv_pus.zip -O 2011_census.zip
	cd data/census; unzip -o 2011_census.zip


census_data_12 : 
	cd data/census; wget https://www2.census.gov/programs-surveys/acs/data/pums/2012/1-Year/csv_pus.zip -O 2012_census.zip
	cd data/census; unzip -o 2012_census.zip
