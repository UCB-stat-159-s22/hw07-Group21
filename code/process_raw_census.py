import pandas as pd
import numpy as np
from tqdm import tqdm
import wquantiles as wq

cols = ['ADJINC','AGEP','CIT','COW','ENG','SCHL','SEX','WAGP','WKHP','WKW','FOD1P','FOD2P', 'PERNP' ,'ESR', 'PWGTP']
years = [10,12,14,16,18]

def get_college_plus_grads_from_raw(years=years, cols=cols):
	"""
	Loads PUMS data for specified years, selects desired columns, and combines into one file per year
	
	Requires: 
	--------
	Each year's data is expected to be stored in two csv files `ssXXpusa.csv` and `ssXXpusb.csv` where 
	XX is the last two digits of the year.
	"""
	for year in tqdm(years):
		file_names = ["data/census/raw/ss"+str(year)+"pus"+X+".csv" for X in ['a','b']]
		data_a = pd.read_csv(file_names[0], usecols=cols)
		data_b = pd.read_csv(file_names[1], usecols=cols)
		year_data = pd.concat([data_a,data_b])
		year_data = year_data.query("SCHL >= 21")
		year_data.to_csv("data/census/processed/"+str(year)+"_edu_wage_data.csv",index=False)

def compute_major_stats(df):
	"""
	Given a dataframe of entries for a specific major
	
	Input:
	-----
	df  (pandas.DataFrame) : Dataframe with majors data, must all have the same FOD1P code and the following colums
		PWGTP - weight per entry
		SEX   - person's sex 
		WAGP  - income
		WKW   - encoding for weeks worked (1 - 50 to 52 weeks / year)
		WKHP  - typical hours per week (in hours) 
		
	Output:
	------
	A pandas.Series with counts for total majors, male majors, and female majors, as well as median incomes for
	all majors, as well for male and female majors separately. 
	"""
	output = {}
    
	# get counts for men, women, and both
	output['total'] = df['PWGTP'].sum()
	output['men'] = df.query("SEX == 1")['PWGTP'].sum()
	output['women'] = df.query("SEX == 2")['PWGTP'].sum()
    
    # compute income stats (by gender and not) 
	df = df[df['WKHP']!=' '] # drop any rows with empty wkhp 
	df['WKHP'] = df['WKHP'].astype(float)
	
	full_time = df.query("WKW == 1 & WKHP >= 35")
	full_time_men = full_time.query("SEX == 1")
	full_time_women = full_time.query("SEX == 2")
	output['total median']  = int(wq.median(full_time['WAGP'], full_time['PWGTP']))
    
	# compute median earnings split by men & women, if no data points, return -1 
	if full_time_women.size > 0:
		output['women median']  = int(wq.median(full_time_women['WAGP'], full_time_women['PWGTP']))
	else: 
		output['women median']  = -1
	
	if full_time_men.size > 0:
		output['men median']  = int(wq.median(full_time_men['WAGP'], full_time_men['PWGTP']))
	else: 
		output['men median']  = -1
        
	return pd.Series(output, dtype=int)

def compute_recent_grad_stats(years=years):
	"""
	DOCSTRING
	"""
	major_list = pd.read_csv("data/raw/majors-list.csv")
	major_list = major_list[~major_list['FOD1P'].str.contains('bb')]
	major_list['FOD1P'] = major_list['FOD1P'].astype(int)
	for year in tqdm(years):
		filename = "data/census/processed/"+str(year)+"_edu_wage_data.csv"
		data = pd.read_csv(filename)
		if year == 14:
			data = data[data['FOD1P']!= 2415]
		recent_grads = data.query('SCHL >= 21 & AGEP < 28')
		major_stats = recent_grads.groupby('FOD1P').apply(compute_major_stats)
		major_stats = major_stats.merge(major_list, on="FOD1P")
		major_stats.to_csv("data/census/processed/20"+str(year)+"_recent_grad_stats_by_major.csv", index=False)


if __name__ == "__main__":
	get_college_plus_grads_from_raw()
	compute_recent_grad_stats()