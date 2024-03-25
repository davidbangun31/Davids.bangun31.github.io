import datetime

num = int(input("Masukkan bilangan bulat: "))
days_in_year = 365  # Atau 366 untuk tahun kabisat

result = num / days_in_year
print(f"Hasil: {result:.11f}")