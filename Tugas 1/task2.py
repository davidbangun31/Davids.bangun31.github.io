import math

def divide_by_three():
    # user memasukkan bilangan bulat
    number = int(input("Enter a whole number: "))

    # lakukan pembagian dan pembulatan
    result = math.ceil(number / 3)

    # menampilkan hasil dengan desimal
    formatted_result = "{:.3f}".format(result)
    print(f"The result is: {formatted_result}")

# memanggil
divide_by_three()
