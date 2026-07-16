shopping_list = []

shopping_list.append("milk")
shopping_list.append("egg")
shopping_list.append("bread")
shopping_list.append("rice")

shopping_list.remove("bread")

print("Shopping List:")

for item in shopping_list:
    print(item)

print("Total Items:", len(shopping_list))