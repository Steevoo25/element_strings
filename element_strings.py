# open file
symbols_file = open("symbols.txt", "r")
data = symbols_file.read()
# extract symbols
elements = data.split("\n")
symbols = []
for element in elements:
    symbols.append(element.split(",")[1])
