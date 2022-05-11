import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def groupby_major_category(df):
    """
	Given a dataframe of entries for graduate and nongrad degree data, group them by major           category
	
	Input:
    
    # df is a dataframe of grad vs undergrad student data
    
    Output:
    
    A pandas dataframe grouped by major category
    """
    return df.groupby(by = ['Major_category']).median()

def best_programs(df):
    """
	Given a dataframe of entries that are grouped by their major category, return the best           category with respect to grad premiums
	
	Input:
    
    # df is a dataframe of major categories
    
    
    Output:
    
    A pandas dataframe of the best major categories with respect to their grad premium
    """
    
    
    result =  df.sort_values(by = ['Grad_premium'], ascending = False)['Grad_premium']
    
    return result.reset_index()
    
    
def worst_premiums(df, n = 10):
    
    """
	Given a dataframe of entries for graduate and nongrad degree data, rank them
	
	Input:
    
    # df is a dataframe of grad vs undergrad student data
    # n is a ranking boundary, ie) worst n majors
    
    Output:
    
    A pandas dataframe of the n worst graduate degree majors in terms of its median salary           premium in comparison to its undergrad median salary
    """
    
    if n <= 0:
        return "Invalid n, choose a positive value for n"
    result = df.sort_values(by = ['Grad_premium'])[['Major', 'Grad_premium']].iloc[0:n,:]
    
    return result

def best_premiums(df, n = 10):
    
    """
	Given a dataframe of entries for graduate and nongrad degree data, rank them
	
	Input:
    
    # df is a dataframe of grad vs undergrad student data
    # n is a ranking boundary, ie) best n majors
    
    Output:
    
    A pandas dataframe of the n best graduate degree majors in terms of its median salary           premium in comparison to its undergrad median salary
    """
    
    if n <= 0:
        return "Invalid n, choose a positive value for n"
    result = df.sort_values(by = ['Grad_premium'], ascending = False)[['Major','Grad_premium']].iloc[0:n,:]
    
    return result

def plot_programs(df):
    
    """
    Given a dataframe of Major Category Programs, plot their grad premiums
    
    Input:
    
    # df is a dataframe of major category programs and their grad premiums
    
    Output:
    
    A bar plot of grad premium for each major category
    
    """
    
    plt.bar(df['Major_category'], df['Grad_premium']);
    plt.xlabel("Major Category");
    plt.ylabel("Grad Salary Premium %");
    plt.xticks(rotation = 90);
    plt.title("Ranking of Major Degree Categories by their Graduate Degree Salary Premiums");
    

def plot_rankings(df, worst = True):
    
    """
    Given a dataframe of best/worst grad degree premiums, plot their rankings
    
    Input:
    
    # df is a dataframe of the grad degree premiums ranked
    # worst: assumes its the worst rankings, set worst to False and it will plot best rankings. 	This is for stylistic purposes in the bar graph
    
    Output:
    
    A bar plot of grad premium rankings
    
    """
    
    plt.bar(df['Major'], df['Grad_premium']);
    plt.xlabel("Degree");
    plt.ylabel("Grad Salary Premium %");
    plt.xticks(rotation = 90);
    if worst:
        plt.title("Worst Graduate Degrees by their Salary Premium to Nongrad Degree");
    else:
        plt.title("Best Graduate Degrees by their Salary Premium to Nongrad Degree");
    
    
if __name__ == "__main__":
	grad_vs_nongrad()