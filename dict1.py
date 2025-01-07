students = {
    1: {"name" : "jayanth" , "age":20},
    2: {"name" : "gundu" , "age":22},
    3: {"name" : "boogi" , "age":23},
    4: {"name" : "chemcha" , "age":19},
    5: {"name" : "balu" , "age":21},
}

for student_id, details in students.items():
    print(f"student_ID: {student_id},Name: {details['name']},Age: {details['age']}")