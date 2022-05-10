import pandas as pd
import numpy as np
from tqdm import tqdm
import wquantiles as wq

years = [10,12,14,16,18]


def weighted_median(df, val_name, weight_name):
	if df.size > 0:
		return int(wq.median(df[val_name], df[weight_name]))
	else: 
		return -1

def compute_grad_stats(df):
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
		SCHL  - highest level of school attained 
		
	Output:
	------
	A pandas.Series with counts for per major male/female majors with/out graduate degrees and median income for each 
	of those groups
	"""
	output = {}
    
	# get counts for men, women, and both
	output['total'] = df['PWGTP'].sum()
	output['total_grad'] = df.query('SCHL > 21')['PWGTP'].sum()
	output['total_no_grad'] = df.query('SCHL == 21')['PWGTP'].sum()
	output['total_men'] = df.query("SEX == 1")['PWGTP'].sum()
	output['total_grad_men'] = df.query("SEX == 1 & SCHL > 21")['PWGTP'].sum()
	output['total_no_grad_men'] = df.query("SEX == 1 & SCHL == 21")['PWGTP'].sum()
	output['total_women'] = df.query("SEX == 2")['PWGTP'].sum()
	output['total_grad_women'] = df.query("SEX == 2 & SCHL > 21")['PWGTP'].sum()
	output['total_no_grad_women'] = df.query("SEX == 2 & SCHL == 21")['PWGTP'].sum()
    
    # compute income stats (by gender and not) 
	df = df[df['WKHP']!=' '] # drop any rows with empty wkhp 
	df['WKHP'] = df['WKHP'].astype(float)
	
	full_time = df.query("WKW == 1 & WKHP >= 35")
	full_time_men = full_time.query("SEX == 1")
	full_time_women = full_time.query("SEX == 2")
	full_time_grad = full_time.query('SCHL>21')
	full_time_no_grad = full_time.query('SCHL==21')
	# compute median earnings split by men & women, if no data points, return -1 
	output['overall_median']  = int(wq.median(full_time['WAGP'], full_time['PWGTP']))
	output['overall_grad_median']     = int(wq.median(full_time_grad['WAGP'], full_time_grad['PWGTP']))
	output['overall_no_grad_median']     = int(wq.median(full_time_no_grad['WAGP'], full_time_no_grad['PWGTP']))

	output['women_median']          = weighted_median(full_time_women,'WAGP','PWGTP')
	output['women_grad_median']     = weighted_median(full_time_women.query("SCHL > 21"),'WAGP','PWGTP')
	output['women_no_grad_median']  = weighted_median(full_time_women.query("SCHL == 21"),'WAGP','PWGTP')

	output['men_median']            = weighted_median(full_time_men,'WAGP','PWGTP')
	output['men_grad_median']       = weighted_median(full_time_men.query("SCHL > 21"),'WAGP','PWGTP')
	output['men_no_grad_median']    = weighted_median(full_time_men.query("SCHL == 21"),'WAGP','PWGTP')

	return pd.Series(output, dtype=int)

def compute_graduate_stats_by_major(years=years):
	"""
	DOCSTRING
	"""
	major_list = pd.read_csv("data/fivethirtyeight/majors-list.csv")
	major_list = major_list[~major_list['FOD1P'].str.contains('bb')]
	major_list['FOD1P'] = major_list['FOD1P'].astype(int)
	for year in tqdm(years):
		filename = "data/pums/processed/"+str(year)+"_edu_wage_data.csv"
		all_grads = pd.read_csv(filename)
		grad_stats = all_grads.groupby('FOD1P').apply(compute_grad_stats)
		grad_stats = grad_stats.merge(major_list, on="FOD1P")
		grad_stats.to_csv("data/pums/processed/20"+ str(year)+ "_graduate_stats_by_major.csv", index=False)

if __name__ == "__main__":
	compute_graduate_stats_by_major()