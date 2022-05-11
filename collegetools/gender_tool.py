import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Plot a horizonal bar plot of each major's median income differences 
# between men and women (men - women) recent college graduates in the given year
def plot_gender_income_diff(year, recent_grads):
	
	'''
	year: an integer selected from 2010, 2012, 2014, 2016 or 2018

	recent_grads: a list of processed dataframes from 2010 to 2018
				with N/A dropped and income differences calculated
				as median income of men - median income of women

	return: a list of dataframes from 2010 to 2018, sorted by differences
			of income.
	'''

	# Get the index of the dataframe of that year
	index = int((year - 2010) / 2)
	# Sort majors by median income differences
	sorted_grads_diff = [df.sort_values("median income diff (men - women)") for df in recent_grads]

	# Get major as y axis and income_diff as x axis
	major = sorted_grads_diff[index]['Major']
	income_diff = sorted_grads_diff[index]['median income diff (men - women)']

	# Plot the horizontal bar plot
	plt.figure(figsize=(5,40))
	plt.barh(major, income_diff)
	plt.title("Median Income Differences between Men and Women (Men - Women) in All Majors")

	return sorted_grads_diff


# Creat line plots to show how gender gap in income changed for each major category over time
def plot_income_diff_category(recent_grads):
    
	'''
	recent_grads: a list of processed dataframes from 2010 to 2018
				with N/A dropped and income differences calculated
				as median income of men - median income of women
	return: the datafram tracking gender differences in income
				for each major category over years
	'''
	# Group median income by major category.
	recent_grads_category = [df.groupby(['Major_Category']).mean()
							 for df in recent_grads]

	# Create a list of gender income gap for each major category in each year
	income_diff_category = []
	for df in recent_grads_category:
		income_diff_category.append(df['median income diff (men - women)'])

	# Creat a dataframe out of income_diff_category
	income_diff_category_time = pd.DataFrame(income_diff_category)


	# Since the number of categories exceed the readbility capacity of line plot,
	# divide them into three sets
	categories_1 = income_diff_category_time[income_diff_category_time.columns[0:5]]
	categories_2 = income_diff_category_time[income_diff_category_time.columns[6:11]]
	categories_3 = income_diff_category_time[income_diff_category_time.columns[12:]]
	
	# Make a list of years
	year = [2010, 2012, 2014, 2016, 2018]

	# Plot each set of categories in a line plot
	plt.plot(year, categories_1)
	plt.legend(income_diff_category_time.columns[0:5], loc = 4)
	plt.show()
	plt.plot(year, categories_2)
	plt.legend(income_diff_category_time.columns[6:11], loc = 4)
	plt.show()
	plt.plot(year, categories_3)
	plt.legend(income_diff_category_time.columns[12:], loc = 1)
	plt.show()

	return income_diff_category_time


# Draw a scatter plot of women ratio vs. total median earning to see the correlation
def womenratio_median_scatter_plot(df, year):
	'''
	df: a datafram containing data of recent college graduates
	year: an integer selected from 2010, 2012, 2014, 2016 or 2018
	return: correlation coefficient between 
			women ratio and total median earning in that year
	'''

	# Make a scatter plot
	plt.scatter(df['women_ratio'], df['total median'])
	plt.legend()
	# Build a linear regression model
	sns.regplot('women_ratio', 'total median', data=df)
	# Title the plot
	plt.title("women ratio vs total median")
	# Calculate correlation coef
	corr = df['women_ratio'].corr(df['total median'])
	# Print the corr coref in a readable line
	print("correlation coefficient between women ratio and median earning in", year, "equals to:", corr)
	return corr