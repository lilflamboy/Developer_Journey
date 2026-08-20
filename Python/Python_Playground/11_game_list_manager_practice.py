games = ["Chess", "Cricket", "Football", "Hockey", "Tennis"]
print("Current Games List:")
for game in games:
    print(game)
new_game = input("Enter a new game to add to the list:")
games.append(new_game)
print("Updated Games List:")
for game in games:
    print(game)
remove_game = input("Enter a game to remove from the list:")
if remove_game in games:
    games.remove(remove_game)
    print(f"{remove_game} has been removed from the list.")
else:
    print(f"{remove_game} is not in the list.")
games.sort()   
print("Final Games List:")
for game in games:
    print(game)            