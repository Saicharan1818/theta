mathematics = float(input("Enter marks for mathematics: "))
english = float(input("Enter marks for english: "))
science = float(input("Enter marks for science: "))

average = (mathematics + english + science) / 3
if average >= 90:
    print("Grade: A")
elif 80 <= average < 90:
    print("Grade: B")
elif 70 <= average < 80:
    print("Grade: C")
else:
    print("Grade: Fail")

