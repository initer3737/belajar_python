# File: dir_buster.py
import urllib.request
import urllib.error
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime

# Mengimpor fungsi dari file utilitas.py yang kita buat sebelumnya
from utilitas import muat_wordlist

def cek_direktori(url_target, direktori):
    """Memeriksa apakah sebuah direktori ada di web target"""
    # Pastikan format URL benar (contoh: http://target.com)
    if not url_target.endswith("/"):
        url_target += "/"
        
    url_penuh = f"{url_target}{direktori}"
    
    try:
        # Meniru User-Agent browser agar tidak diblokir instan oleh web server
        req = urllib.request.Request(
            url_penuh, 
            headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
        )
        
        # Lakukan request ke URL tersebut
        with urllib.request.urlopen(req, timeout=2.0) as respon:
            status = respon.getcode()
            if status == 200:
                print(f"[+] [200 OK] Ditemukan: {url_penuh}")
                
    except urllib.error.HTTPError as e:
        # Kode 403 artinya folder ada tapi dilarang diakses (Forbidden)
        if e.code == 403:
            print(f"[!] [403 Forbidden] Ada tapi dikunci: {url_penuh}")
        # Kode 404 artinya folder benar-benar TIDAK ADA (kita abaikan saja)
        elif e.code == 404:
            pass
    except Exception:
        pass # Abaikan error jaringan lainnya seperti timeout atau salah ketik domain

def main():
    print("=" * 50)
    print("         MULTI-THREADED WEB DIR BUSTER         ")
    print("=" * 50)
    
    # 1. Input target dari user
    target = input("Masukkan URL Target (contoh: http://example.com): ")
    if not target.startswith("http://") and not target.startswith("https://"):
        target = "http://" + target

    # 2. Muat kata kunci menggunakan modul utilitas kita
    wordlist = muat_wordlist("kamus.text")
    if not wordlist:
        print("[-] Pemindaian dibatalkan karena wordlist kosong.")
        return

    print("-" * 50)
    print(f"Target URL   : {target}")
    print(f"Total Kata   : {len(wordlist)} kata kunci")
    print(f"Waktu Mulai  : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 50)
    print("Memulai pemindaian...\n")

    waktu_mulai = datetime.now()

    # 3. Jalankan Multi-threading dengan 20 pekerja sekaligus
    with ThreadPoolExecutor(max_workers=20) as executor:
        # Memetakan fungsi pengecekan ke setiap kata di dalam wordlist
        executor.map(lambda d: cek_direktori(target, d), wordlist)

    total_waktu = datetime.now() - waktu_mulai
    print("-" * 50)
    print(f"Selesai dalam: {total_waktu.total_seconds():.2f} detik")
    print("-" * 50)

if __name__ == "__main__":
    main()
