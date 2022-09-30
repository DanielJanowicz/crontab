## Importing packages
import pandas as pd
import airflow
import crontab 
import os
import sys
import time

## Pulling data from API
df = pd.read_json('https://pomber.github.io/covid19/timeseries.json')
df

## Getting the time on the system
currentTime = time.time()
listTime = time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime(currentTime))
print('The current time is: ', listTime)

## Getting the current working directory
cwd = os.getcwd()
print(cwd)

## Creating a ile in the current working directory
with open(cwd + '/updateFile_' + listTime + '.txt', 'w') as f:
    f.write(str(df))