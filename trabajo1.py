last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# Your code below: 
 #creacion de lista doble o bidimensional para materias y calificaciones
#1
Subjects=["Fisica", "Calculus", "Poesia", "Historia"]
#2
Grades=[98, 97, 85, 88]
#3
Gradesbook=[Subjects, Grades]
#4
print("Lista Primaria:")
print(Gradesbook)
#5
Subjects.append("Computer Science")
Grades.append(100)
#6
Subjects.append("Visual Arts")
Grades.append(93)
#7
print("Lista Con Datos Nuevos:")
print(Gradesbook)
#8
Gradesbook[1][-1]+=5
print("Lista Con Datos Modificados:")

print(Gradesbook)
#9
Grades.remove(88)
Grades.append("Pass")
#10
print("Agregando el valor de Pass a la nota de poesia:")
print(Gradesbook)