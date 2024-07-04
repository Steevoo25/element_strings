from argparse import ArgumentParser
import csv
import os
# open file
elements_file = open("elements.txt", "r")
elements = elements_file.read()
elements = elements.split("\n")

# Initialise dicts
single_symbols = {}
double_symbols = {}

# sort symbols into single and double symbols, with singles being made of one character and doubles made of two
for element in elements:
    element = element.split(",")
    if len(element[1]) == 1:
        single_symbols[element[1]] = element[0]
    else:
        double_symbols[element[1]] = element[0]

def check_single_symbol(word: str):  
    return word in single_symbols.keys()

def check_double_symbol(word: str):
    return word in double_symbols.keys()

def create_string_from_element_symbols(word: str):
    pos = 0
    elements_to_create = []
    single_just_used = False

    while pos < len(word):
        if check_single_symbol(word[pos]):
            elements_to_create.append(single_symbols[word[pos]])
            pos +=1
            single_just_used = True

        elif check_double_symbol(word[pos:pos+2].capitalize()):
            elements_to_create.append(double_symbols[word[pos:pos+2].capitalize()])
            pos +=2
            single_just_used = False

        else:
            # Case where a single symbol has been selected but cannot go any further, so need check double symbols starting from the previous character
            if single_just_used:
                if check_double_symbol(word[pos-1:pos+1].capitalize()):

                    elements_to_create.pop(len(elements_to_create)-1) # Remove most recent addition to list
                    elements_to_create.append(double_symbols[word[pos-1:pos+1].capitalize()])
                    pos +=1
                    single_just_used = False
                else: return None
            else: return None

    return elements_to_create

def setup_parser():
    arg_parser = ArgumentParser(description='A program that checks if a given word can be constructed using scientific element Symbols')
    arg_parser.add_argument('-f', help='Path to file of words to check. File must be CSV format. Writes results to a file in the current directory')

    args = arg_parser.parse_args()
    try:
        file = getattr(args)
    except TypeError:
        file = None
    finally:
        return file

def run_cli():
    valid_word = False
    while not valid_word:
        word = input("Please enter a word (Press Q to quit)\n").upper().strip()
        valid_word = word.isalpha()
    while not word == 'Q':
        word = input("Please enter a word (Press Q to quit)\n").upper().strip()
        result = create_string_from_element_symbols(word)
        if result == None and not word == 'Q':
            print("Word not possible:", word)
        else:
            print(word, "passes the Breaking Bad test\n", result)

def run_file(path:str):

    current_dir = os.getcwd()
    results = []
    print('Opneing File:', path)

    with open(path, 'r') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        for row in csv_data:
            print(row)
            result = create_string_from_element_symbols(row)
            results.append(result)

    results_path = current_dir + 'results.csv'
    print("Writing results to",results_path )

    with open(results_path, 'w+') as results_file:
        results_writer = csv.writer(results_file, delimiter=',\n')
        results_writer.writerows(results)
    return


def main(path):
    if path is None:
        run_cli()
    else:
        try:
            run_file(path)
        except FileNotFoundError:
            print("File Error")
    return

if __name__ == "__main__":
    path = setup_parser()
    main(path)