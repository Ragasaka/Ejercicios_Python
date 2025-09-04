import os

FILENAME = "shopping_list.txt"
index = {}  # Dictionary: product_name -> file_position

def load_index():
    """Load existing products into the index dictionary."""
    if os.path.exists(FILENAME):
        with open(FILENAME, "r", encoding="utf-8") as f:
            while True:
                pos = f.tell()  # current position
                line = f.readline()
                if not line:
                    break
                fields = line.strip().split(",")
                if len(fields) == 4:
                    name = fields[0]
                    index[name] = pos


def add_product():
    """Add a product to the shopping list file."""
    name = input("Enter product name: ").strip()
    total_cost, quantity, unit_cost = 0.0, 0.0, 0.0
    
    # Prevent duplicates
    if name in index:
        print(f"❌ Product '{name}' already exists in the list.")
    else:
        try:
            quantity = int(input("Enter quantity: ").strip())
            unit_cost = float(input("Enter unit cost: ").strip())
        except ValueError:
            print("⚠️ Invalid input. Quantity must be integer and unit cost must be numeric.")
        else:
            total_cost = quantity * unit_cost
            
            # Append to file and record position
            with open(FILENAME, "a", encoding="utf-8") as f:
                pos = f.tell()  # position before writing
                line = f"{name},{quantity},{unit_cost},{total_cost}\n"
                f.write(line)
                index[name] = pos
            load_index()
            print(f"✅ Added: {name} | Qty: {quantity} | Unit: {unit_cost} | Total: {total_cost}")

def ask_products():
    """Ask for a product by name or list all products."""
    if not os.path.exists(FILENAME) or os.stat(FILENAME).st_size == 0:
        print("📂 Shopping list is empty.")
        return
    
    name = input("Enter product name to search (leave empty to list all): ").strip()
    
    if name == "":  # List all
        print("\n--- Shopping List ---")
        with open(FILENAME, "r", encoding="utf-8") as f:
            for line in f:
                fields = line.strip().split(",")
                if len(fields) == 4:
                    name, quantity, unit_cost, total = fields
                    print(f"🛒 {name} | quantity: {quantity} | Unit: {unit_cost} | Total: {total}")
    elif name in index:
            with open(FILENAME, "r", encoding="utf-8") as f:
                f.seek(index[name])
                fields = f.readline().strip().split(",")
            if len(fields) == 4:
                name, quantity, unit_cost, total = fields
                print(f"🛒 {name} | quantity: {quantity} | Unit: {unit_cost} | Total: {total}")
    else:
        print(f"❌ Product '{name}' not found.")

def update_product():
    """Update a product using its position in the file (from index)."""
    name = input("Enter product name to update: ").strip()
    total_cost, quantity, unit_cost = 0.0, 0.0, 0.0
    
    if name not in index:
        print(f"❌ Product '{name}' not found.")
        return
    
    try:
        quantity = int(input("Enter new quantity: ").strip())
        unit_cost = float(input("Enter new unit cost: ").strip())
    except ValueError:
        print("⚠️ Invalid input.")
    else:
        total_cost = quantity * unit_cost
        new_line = f"{name},{quantity},{unit_cost},{total_cost}\n"
        
        with open(FILENAME, "r", encoding="utf-8") as f:
            f.seek(index[name])
            _ = f.readline()             # read old product line
            rest_lines = f.readlines()   # read everything after it
    
        with open(FILENAME, "r+", encoding="utf-8") as f:
            f.seek(index[name])      # cut file before product
            f.write(new_line)            # write new product data
            for line in rest_lines:      # rewrite the rest
                f.write(line)
            
        load_index()
        print(f"✅ Updated: {name} | Qty: {quantity} | Unit: {unit_cost} | Total: {total_cost}")

def delete_product():
    """Delete a product by rewriting file starting from its position."""
    name = input("Enter product name to delete: ").strip()
    
    if name in index:    
        with open(FILENAME, "r", encoding="utf-8") as f:
            f.seek(index[name])
            _ = f.readline()
            rest_lines = f.readlines()  # read everything after the target line
        
        # Keep file content only up to product’s position
        with open(FILENAME, "r+", encoding="utf-8") as f:
            f.truncate(index[name])  # cut file right before target product
            # Rewrite the rest (skipping deleted product)
            f.seek(index[name])
            for line in rest_lines:
                f.write(line)
        
        load_index()
        print(f"🗑️ Deleted product '{name}'")
    else:
        print(f"❌ Product '{name}' not found.")



# Run the menu
with open(FILENAME, 'w') as f:
    print(f'{FILENAME} was created')
    
load_index()
while True:
        print("\n--- Options Menu ---")
        print("1. Add")
        print("2. Ask (View)")
        print("3. Update")
        print("4. Delete")
        print("5. Exit")
        
        choice = input("Choose an option (1-5): ").strip()
        
        match choice:
            case "1":  # Add
                data = load_index()
                add_product()
            
            case "2":  # Ask (View)
                ask_products()
            
            case "3":  # Update
                update_product()
            
            case "4":  # Delete
                delete_product()
            
            case "5":  # Exit
                print("Exiting program. Goodbye!")
                os.remove(FILENAME)
                break
            
            case _:  # Default case
                print("Invalid option. Please choose between 1-5.")
