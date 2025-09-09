## Dictionary Access ##
book = {
    "title": "Atomic Physics Fundamental",
    "author": "Yusman Wiyatno",
    "year": 2015,
    "pages": 100
    }
print(book.get("title"))
print(book.get("author"))
book["rating"] = 4.5
book["year"] = 2017
book.pop("pages")

## Set Operation ##
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print(set1.union(set2), set1.intersection(set2), set1.difference(set2))

## Dictionary Merger Function ##
def mergedicts(d1, d2):
    newdict = d1.copy()
    newdict.update(d2)
    return newdict