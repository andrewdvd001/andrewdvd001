## List Manager ##
food = ["Bakso", "Ramen", "Pizza", "Burger", "Soda"]
food[1] = "Mie Ayam"
food.append("Milk")
food.remove("Burger")
print(food)

## Tuple Unpacking ##
point = (5, 10)
x, y = point
print(f"x = {x}, and y = {y}")


## List Slice ##
def slice_middle(lst):
    mid = len(lst) // 2
    return lst[mid - 1:mid + 2]