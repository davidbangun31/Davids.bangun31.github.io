def main():
    grades = []
    while True:
        grade = input("Masukkan nilai (-1 untuk berhenti): ")
        if grade == '-1':
            break
        grades.append(int(grade))

    if not grades:
        print("Tidak ada nilai yang dimasukkan.")
        return

    rata_rata = sum(grades) // len(grades)
    print("Rata-rata:", rata_rata)

    print("Nilai dalam urutan:")
    for nilai in grades:
        print(nilai)

if __name__ == "__main__":
    main()
