import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from code.rate_plot import combine2table, employment_rate_table, plotting_trend, filter_major_category
import os

table1 = pd.read_csv("data/pums/processed/10_edu_wage_data.csv")
table2 = pd.read_csv("data/fivethiryeight/majors-list.csv")
table2 = table2[table2["FOD1P"] != "bbbb "]
table2["FOD1P"] = pd.to_numeric(table2["FOD1P"])
combined_table = combine2table(table1, table2)

def test_combine2table():
	assert all(combined_table["SEX"].isin(["Male", "Female"])) == True


def test_employment_rate_table():
	employment_df = employment_rate_table(combined_table, 2010)
	assert all(employment_df["employment_rate2010"] <= 100) == True


def test_plotting_trend():
	employment_df = employment_rate_table(combined_table, 2010)
	filetype = ".png"
	plotting_trend(employment_df, "Employment Rate By Major Category In 2010",\
				   "Year", "Employment Rate (%)", ["2010"], "temp_employment_rate", filetype)
	filepath = "figures/temp_employment_rate.png"
	assert os.path.exists(filepath)
	os.remove(filepath)


def test_filter_major_category():
	employment_df = employment_rate_table(combined_table, 2010)
	salary_df = filter_major_category(combined_table, 2010, employment_df)
	assert all(salary_df["$/hr2010"] >= 0) == True
