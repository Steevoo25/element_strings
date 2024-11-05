# This script runs the breaking bad algorithm on a csv containing words, and performs some analysis on the results

from breaking_bad_algorithm import create_string_from_element_symbols
from matplotlib import pyplot as plt
import pandas as pd

import csv

# -- STRUCTURE--

path : str = './Dictionaries/English/OPTED-Dictionary.csv'

with open(path, 'r', newline='') as csv_file:
    csv_data = csv.reader(csv_file, delimiter=',')
    for row in csv_data:
        print(row)
#data cleaning
#1 remvoe duplicates
#2 remove spaces
#3 remove special characters "-, ', "

# import csv into df
# df structure:
# word | languague | length | BrBa Result

# run words through BrBa and save results into df

# plot results
