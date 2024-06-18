# open file
elements_file = open("elements.txt", "r")
elements = elements_file.read()
# extract symbols
elements = elements.split("\n")

symbols = {}
for element in elements:
    element = element.split(",")
    symbols[element[1]] = element [0]

print(symbols)

def create_string_from_element_symbols(word: str) -> list:
    return []

if __name__ == "__main__":
    valid_word = False
    while not valid_word:
        word = input("Please enter a word").upper().strip()
    valid_word = word.isalpha()