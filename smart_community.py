members = []
member_ids = set()

# add members (heads only)
def add_members():
    print("Add Members")
    print("-------------------------------")
    member_id = input("Member ID: ") # takes id
    # prevents duplicates
    if member_id in member_ids:
        print("This ID already exists")
        return 
    
    member_name = input("Member name: ")
    member_age = input(f"{member_name}'s age: ")

    # validates the age
    if not member_age.isdigit():
        print(f"Sorry, {member_name}'s age must be a number.")
        return 
    
    member_age = int(member_age) # typecasting the age
    # member dictionary
    member = {
        "id": member_id,
        "name": member_name,
        "age": member_age
    }

    members.append(member) # adds it to the list
    member_ids.add(member_id) # adds it to the set to prevent duplicates

    print("Member added successfully")

# Remove members (heads only)
def remove_members():
    print("Remove member")
    print("-----------------------")
    user_choice = input("Remove by ID or name? (id/name): ").lower()

    # remove by id
    if user_choice == "id":
        id_to_remove = input("Member ID: ")
        for member in members:
            if member["id"] == id_to_remove: # compare before removing
                members.remove(member)
                member_ids.remove(id_to_remove)
                print(f"Successfully removed {member['name']}")
                return
    # remove by name
    elif user_choice == "name":
        name_to_remove = input("Member's name: ").lower()# lower because of comparison
        for member in members:
            if member["name"].lower() == name_to_remove:
                members.remove(member)
                member_ids.remove(member["id"])
                print(f"Successfully removed {member['name']}")
                return
    else:
        print("Invalid Choice.")
        return
    # member not in the list 
    print("Member not found") 



# Main Program

print("Welcome to the Smart Community")
print("------------------------------")


while True:
    # role selection
    role = input("Enter your role (head/member): ").lower()
    if role in ["head", "member"]:
        break
    print("Invalid role.")

while True:
    if role == "head":
        # Head Menu
        print("""
    -------------------------------
        1. Add a member
        2. Remove members
        3. View members
        4. Search member
        5. Total members
        6. Exit   
    --------------------------------          
        """)

        user_choice = input("Select an option: ")
        if user_choice == "1":
            add_members()
        elif user_choice == "2":
            remove_members()
        elif user_choice == "3":
            view_members(role)
        elif user_choice == "4":
            search_members(role)
        elif user_choice == "5":
            total_members()
        elif user_choice == "6":
            print("Thank You for using Smart Community")
            break
        else:
            print("Invalid option.")
    else:
        # Member menu
        print("""
    -----------------------------
        1. View members
        2. Search members
        3. Total members
        4. Exit
    -----------------------------
        """)
        user_choice = input("Select an option: ")
        if user_choice == "1":
            view_members(role)
        elif user_choice == "2":
            search_members(role)
        elif user_choice == "3":
            total_members()
        elif user_choice == "4":
            print("Thank You for using Smart Community")
            break
        else:
            print("Invalid option")