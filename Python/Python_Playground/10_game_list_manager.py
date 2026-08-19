current_games = ["Chess","Cricket","Football","Hockey","Tennis"]
print("Current Games List:")
for game in current_games:  
    print(game)
new_game = input("Enter a new game to add to the list: ")    
current_games.append(new_game)
print("Updated Games List:")
for game in current_games:
    print(game)
remove_game = input("Enter a game to remove from the list: ")
if remove_game in current_games:
    current_games.remove(remove_game)
    print(f"{remove_game} has been removed from the list.")
else:
    print(f"{remove_game} is not in the list.")
print("Final Games List:")
for game in current_games:
    print(game)    
current_games.sort()
print("Sorted Games List:")    
for game in current_games:
    print(game)

    