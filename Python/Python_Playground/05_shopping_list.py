shopping_list = []

for i in range(5):
    input_item = input(f"Enter an item {i + 1}: ")
    shopping_list.append(input_item)

   
print ("Shopping List:")
for item in shopping_list:
    print(item)

print("Total Items:", len(shopping_list))
