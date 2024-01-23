#Given two list of numbers, write a program to create a new list such that 
#the new list should contain odd numbers from the first list and even numbers from the second list.
given_list_1 = list()
given_list_1.append(10)
given_list_1.append(20)
given_list_1.append(25)
given_list_1.append(30)
given_list_1.append(35)

given_list_2 = list()
given_list_2.append(40)
given_list_2.append(45)
given_list_2.append(60)
given_list_2.append(75)
given_list_2.append(90)

new_list = list()

for i in range (5):
    if given_list_1[i] % 2 != 0:
        new_list.append(given_list_1[i])

for i in range (5):
    if given_list_2[i] % 2 == 0:
        new_list.append(given_list_2[i]) 

print('The new list will be:',new_list)