import pandas as pd
import numpy as np 
import pytest

def has_majors(df):
	return df['FOD1P'].isna().sum() == 0

def genders_add(df):
	return (df['men'] + df['women'] != df['total']).sum() == 0

testyears = [2010,2012,2014,2016,2018]

@pytest.mark.parametrize("year", testyears)
def test_year_has_majors(year):
	year_df = pd.read_csv("data/pums/processed/"+str(year)+"_recent_grad_stats_by_major.csv")
	assert has_majors(year_df)

@pytest.mark.parametrize("year", testyears)
def test_year_gender_split(year):
	year_df = pd.read_csv("data/pums/processed/"+str(year)+"_recent_grad_stats_by_major.csv")
	assert genders_add(year_df)
