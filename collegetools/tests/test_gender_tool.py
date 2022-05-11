import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from collegetools import gender_tool as gt

# Read data
recent_grads_10 = pd.read_csv("data/pums/processed/2010_recent_grad_stats_by_major.csv")
recent_grads_12 = pd.read_csv("data/pums/processed/2012_recent_grad_stats_by_major.csv")
recent_grads_14 = pd.read_csv("data/pums/processed/2014_recent_grad_stats_by_major.csv")
recent_grads_16 = pd.read_csv("data/pums/processed/2016_recent_grad_stats_by_major.csv")
recent_grads_18 = pd.read_csv("data/pums/processed/2018_recent_grad_stats_by_major.csv")

# Make a list of dataframs
recent_grads = [recent_grads_10, recent_grads_12, recent_grads_14, recent_grads_16, recent_grads_18]

# Loop over the list and a column to each of the datafram
for df in recent_grads:
    df['median income diff (men - women)'] = df['men median'] - df['women median']

# Test the plot_gender_income_diff function
def test_plot_gender_income_diff():
	result_2010 = gt.plot_gender_income_diff(2010, recent_grads)
	result_2012 = gt.plot_gender_income_diff(2012, recent_grads)

	assert result_2010 is not None
	assert result_2012 is not None


# Test the plot_income_diff_category function
def test_plot_income_diff_category():
	result = gt.plot_income_diff_category(recent_grads)
	assert result is not None


# Test the womenratio_median_scatter_plot function
def test_womenratio_median_scatter_plot():
	women = recent_grads_10['women'] 
	all_gender = recent_grads_10['men'] + recent_grads_10['women']
	recent_grads_10['women_ratio'] = women / all_gender
							
	corr = gt.womenratio_median_scatter_plot(recent_grads_10, 2010)
	assert corr != 0
