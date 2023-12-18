import os

def input_text():
    return input("Masukkan Teks : ")

def input_pola():
    return input("Masukkan Pola Yang ingin Dicari: ")

def cari_pola(teks, pola):
    posisi = teks.find(pola)
    if posisi == -1:
        return "Pola tidak ditemukan dalam teks."
    else:
        return f"Pola ditemukan pada posisi {posisi + 1} sampai {posisi + len(pola)}."

def count_pola(teks, pola):
    count = teks.count(pola)
    return f"Jumlah pola yang ditemukan: {count}"

def main():
    teks = input_text()
    pola = input_pola()
    while True:
        print("\nPilihan:")
        print("1. Cari pola")
        print("2. Hitung pola")
        print("3. Keluar")
        pilihan = input("Masukkan pilihan (1/2/3): ")
        
        if pilihan == "1":
            os.system("cls")
            print(cari_pola(teks, pola))
            
        elif pilihan == "2":
            os.system("cls")
            print(count_pola(teks, pola))
            
        elif pilihan == "3":
            os.system("cls")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()