def determine_size():
    # user memasukkan angka
    number = float(input("Enter a number: "))

    # melakukan pengecekan
    if number < 100:
        print("Small")
    elif number > 200:
        print("Large")
    else:
        print("Medium")

# memanggil fungsi
determine_size()
