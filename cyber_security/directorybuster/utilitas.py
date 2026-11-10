# File: utilitas.py
import os

def muat_wordlist(nama_file):
    """Fungsi untuk membaca file wordlist dan mengembalikan daftar kata."""
    lokasi_folder = os.path.dirname(os.path.abspath(__file__))
    jalur_penuh = os.path.join(lokasi_folder, nama_file)
    
    daftar_kata = []
    try:
        with open(jalur_penuh, "r", encoding="utf-8") as f:
            for baris in f:
                kata = baris.strip()
                if kata: # Pastikan tidak memasukkan baris kosong
                    daftar_kata.append(kata)
        return daftar_kata
    except FileNotFoundError:
        print(f"[-] Error: File '{nama_file}' tidak ditemukan di {lokasi_folder}")
        return []

# KODE UJI COBA MANDIRI
if __name__ == "__main__":
    print("[UJI COBA] Menjalankan file utilitas.py secara langsung...")
    hasil = muat_wordlist("kamus.text")
    print(f"[UJI COBA] Berhasil membaca {len(hasil)} kata dari wordlist.")