from datetime import datetime, timedelta

def cetak_tanggal_mendatang(jumlah_hari):
    # Dapatkan tanggal hari ini
    tanggal_sekarang = datetime.now()

    # Hitung tanggal di masa depan
    tanggal_mendatang = tanggal_sekarang + timedelta(days=jumlah_hari)

    # Format string tanggal
    tanggal_terformat = tanggal_mendatang.strftime("%A, %d %B %Y")

    # Cetak tanggal yang diformat
    print(tanggal_terformat)

# Program utama
if __name__ == "__main__":
    try:
        hari = int(input("Masukkan jumlah hari dari sekarang: "))
        cetak_tanggal_mendatang(hari)
    except ValueError:
        print("Harap masukkan jumlah hari yang valid.")
