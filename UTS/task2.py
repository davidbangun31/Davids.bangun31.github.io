def calculate_product(n):
    product = 1
    for i in range(1, n + 1):
        product *= i
    return product

def main():
    try:
        number = int(input("Masukkan angka (tanggal tes hari ini): "))
        if number < 0:
            print("Angka harus positif.")
        else:
            result = calculate_product(number)
            print(f"Produk dari semua nilai dari 1 hingga {number} adalah: {result}")
    except ValueError:
        print("Masukan tidak valid. Harap masukkan angka.")

if __name__ == "__main__":
    main()
