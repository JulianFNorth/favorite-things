favorites = {
    "dog": "Retriever",
    "place": "My house",
    "food": "Pizza"
}

def display_favs(favorites):
    return f"Your favorite categories are: {', '.join(favorites)}"

def type_category(favorites):
    category = ''
    while category not in favorites:
        category = input("What category would you like to input? ")
        if category not in favorites:
            print("Category not available!\n")
    return f"My favorite for this is: {favorites[category]}"

def new_category(favorites):
    choice = ''
    while choice.lower() not in ['y', 'yes', 'n', 'no']:
        choice = input("Would you like to add a new category (y/n)? ")
        if choice.lower() not in ['y', 'yes', 'n', 'no']:
            print("Please enter a valid choice!")
    if choice.lower() in ['y', 'yes']:
        add_category(favorites)

def add_category(favorites):
    cat = input("What is your new category? ")
    fav = input("What is your favorite? ")
    if cat in favorites:
        print("Category already exists!")
    else:
        favorites[cat] = fav
    print("\nHere are all your favorites:")
    for cat, fav in favorites.items():
        print(f"{cat}: {fav}")
    return favorites

def main():
    print("Welcome to Julian's Fav Tracker!")
    print(display_favs(favorites))
    
    print("\n--- View a Category ---")
    print(type_category(favorites))
    
    print("\n--- Add a New Category ---")
    new_category(favorites)

    print("\nSee your later!")

main()