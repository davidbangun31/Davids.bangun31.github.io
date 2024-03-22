def jumlah_angka():
    total = 0
    while True:
        try:
            angka = float(input("Masukkan angka (-1 untuk berhenti): "))
            if angka == -1:
                break
            total += angka
        except ValueError:
            print("Input tidak valid. Harap masukkan angka yang valid.")

    # Cetak jumlah dengan dua digit setelah koma
    print(f"Jumlah: {total:.2f}")

# Program utama
if __name__ == "__main__":
    jumlah_angka()
