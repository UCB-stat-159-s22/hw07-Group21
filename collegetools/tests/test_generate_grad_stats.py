import pandas as pd
import numpy as np

from collegetools.generate_grad_stats import weighted_median

def test_empty_median():
	empty_df = pd.DataFrame(columns=['val','wt'])
	assert weighted_median(empty_df,'val','wt') == -1 


def test_unweighted_median():
	sample_df = pd.DataFrame(data=[[1,1],[2,1],[3,1]],columns=['val','wt'])
	assert weighted_median(sample_df,'val','wt') == 2

def test_weighted_median():
	sample_df = pd.DataFrame(data=[[1,5],[2,2],[3,1]],columns=['val','wt'])
	assert weighted_median(sample_df,'val','wt') == 1
