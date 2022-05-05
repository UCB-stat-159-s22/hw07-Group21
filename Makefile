census_data_20 : 
	cd data/census; wget https://www2.census.gov/programs-surveys/acs/experimental/2020/data/pums/1-Year/csv_pus.zip -O 2020_census.zip
	cd data/census; unzip -o 2020_census.zip

census_data_10 : 
	cd data/census; wget https://www2.census.gov/programs-surveys/acs/data/pums/2010/1-Year/csv_pus.zip -O 2010_census.zip
	cd data/census; unzip -o 2010_census.zip