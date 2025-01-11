string = "do what i say to the world"
for word in string.split():
    if len(word) % 2 == 0:
        print(word)


#2
string = "do what i say to the world"
list = [1,2,3,4]
for word in string.split():
    if len(word) % 2 == 0:
        print(word)

#3 question find the length of the string if the length of the 
#string is more than 3 print the first letter of the word
#output: w
string = " where is hyderabad"
for word in string.split():
    if len(word) > 3:
            print(word[0])




#COVERT THE STRING INTO LIST
string = "welcome to the world"
list = [i for i in string.split()]
print(list)

#expected output :[to]
string = "welcome to the world"
list = [i for i in string.split() if len(i) == 2]
print(list)
