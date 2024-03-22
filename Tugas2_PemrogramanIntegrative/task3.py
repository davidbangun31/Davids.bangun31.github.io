class Person:
    def __init__(self, berat, tinggi):
        self.berat = berat
        self.tinggi = tinggi

    @property
    def berat(self):
        return self._berat

    @berat.setter
    def berat(self, berat):
        self._berat = berat

    @property
    def tinggi(self):
        return self._tinggi

    @tinggi.setter
    def tinggi(self, tinggi):
        self._tinggi = tinggi

    def BMI_Value(self):
        if self.tinggi <= 0:
            return None
        return self._berat / (self._tinggi ** 2)

# Contoh penggunaan kelas
if __name__ == "__main__":
    berat = float(input("Masukkan berat (kg): "))
    tinggi = float(input("Masukkan tinggi (m): "))

    person = Person(berat, tinggi)
    bmi = person.BMI_Value()

    if bmi is not None:
        print(f"BMI Anda adalah: {bmi:.2f}")
    else:
        print("Tinggi tidak valid.")
