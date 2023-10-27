class Auto:
    def __init__(self, rekisteritunnus, vari):
        self.rekisteritunnus = rekisteritunnus
        self.vari = vari


class Maalaamo:
    def maalaa(self, auto, vari):
        auto.vari = vari


maalaamo = Maalaamo()
auto = Auto("ABC-123", "keltainen")
print(f"Auto on {auto.vari}")
maalaamo.maalaa(auto, "punainen")
print(f"Auto on nyt {auto.vari}")
