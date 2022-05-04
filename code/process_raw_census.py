import pandas as pd
import numpy as np 
from tqdm import tqdm

cols = ['ADJINC','AGEP','CIT','COW','ENG','SCHL','SEX','WAGP','WKHP','WKW','FOD1P','FOD2P', 'PERNP']

def get_college_plus_grads_from_raw():
	years = [10,12,14,16,18]
	for year in tqdm(years):
		file_names = ["data/census/raw/ss"+str(year)+"pus"+X+".csv" for X in ['a','b']]
		data_a = pd.read_csv(file_names[0], usecols=cols)
		data_b = pd.read_csv(file_names[1], usecols=cols)
		year_data = pd.concat([data_a,data_b])
		year_data = year_data.query("SCHL >= 21")
		year_data.to_csv("data/census/processed/"+str(year)+"_edu_wage_data.csv",index=False)


if __name__ == "__main__":
    get_college_plus_grads_from_raw()