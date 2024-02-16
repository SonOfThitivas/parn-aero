# initialization
import random
n_students = 20
days_in_year = 365
n_simulations = 10000
max_diffs = [] # used to store the longest period of each classroom

# #################################
# Write down your code from here. #
# #################################

for i in range(n_simulations): # create data to find probability with 10,000 simulations
    # intiialize variables
    a_classroom = [] # collect all student's birthday
    all_period = [] # collect all the period of student's birthday (older student - younger student)
    
    for j in range(n_students): # random 20 student's birtdays
        a_classroom.append(random.randint(1,days_in_year)) # random between 1-365 day
    
    a_classroom.sort() # sort the days easily to find the period
    for k in range(0,len(a_classroom),2): # step +2
        all_period.append(a_classroom[k+1] - a_classroom[k]) # compute the period Ex. student2 - student1, student4 - student3
        
    max_diffs.append(max(all_period)) # collect the longest period of each simulate

print("Probability: ", sum(max_diffs)/len(max_diffs))