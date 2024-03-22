def main():
    try:
        with open("indata.txt", "r") as file:
            numbers = [int(line.strip()) for line in file]

        total = sum(numbers)
        print(f"{total:.2f}")
    except FileNotFoundError:
        print("File 'indata.txt' tidak ditemukan.")
    except ValueError:
        print("File 'indata.txt' berisi data yang tidak valid.")

if __name__ == "__main__":
    main()
