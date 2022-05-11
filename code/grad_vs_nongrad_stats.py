import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def worst_premiums(df, n):
    
    """
	Given a dataframe of entries for graduate and nongrad degree data, rank them
	
	Input:
    
    # df is a dataframe of grad vs undergrad student data
    # n is a ranking boundary, ie) worst n majors
    
    Output:
    
    A pandas dataframe of the n worst graduate degree majors in terms of its median salary           premium in comparison to its undergrad median salary
    """
    
    
    result = df.sort_values(by = ['Grad_premium'])[['Major', 'Grad_premium']].iloc[0:n,:]
    
    return result

def best_premiums(df, n):
    
    """
	Given a dataframe of entries for graduate and nongrad degree data, rank them
	
	Input:
    
    # df is a dataframe of grad vs undergrad student data
    # n is a ranking boundary, ie) best n majors
    
    Output:
    
    A pandas dataframe of the n best graduate degree majors in terms of its median salary           premium in comparison to its undergrad median salary
    """
    
    
    result = df.sort_values(by = ['Grad_premium'], ascending = False)[['Major','Grad_premium']].iloc[0:n,:]
    
    return result

def bar_plot_premium_rankings(df, worst = True):
    
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
    plt.ylabel("Grad Salary Premium");
    plt.xticks(rotation = 90);
    if worst:
        plt.title("Worst Graduate Degrees by their Salary Premium to Nongrad Degree");
    else:
        plt.title("Best Graduate Degrees by their Salary Premium to Nongrad Degree");
    
if __name__ == "__main__":
	grad_vs_nongrad_stats()