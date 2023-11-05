'''
Jatketaan edellisen moduulin esimerkki, ks. sieltä tarvittaessa tarkemmat kommentit.
'''

class School:

    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.courses = []

    def add_course(self, course):
        self.courses.append(course)

    def remove_course(self, course):
        self.courses.remove(course)

    def fire_alarm(self):
        print(f'Kamalaa! 🔥 Palohäytys 🚒 koulussa {self.name}, lokaatiossa {self.location}')
        for course in self.courses:
            print(f'Kurssi käynnissä: {course.name}')
            course.check_students_on_course()


class Course:

    def __init__(self, name, teacher):
        self.name = name
        self.students = []
        self.teacher = teacher

    def check_coursename(self):
        print(f'Kurssin nimi on: {self.name}')

    def get_course_info(self):
        return f'Nimi: {self.name}\nOpettaja: {self.teacher.name}'

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, student):
        self.students.remove(student)

    def check_students_on_course(self):
        for student in self.students:
            # print(student)
            print(student.name)

    def add_credits_to_all(self, credit_units):
        for student in self.students:
            # kutsutaan Student olion metodeja!!!
            student.add_credits(credit_units)
            student.say_hello()

class Person:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print(f"Morjes! Olen {self.name}")

class Student(Person):

    count = 0

    def __init__(self, name, age=15):  # age oletusarvo 15, jossei määritelty kutsussa
        self.age = age
        self.credits = 0
        Student.count += 1
        # print(f"Uusi opiskelija luotu. Opiskelijoita on nyt yhteensä {Student.count}.")
        super().__init__(name)

    def say_hello(self):
        super().say_hello()
        print(f"Olen {self.age} vuotta. "
              f"Minulla on {self.credits} opintopistettä.")

    def change_name(self, new_name):
        self.name = new_name

    def add_credits(self, credits):
        # estä opintopisteiden meneminen negaativiseksi
        if self.credits + credits < 0:
            self.credits = 0
        else:
            self.credits = self.credits + credits

class Teacher(Person):
    def __init__(self, name, id_number):
        self.id_number = id_number
        super().__init__(name)
    def say_hello(self):
        super().say_hello()
        print("Id:" + str(self.id_number))

print('Hei, tervetuloa kouluun!')

# luodaan 3 opiskelijaa ja annetaan opintopisteet
st1 = Student("Mikko Mallikas", 38)
#print(st1)
st1.add_credits(3)
st1.say_hello()
st2 = Student("Iines Ankka", 34)
#print(st2)
st2.add_credits(3)
st2.say_hello()
st3 = Student("Rob Fury", 20)
#print(st3)
st3.add_credits(3)
st3.say_hello()

print(f'Uusia opiskeljoita on kurssilla {Student.count}')

print("*==========*")

# Luodaan opettaja, koska se vaaditaan kurssin luomiseksi
teacher1 = Teacher("Olli Opettaja", 5343)
teacher1.say_hello()

# Luodaan kaksi kusrssia, tsekataan kurssien kurssin nimi (metodi)
course1 = Course('Ohjelmisto1', teacher1)
course1.check_coursename()

course2 = Course('Ohjelmisto2', teacher1)


print("*==========*")

# lisätään oppilaat kursseille
# Mikko ja Iines ovat Ohjelmisto 1 kurssilla
# Iines ja Rob ovat Ohjelmisto 2 kurssilla

course1.check_coursename()
course1.students.append(st1)
course1.students.append(st2)
course1.check_students_on_course()

print("*==========*")

# parempi tapa on käyttää metodeja tähän toimintoon
# Student-olio (tai oikeastaan viittaus siihen) annetaan metodikutsun parametrina

course2.check_coursename()
course2.add_student(st2)
course2.add_student(st3)
course2.check_students_on_course()

print("*==========*")

# Oppilaat olet kurssilla 2 tosi ahkeria ja saavat lisää opintopisteitä!!!
course2.add_credits_to_all(5)

# Luodaan nyt kaksi koulua
# Metropolia ja Laura. MP saa Ohelmisto 1 ja Laurea Ohjelmisto 2.
# Molemmista tallennetan nimi ja lokaatio

print("*==========*")

school1 = School('Metropolia', 'Karamalmi')
school2 = School('Laurea', 'Leppävaara')
school1.add_course(course1)
school2.add_course(course2)

# apua koululla on palohälytys!!!!!
# Printatkaa koulun nimi, lokaatio, kurssit ja opiskelijat

school1.fire_alarm()

# Haetaan kurssin info
print(course1.get_course_info())

# kaikkia Student-, Teacher-, ja Person-luokista luotuja olioita voidaan käsitellä
# Person-tyyppisenä
randomPerson = Person("Random Kaveri")
persons = [st1, st2, st3, randomPerson, teacher1]
print("print all persons\n==========")
for p in persons:
    p.say_hello()