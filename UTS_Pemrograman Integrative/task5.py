with open("input.txt", "r") as file:
    numbers = [int(line.strip()) for line in file]

sum_of_numbers = sum(numbers)
formatted_sum = "{:,}".format(sum_of_numbers)

print(f"Jumlah bilangan dengan pemisah koma dan tiga digit: {formatted_sum}")