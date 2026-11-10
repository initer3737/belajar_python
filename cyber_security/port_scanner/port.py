import socket
import sys
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor

# Fungsi tunggal untuk memeriksa satu port
def scan_single_port(target_ip, port):
    try:
        # Membuat objek socket baru untuk setiap thread
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1.5) # Batas tunggu respon port (dalam detik)
        
        # connect_ex mengembalikan 0 jika port TERBUKA
        result = s.connect_ex((target_ip, port))
        
        if result == 0:
            print(f"[+] Port {port:<5} : TERBUKA")
            
        s.close()
    except Exception:
        pass # Abaikan error jika ada gangguan koneksi pada port tertentu

def main():
    print("=" * 50)
    print("      MULTI-THREADED PYTHON PORT SCANNER       ")
    print("=" * 50)
    
    # 1. Input Target
    target = input("Masukkan IP Target / Domain: ")
    try:
        target_ip = socket.gethostbyname(target)
    except socket.gaierror:
        print("\n[-] Error: Gagal menerjemahkan Hostname. IP tidak valid.")
        sys.exit()

    # 2. Input Range Port
    try:
        start_port = int(input("Masukkan Port Awal (contoh 1): "))
        end_port = int(input("Masukkan Port Akhir (contoh 1024): "))
    except ValueError:
        print("\n[-] Error: Input Port harus berupa angka.")
        sys.exit()

    # Tampilkan banner informasi awal
    print("-" * 50)
    print(f"Memindai Target : {target_ip} ({target})")
    print(f"Mencakup Port   : {start_port} sampai {end_port}")
    print(f"Waktu Mulai     : {str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))}")
    print("-" * 50)
    print("Scanning sedang berjalan...\n")
    
    waktu_mulai = datetime.now()

    # 3. Eksekusi Multi-threading dengan ThreadPoolExecutor
    # max_workers=100 artinya kita menjalankan maksimal 100 thread/pekerja sekaligus secara bersamaan
    try:
        with ThreadPoolExecutor(max_workers=100) as executor:
            # Membuat daftar port yang akan dipindai
            ports = range(start_port, end_port + 1)
            
            # Memetakan fungsi scan_single_port ke semua daftar port secara paralel
            executor.map(lambda p: scan_single_port(target_ip, p), ports)
            
    except KeyboardInterrupt:
        print("\n[-] Pemindaian dihentikan paksa oleh pengguna (Ctrl+C).")
        sys.exit()

    # 4. Hitung Total Waktu Durasi Scan
    waktu_selesai = datetime.now()
    total_waktu = waktu_selesai - waktu_mulai
    print("\n" + "-" * 50)
    print(f"Pemindaian Selesai dalam waktu: {total_waktu.total_seconds():.2f} detik")
    print("-" * 50)

if __name__ == "__main__":
    main()
