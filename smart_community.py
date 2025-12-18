members = []
member_ids = set()



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