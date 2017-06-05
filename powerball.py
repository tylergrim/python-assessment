# Tyler Grim
# Greenfire Python Coding Assessment
# Powerball.py

from random import *

# Set up variables

def compare(list1, list2):

    correct_list = []
    num_correct = 0;
    winners = []
    differences = []
    random_index = randint(0,6)
    for i in range(len(list1)):
        for j in range(6):
            if(list1[i][2][j] == list2[j]):
                num_correct += 1
        correct_list.append(num_correct)
        num_correct = 0;
    m = max(correct_list)
    for i in range(len(correct_list)):
        if correct_list[i] == m:
            winners.append(i)
    if(len(winners)>1):
        random_number = list2[random_index]
        for i in winners:
            winners_number = list1[i][2][random_index]
            diff = abs(random_number - winners_number)
            differences.append(diff)
        try:
            smallest = min(differences)
            winning_index = list1.index(smallest)
            return ("The winner is: " + list1[winning_index][0] + " " + list1[winning_index][1])
        except ValueError:
            return "Multiple players have picked the same number of correct numbers and have the same number in the tiebreaker!!!"
        else:
            winning_index = winners[0]
            return "The winner is: " + list1[winning_index][0] + " " + list1[winning_index][1]
    
            
    

employee_list = []
lottery_numbers = []

for i in range(5):
    val = randint(1,69)
    while(val in lottery_numbers):
        val = randint(1,69)
    lottery_numbers.append(val)
    
lottery_numbers.append(randint(1, 26))

print(lottery_numbers)

print('''Welcome to the Powerball lottery drawing application. Start by entering
    the first and last name of an employee, and continue to enter their
    favorite numbers.\n
    *****RULES*****\n
    1. No duplicate numbers must be given\n
    2. The first five numbers should be between the values of 1 - 69.\n
    3. The sixth number should be between the values of 1 - 26.\n
    4. Employee with the most matched numbers will win, if there is a tie,
    a random picked number will be chosen, the employee's whose favorite number
    is closest to the chosen number will be deemed the winner.
    \n\n
    *****HOW TO USE THE PROGRAM*****
    \n
    1. Start by entering the employee's first and last name.\n
    2. Next enter in each of the employee's favorite five numbers.
    3. When completed entering one employee, enter in any value to enter
    in another employee, or simply press enter with no value to quit.
    ''')

choice = input("Enter an employee? <LEAVE BLANK TO QUIT>")

while(choice != ""):

    num_list = []
    employee = []
    first_name = input("Please enter the employee's first name: ")
    last_name = input("Please enter the employee's last name: ")
    employee.append(first_name)
    employee.append(last_name)
    
    fav1 = int(input("Please enter the employee's favorite number (1-69): "))
    while (fav1 < 1 or fav1 > 69):
        print("FAILED! Please enter a number between the values of 1 and 69: ")
        fav1 = int(input("Please enter the employee's favorite number (1-69): "))
    num_list.append(fav1)
    
    fav2 = int(input("Please enter the employee's favorite number (1-69): "))
    while (fav2 < 1 or fav2 > 69):
        print("FAILED! Please enter a number between the values of 1 and 69: ")
        fav2 = int(input("Please enter the employee's favorite number (1-69): "))
    while (fav2 in num_list):
        print("This number has already been selected; Please enter a different number!")
        fav2 = int(input("Please enter the employee's favorite number (1-69): "))
    num_list.append(fav2)
    
    fav3 = int(input("Please enter the employee's favorite number (1-69): "))
    while (fav3 < 1 or fav3 > 69):
        print("FAILED! Please enter a number between the values of 1 and 69: ")
        fav3 = int(input("Please enter the employee's favorite number (1-69): "))
    while (fav3 in num_list):
        print("This number has already been selected; Please enter a different number!")
        fav3 = int(input("Please enter the employee's favorite number (1-69): "))
    num_list.append(fav3)
    
    fav4 = int(input("Please enter the employee's favorite number (1-69): "))
    while (fav4 < 1 or fav4 > 69):
        print("FAILED! Please enter a number between the values of 1 and 69: ")
        fav4 = int(input("Please enter the employee's favorite number (1-69): "))
    while (fav4 in num_list):
        print("This number has already been selected; Please enter a different number!")
        fav4 = int(input("Please enter the employee's favorite number (1-69): "))
    num_list.append(fav4)
    
    fav5 = int(input("Please enter the employee's favorite number (1-69): "))
    while (fav5 < 1 or fav5 > 69):
        print("FAILED! Please enter a number between the values of 1 and 69: ")
        fav5 = int(input("Please enter the employee's favorite number (1-69): "))
    while (fav5 in num_list):
        print("This number has already been selected; Please enter a different number!")
        fav5 = int(input("Please enter the employee's favorite number (1-69): "))
    num_list.append(fav5)
    
    fav6 = int(input("Please enter the employee's favorite number (1-26): "))
    while (fav6 < 1 or fav6 > 26):
        print("FAILED! Please enter a number between the values of 1 and 26: ")
        fav6 = int(input("Please enter the employee's favorite number (1-26): "))
    num_list.append(fav6)

    
    employee.append(num_list)
    employee_list.append(employee)

    choice = input("Enter an employee? <LEAVE BLANK TO QUIT>")

print(compare(employee_list, lottery_numbers))
