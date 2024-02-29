import math

def calculate_monthly_salary():
    # user memasukkan jumlah gaji tahunannya
    salary = float(input("Enter your annual salary: "))

    # Menghitung jumlah gaji
    monthly_salary = math.ceil(salary / 12)

    # Menampilkan Hasil
    print(f"Your monthly salary is: {monthly_salary}")

# Memanggil Fungsi
calculate_monthly_salary()
