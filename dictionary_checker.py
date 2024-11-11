# This script runs the breaking bad algorithm on a csv containing words, and performs some analysis on the results

from breaking_bad_algorithm import create_string_from_element_symbols
from matplotlib import pyplot as plt
import pandas as pd
import time

import csv

SPECIAL_CHARACTERS = ["'", "-", " "]

def remove_special_chars(word: str, chars: list) -> str:
    for char in chars:
        try:
            word = word.replace(char, "")
        except AttributeError as e:
            print(word, "\n", e)
    return word
            
# -- IMPORT DATA --

# word | length | BrBa Result

path : str = './Dictionaries/English/OPTED-Dictionary.csv'
eng_dict = pd.read_csv(path)

# -- DATA CLEANING --

# remove unneccesary columns
eng_dict = eng_dict.drop(['POS'], axis=1)

# remove empty rows
eng_dict = eng_dict.dropna()

# remove special characters: " ", "'", "-"
start = time.time()
eng_dict['Word'] = eng_dict['Word'].apply(remove_special_chars, chars=SPECIAL_CHARACTERS)
end = time.time()


# remove duplicates
eng_dict = eng_dict.drop_duplicates()

eng_dict['breaking_bad_test'] = eng_dict['Word'].apply(create_string_from_element_symbols)
# run words through BrBa and save results into df



results = eng_dict[eng_dict['breaking_bad_test'].notna()]
results.reset_index()
print(results.head())

# How many words in the English Dictionary can be created with Element Symbols?
count_of_creatable = len(results)
print(count_of_creatable)

# What % is this of the total?
count_of_words = len(eng_dict)
proportion_of_dictionary = 100 * (count_of_creatable / count_of_words)
print(proportion_of_dictionary)
# plot results
