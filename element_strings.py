# open file
elements_file = open("elements.txt", "r")
elements = elements_file.read()
# extract symbols
elements = elements.split("\n")
symbols = []
for element in elements:
    symbols.append(element.split(",")[1])
symbols_file = open("symbols.txt", "w")
symbols_file.write(symbols.__str__)
print(symbols)