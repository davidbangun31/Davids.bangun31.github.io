def calculate_sum_until_minus_one():
    # Initialize a variable to store the sum
    total_sum = 0

    while True:
        # user memasukkan angka
        num = int(input("Enter a number (or -1 to stop): "))

        # periksa apakah pengguna memasukkan angka -1 untuk menghentikan perulangannya
        if num == -1:
            break

        # tambahkan angka untuk dijumlah total 
        total_sum += num

    # menampilkan
    print(f"The sum of all entered numbers is: {total_sum}")

# memanggil fungsi
calculate_sum_until_minus_one()
