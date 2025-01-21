#string methods like upper, lower soon
#strings are immutable

a="saicharan"
b="SAICHARAN"
print(a.upper()) #coverts into upper string
print(b.lower()) #converts into lower string


#strip
c="  hello bhai  "
print(c.strip())

#rstrip: which is used to remove the the mentioned string 
d="saicharan!!!"
print(d.rstrip("!"))

#replace
print(a.replace("saicharan","ram"))

#split
e="hello, bro how are you"
print(e.split())

#capitalize: capitalize the each starting word
print(e.capitalize())

#center
print(a.center(50))

#count: counting the specific word how many times repetiting
print(a.count("a"))

#find
print(a.find("a"))

#index:
f="iam fine"
print(f.index("fine"))

#title
print(f.title())
