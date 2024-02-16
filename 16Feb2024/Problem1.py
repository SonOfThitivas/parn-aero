# Problem 1 unique values
def unique(l): # define a function that return a list of unique values
    unique_list = [] # collect unique values
    for x in l: # loop all item in the list with x
        if x not in unique_list:
            unique_list.append(x) # add it to the the list
            
    if unique_list[0].isalpha: # if it's alphabets
        return sorted(unique_list)
    else: # if it's numbers
        new_list = [int(n) for n in unique_list] # convert string to integer
        return sorted(new_list)

# program start
user_list = [e for e in input("Enter only numbers or strings with space: ").split()]
print(unique(user_list))