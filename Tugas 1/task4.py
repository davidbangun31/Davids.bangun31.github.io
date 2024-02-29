def calculate_sum():
    # user memasukkan angka 
    number = int(input("Enter a number: "))

    total_sum = 0

    # menghitung jumlah 
    for i in range(1, number + 1):
        total_sum += i

    # menampilkan hasil
    print(f"The sum of values from 1 to {number} is: {total_sum}")

# memanggil fungsi
calculate_sum()
