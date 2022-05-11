import pandas as pd
import numpy as np

from collegetools.grad_vs_nongrad import worst_premiums, best_premiums, groupby_major_category, best_programs

def test_worst_premiums_sort():
    d = {"Major": ['A', 'B', 'C'], "Grad_premium": [1.3, 1.5, 1.0]}
    sample_df = pd.DataFrame(data = d)
    sort_df = worst_premiums(sample_df, 2)
    assert list(sort_df['Grad_premium']) == [1.0,1.3]

def test_best_premiums_sort():
    d = {"Major": ['A', 'B', 'C'], "Grad_premium": [1.3, 1.5, 1.0]}
    sample_df = pd.DataFrame(data = d)
    sort_df = best_premiums(sample_df, 2)
    assert list(sort_df['Grad_premium']) == [1.5,1.3]

def test_groupby():
    d = {"Major_category": ['A', 'A', 'C'], "Major": ['a', 'b', 'c' ], "Grad_premium": [1.3, 1.5, 5.0]}
    sample_df = pd.DataFrame(data = d)
    assert groupby_major_category(sample_df).iloc[0][0] == 1.4
def test_major_category_ranks():
    d = {"Major_category": ['A', 'A', 'C'], "Major": ['a', 'b', 'c' ], "Grad_premium": [1.3, 1.5, 5.0]}
    sample_df = pd.DataFrame(data = d)
    x = groupby_major_category(sample_df)
    best_programs(x).iloc[0][1] == 5.0