import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from collegetools import gender_tool as gt

def test_plot_gender_income_diff():
	sorted_recent_grads_2010 = gt.plot_gender_income_diff(2010, recent_grads)
	sorted_recent_grads_2012 = gt.plot_gender_income_diff(2012, recent_grads)
	sorted_recent_grads_2014 = gt.plot_gender_income_diff(2014, recent_grads)

	assert sorted_recent_grads_2010['Major'][0] == 'FOOD SCIENCE'
	assert sorted_recent_grads_2012['Major'][1] == 'PETROLEUM ENGINEERING'
	assert sorted_recent_grads_2012['Major'][2] == 'GEOLOGICAL or GEOPHYSICAL ENGINEERING'
	

def test_plot_income_diff_category():
	assert plot_income_diff_category(recent_grads) is not None
	
def test_womenratio_median_scatter_plot():
	assert womenratio_median_scatter_plot(df, year) != 0
	