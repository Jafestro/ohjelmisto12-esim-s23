class Student:

    count = 0

    def __init__(self, name, age=0):  # age oletusarvo 15, jossei määritelty kutsussa
        self.name = name
        self.age = age
        self.credits = 0
        Student.count += 1
        print(f"Uusi opiskelija luotu. Opiskelijoita on nyt yhteensä {Student.count}.")

    def say_hello(self):
        print(f"Morjes! olen {self.name}, {self.age} vuotta. "
              f"Minulla on {self.credits} opintopistettä.")

    def change_name(self, new_name):
        self.name = new_name

    def add_credits(self, credits):
        # estä opintopisteiden meneminen negaativiseksi
        if self.credits + credits < 0:
            self.credits = 0
        else:
            self.credits = self.credits + credits


st1 = Student("Mikko Mallikas", 38)
st1.say_hello()
st1.change_name("Uusi nimi")
st1.say_hello()
st2 = Student("Iines Ankka" )
st2.say_hello()

st1.add_credits(6)
st2.add_credits(3)
st2.add_credits(-10)
st1.add_credits(15)

st1.say_hello()
st2.say_hello()

print("*==========*")
# Luodaan 10 uutta opiskelijaa lisää ja tallennetaan viittaukset listaan
students = []
for i in range(10):
    new_student = Student("Opiskelija " + str(i))
    new_student.add_credits(30)
    students.append(new_student)
# lisätään myös aiemmin luotujen kahden opiskelijaolion viittaukset listalle
students.append(st1)
students.append(st2)
# Käydään kaikki listalla olevat opiskelijat läpi
for student in students:
    student.say_hello()