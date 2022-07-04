# Test kung lang kung macoconfirm yung pag-edit kasi di na ako marunong mag-python

input_list = []

def add_to_list():
    print("\n")
    input_list.append(int(input("Enter a number to add to the list: ")))
    print("\nSuccessfully added!")
    
def edit_element_in_list():
    pass

def delete_element_in_list():
    pass

while True:
    print(f"\n\nCurrent status of list: {input_list}\n\n")
    print("Choose one of the following:\n")
    print("[1] Add")
    print("[2] Edit")
    print("[3] Delete")
    print("[0] Exit")
    user_choice = int(input("Choice: "))

    if user_choice == 1:
        add_to_list()    
    elif user_choice == 2:
        edit_element_in_list()
    elif user_choice == 3:
        delete_element_in_list()
    elif user_choice == 0:
        break
    else:
        print("\nInvalid input. Try again!")
