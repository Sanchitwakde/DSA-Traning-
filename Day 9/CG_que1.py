# 1. Problem Statement - Raj wants to know the maximum marks scored by him in each semester.
# The mark should be between 0 to 100, if it goes beyond the range display "You have entered
# invalid mark.”

# Sample Input 1:
# · Enter no of semester:
# 3
# · Enter no of subjects in 1 semester:
# 3
# · Enter no of subjects in 2 semester:
# 4
# · Enter no of subjects in 3 semester:
# 2
# · Marks obtained in semester 1:
# 50
# 60
# 70
# · Marks obtained in semester 2:
# 90
# 98
# 76
# 67
# · Marks obtained in semester 3:
# 89
# 76
# Sample Output 1:
# . Maximum mark in 1 semester:70
# . Maximum mark in 2 semester:98
# . Maximum mark in 3 semester:89


snum = int(input("Enter number of Sem: "))
sub = 0
marks = 0
marks_max = 0
for i in range(snum): 
    sub = int(input(f"Enter number of subject in Sem {i+1}:"))
    maxi = []

    for n in range(sub):
        marks = int(input(f"Enter marks obtained in Sem {i+1}:"))

        if marks < 0 or marks > 100:
            print("You have entered invalid mark.")
        else:
            maxi.append(marks)

    marks_max = max(maxi)
    print(f"Maximum marks in semester {i+1}:",marks_max)


