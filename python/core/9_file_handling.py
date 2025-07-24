## Write File ##
with open("fruits.txt", "w") as file:
    fruits = ["apple", "banana", "cherry"]
    for item in fruits:
        file.write(f"{item} \n")

## Read and Print ##
with open("fruits.txt", "r") as file:
    content = file.read()
    print(content)

## Word Counter (File Edition) ##
def count_words_in_file(filename):
    with open(filename, "r") as file:
        totalword = len(file.read().split())
        return totalword
    