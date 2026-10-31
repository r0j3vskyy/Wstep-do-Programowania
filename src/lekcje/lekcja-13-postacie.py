class Lucznik:
    def __init__(self, nazwa, zycie, zrecznosc, ptaktyki):
        self.nazwa = nazwa
        self.zycie = zycie
        self.zrecznosc = int(zrecznosc)
        self.ptaktyki = int(ptaktyki)

    def is_alive(self):
        return self.zycie > 0
    
    def take_damage(self, dmg):
        self.zycie -= dmg
        if self.zycie <= 0:
            self.zycie = 0
            print(f'{self.nazwa} nie żyje.')
    
    def githp(self):
        if self.zycie > 100:
            self.zycie = 100
        if self.zycie <= 0:
            self.zycie = 0
    
    def atak(self):
        dmg = self.zrecznosc*self.ptaktyki*self.zycie
        return dmg



class Wojownik:
    def __init__(self, nazwa, zycie, sila, ptaktyki):
        self.nazwa = nazwa
        self.zycie = zycie
        self.sila = int(sila)
        self.ptaktyki = int(ptaktyki)

    def is_alive(self):
        return self.zycie > 0
    
    def take_damage(self, dmg):
        self.zycie -= dmg
        if self.zycie <= 0:
            self.zycie = 0
            print(f'{self.nazwa} nie żyje.')
    
    def githp(self):
        if self.zycie > 100:
            self.zycie = 100
    
    def atak(self):
        if self.zycie < 20:
            self.zycie *= 1.5
        dmg = self.sila*self.ptaktyki*self.zycie
        return dmg
