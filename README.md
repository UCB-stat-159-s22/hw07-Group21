Data: [Kaggle College Majors Dataset](https://www.kaggle.com/datasets/tunguz/college-majors)


To download and process origina PUMS data for 2010, 2012, 2014, 2016, and 2018: 
```
make env  # sets up environment
make raw_pums_data
make major_stats # computes wage and gender stats for recent grads by major
make grad_stats # computes wage and gender stats split by graduate degree or not 
```

This process will save a csv per year of the form `20XX_recent_grad_stats_by_major.csv` to `data/pums/processed` with summary statistics for each year grouped by major. 

To access the intermediate raw data for each year (only a subset of features collected) you can load the file `XX_edu_wage_data.csv` from `data/pums/processed` where `XX` corrsponds to the last two digits of the year. 


Troubleshooting for environment setp up and data:

1. If you encounter `ModuleNotFoundError`, try to run `conda activate hw7env`
2. If you encounter `CommandNotFoundError: Your shell has not been properly configured to use 'conda activate'.`, try to run `conda init --all`. Then close your terminal without shutting it down. Reopen it, and run the make command again.  
