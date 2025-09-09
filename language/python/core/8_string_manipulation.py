## Clean Up Text ##
raw = "   Hello, Python!    "
result = raw.strip().lower().replace("python", "world")
print(result)

## Word Counter ##
def count_words(text):
    totalword = len(text.split())
    return totalword

## Username Generator ##
def create_username(name, id):
    username = name.split()[0].lower() + str(id)
    return username