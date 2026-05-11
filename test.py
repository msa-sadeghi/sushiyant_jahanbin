
all_students = [
    {'name' : 'ali' , 'age' : 12 , 'fav_sport' : 'soccer'}
]

for i in range(2):
    name = input('enter name')
    age = input('enter age')
    fav_sport = input('enter fav sport')
    student_info = {'name' : name , 'age' : age , 'fav_sport' : fav_sport}
    all_students.append(student_info)
print(all_students)