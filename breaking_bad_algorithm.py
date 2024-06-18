# open file
elements_file = open("elements.txt", "r")
elements = elements_file.read()
# extract symbols
elements = elements.split("\n")

single_symbols = {}
double_symbols = {}
for element in elements:
    element = element.split(",")
    if len(element[1]) == 1:
        single_symbols[element[1]] = element[0]
    else:
        double_symbols[element[1]] = element[0]

# print(single_symbols)
# print(double_symbols)


def check_single_symbol(word: str):
    return 0

def check_double_symbol(word: str):
    return 0

def create_string_from_element_symbols(word: str) -> list:
    pos = 0
    while pos < len(word):
        check_single_symbol(word[pos])
        check_double_symbol(word[pos])
    return []

if __name__ == "__main__":
    valid_word = False
    while not valid_word:
        word = input("Please enter a word").upper().strip()
        valid_word = word.isalpha()
    create_string_from_element_symbols(word)