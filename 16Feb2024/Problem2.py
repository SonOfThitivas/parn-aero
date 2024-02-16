# Problem 2: Collect students' info and sort it
def sorting(sort_by, l):
    # Initialize lists to store id numbers, first names, and last names
    students_list_sorted = []
    id_list, firstname_list, lastname_list = [], [], []
    
    # Extract id numbers, first names, and last names from the input list
    for i in range(len(l)):
        id_list.append(l[i][0])
        firstname_list.append(l[i][1])
        lastname_list.append(l[i][2])
    
    # Sort based on the chosen criteria
    if sort_by == "id number":
        id_list.sort()
        for id in id_list:
            for j in range(len(l)):
                if id in l[j]:
                    students_list_sorted.append([l[j][0], l[j][1], l[j][2]])
                    break
        
    elif sort_by == "firstname":
        firstname_list.sort()
        for firstname in firstname_list:
            for j in range(len(l)):
                if firstname in l[j]:
                    students_list_sorted.append([l[j][0], l[j][1], l[j][2]])
                    break
        
    else:  # sort_by == "lastname"
        lastname_list.sort()
        for lastname in lastname_list:
            for j in range(len(l)):
                if lastname in l[j]:
                    students_list_sorted.append([l[j][0], l[j][1], l[j][2]])
                    break
    
    return students_list_sorted

# Function to print the list of students
def print_list(l):
    print("id number ,", "firstname ,", "lastname")
    for i in range(len(l)):
        print(l[i][0], ',', l[i][1], ',', l[i][2])

# Initialize an empty list to store students' information
students_list = []

# Loop to collect students' information
while True:
    user_input = [e for e in input(
        """Enter the info that fellow with:
        student id number/firstname/lastname
        (enter '0' to stop)
        >> """
        ).split('/')]
    
    # Break the loop if the user enters '0'
    if user_input[0] == '0':
        break
    # Check if the input is in the correct format
    elif len(user_input) != 3:
        print("\nThat is not the correct one. Please, try again\n")
        continue
    
    students_list.append(user_input)

# Loop to determine the sorting criteria
while True:
    sort_specific = input("""What would you like to sort with?
                        (id number, firstname, lastname)
                        >> """)
    
    # Break the loop if the input is valid
    if sort_specific in ["id number", "firstname", "lastname"]:
        break
    else:
        print("\nThat is not the correct one. Please, try again\n")
        
# Sort the list based on the chosen criteria and print the sorted list
sorted_list = sorting(sort_specific, students_list)
print_list(sorted_list)
