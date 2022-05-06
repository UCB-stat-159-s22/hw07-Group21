import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Plot a horizonal bar plot to see the differences in 2010.
def plot_gender_income_diff(year, recent_grads):
    
    index = int((year - 2010) / 2)
    # Sort majors by median income differences
    sorted_grads_diff = [df.sort_values("median income diff (men - women)") for df in recent_grads]
    
    major = sorted_grads_diff[index]['Major']
    income_diff = sorted_grads_diff[index]['median income diff (men - women)']
    
    plt.figure(figsize=(5,40))
    plt.barh(major, income_diff)
    plt.title("Median Income Differences between Men and Women (Men - Women) in All Majors")
    return sorted_grads_diff