#LIST
#students = ["Hermione", "Harry", "Ron", "Draco"]
#houses = ["Gryffindor", "Gryffindor", "Gryffindor", "Slytherin"]

#for student in students:
  #  print(student)

#for i in range(len(students)):
 #   print(i+1, students[i])

#dictionary

#students= {
 #   "Hermione": "Gryffindor",
  #  "Harry": "Gryffindor",
   # "Ron": "Gryffindor",
    #"Draco": "Slytherin"
#}

#for student in students:
 #  print(student, ": " ,students[student])

#for student in range(len(students)):
 #   print(student+1, ": " ,students[student])


students = [
    {"name":"Hermione", "house": "Gryffindor", "patronous":"Otter"},
    {"name":"Harry", "house": "Gryffindor", "patronous":"Stag"},
    {"name":"Ron", "house": "Gryffindor", "patronous":"Jack Russel terrier"},
    {"name":"Draco", "house": "Slytherin", "patronous":None}
 ]

for student in students:
    print(student["name"], student["house"], student["patronous"], sep=", ")

#print(students["Hermione"])
#print(len(students))
