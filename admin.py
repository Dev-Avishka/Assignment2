import json

file_path = 'data.txt'

# load data at start
try:
    with open(file_path, 'r') as file:
        data = json.load(file)
except:
    data = []

# functions for category/item management

def add_category(category_name):
    """Add a new category with 2-5 options."""
    name_lower = category_name.lower()
    if any(cat['name'].lower() == name_lower for cat in data):
        print("Error: Category already exists!")
        return

    print("Enter 2-5 options (blank to finish):")
    options = []
    while len(options) < 5:
        opt = input(f"Option {len(options)+1}: ").strip()
        if not opt:
            break
        if any(o['name'].lower() == opt.lower() for o in options):
            print("Error: Option already added!")
            continue
        options.append({"name": opt, "votes": 0})
    
    if len(options) < 2:
        print("Error: Need at least 2 options!")
        return

    data.append({"name": category_name, "options": options})
    save_data(data)
    print(f"Category '{category_name}' added.\n")

def add_item_to_category(category_name, item_name):
    """Add an item to existing category."""
    for cat in data:
        if cat['name'].lower() == category_name.lower():
            if any(o['name'].lower() == item_name.lower() for o in cat['options']):
                print("Error: Item already exists!")
                return
            cat['options'].append({"name": item_name, "votes": 0})
            save_data(data)
            print(f"Item '{item_name}' added to '{category_name}'.")
            return
    print(f"Category '{category_name}' not found.")

def list_categories():
    """List all categories with index and option count."""
    if not data:
        print("No categories saved.\n")
        return
    for i, cat in enumerate(data, 1):
        print(f"{i}) {cat['name']} ({len(cat['options'])} options)")
    print()

def search_category(search_term):
    """Search categories by name (case-insensitive)."""
    if not data:
        print("No categories saved.\n")
        return
    results = [cat for cat in data if search_term.lower() in cat['name'].lower()]
    if not results:
        print("No results found.\n")
        return
    for i, cat in enumerate(results, 1):
        print(f"{i}) {cat['name']} ({len(cat['options'])} options)")
    print()

def delete_category(index):
    """Delete category by index (1-based)."""
    if not data:
        print("No categories saved.\n")
        return
    if 0 <= index-1 < len(data):
        removed = data.pop(index-1)
        save_data(data)
        print(f"Category '{removed['name']}' deleted.\n")
    else:
        print("Invalid index!")

# functions for input, saving data

def input_something(prompt):
    while True:
        val = input(prompt).strip()
        if val:
            return val
        print("Cannot be empty!")

def input_int(prompt, max_value):
    while True:
        try:
            n = int(input(prompt))
            if 1 <= n <= max_value:
                return n
            print(f"Must be 1-{max_value}")
        except:
            print("Invalid number!")

def save_data(data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

#main function
def main():
    print("Welcome to the 'One Must Go' Admin Program!\n")
    
    while True:
        print("Choose [a]dd category, add [i]tem, [l]ist, [s]earch, [d]elete, [q]uit")
        choice = input("> ").strip().lower()

        if choice == 'a':
            name = input_something("Enter category name: ")
            add_category(name)

        elif choice == 'i':
            cat = input_something("Category to add to: ")
            item = input_something("Item name: ")
            add_item_to_category(cat, item)

        elif choice == 'l':
            list_categories()

        elif choice == 's':
            term = input_something("Search term: ")
            search_category(term)

        elif choice == 'd':
            if data:
                list_categories()
                idx = input_int(f"Delete index (1-{len(data)}): ", len(data))
                delete_category(idx)
            else:
                print("No categories to delete.\n")

        elif choice == 'q':
            print("Goodbye! Thank you for using One must go program.")
            break

        else:
            print("Invalid choice.\n")

if __name__ == "__main__":
    main()