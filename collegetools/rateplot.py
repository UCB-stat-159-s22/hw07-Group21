import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def combine2table(table1, table2):
    """
    Input: 
        - table1: first table with integer as values
        - table2: second table with string as values
    Combine two datasets, define the integer values to string value, and some data cleaning.
    Return a combined dataframe
    """
	
    table1 = table1.dropna(axis = 0)
    # convert employment structure
    result = table1.set_index('FOD1P').join(table2.set_index('FOD1P')).reset_index()
    # self-employed is not counted as employed
    result["COW"] = np.where((result["COW"] == 9) | (result["COW"] == 8) | \
                             (result["COW"] == 7) | (result["COW"] == 6), "Unemployed", "Employed")
    # Rename the major to first degree
    result = result.rename(columns = {"Major": "First_degree"})
    # Give name to variable SEX
    result["SEX"] = np.where(result["SEX"] == 1, "Male", "Female")
    return result


def employment_rate_table(table1, year):
    """
    Input: 
        - table1: table that needs to add a new variable
        - year: the year of that table
    Calculate the employment rate for each major category based on the combined dataframe
    Return clean dataframe with employment rate variable
    """
    table_copy = table1.copy()
    
    # selected the variables we need
    employment_df = table_copy[["Major_Category", "COW"]]
    # create an index column
    employment_df["index"] = table_copy.index
    # count the number of males and females in different category
    employment_df = employment_df.groupby(["Major_Category", "COW"]).count().reset_index()
    # count the total number of people in that major category
    total_num_mtx = table_copy[["Major_Category", "COW"]].groupby("Major_Category").count().reset_index()
    total_num_mtx = total_num_mtx.rename(columns = {"COW": "total"})
    final_df = employment_df.merge(total_num_mtx, on = "Major_Category", how = "left")
    # drop the major that had less than 50 people
    final_df = final_df[final_df["total"] >= 50]
    # # calculate the rate
    final_df["employment_rate"+str(year)] = final_df["index"] / final_df["total"] * 100
    final_df = final_df[final_df["COW"] == "Employed"]
    final_df = final_df.drop(["COW", "index", "total"], axis = 1)
    return final_df


def plotting_trend(table, plot_title, plot_xlabel, plot_ylabel, year_lst, filename, filetype):
    """
    Input:
        - table: the dataframe with the rate of each major category
        - plot_title: the title of the plot
        - plot_xlabel: label for the x-axis
        - plot_ylabel:label for the y-axis
        - year_lst: year list for the xtick
        - filename: file name for the plot
        - filetype: type of the file that is saving
    Plot the trend of the rate.
    """
    table.plot(figsize = (10, 5), 
               title = plot_title, 
               xlabel = plot_xlabel, 
               ylabel = plot_ylabel)
    plt.legend(bbox_to_anchor = (1, 0.5, 1, 0.4), loc = 'upper left')
    plt.xticks(np.arange(0, len(year_lst), 1), year_lst)
    plt.grid()
    plt.savefig('figures/' + filename + filetype, bbox_inches = "tight")


# function to calculate wage rate in each major category
def filter_major_category(table, year, employment_df):
    """
    Input: 
        - table: table that needs to add a new variable
        - year: the year of that table
    Adjusting the total hours, then calculate the wage rate for each major category.
    Return dataframe with a new wage rate column
    """
    temp_table = table.copy()
    # we only want to include the employed people
    temp_table = temp_table[temp_table["COW"] == "Employed"]
    # only include the major categories with growth
    temp_table = temp_table[temp_table["Major_Category"].isin(employment_df.columns)]
    # adjusting the WAGP based on the ADJING, assuming works 4 weeks each months
    total_hours = temp_table["WKHP"].astype(int) * 4 * 12
    temp_table["$/hr" + str(year)] = temp_table["ADJINC"] * 1e-6 * temp_table["WAGP"] / total_hours
    # keep columns that are meaningful
    temp_table = temp_table[["$/hr" + str(year), "Major_Category"]]
    # group by each major category, calculate the average wage per hour in the whole table
    temp_table = temp_table.groupby("Major_Category").mean().reset_index()
    return temp_table
