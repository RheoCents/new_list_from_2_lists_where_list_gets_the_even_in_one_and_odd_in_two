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

len_list_of_all = int(len(given_list_1)) + int(len(given_list_2))

for i in range (0, 5, 1):
    if given_list_1[i] % 10 == 0:
        new_list_1 = list()
        new_list_1.append(given_list_1[i])
        print(new_list_1)