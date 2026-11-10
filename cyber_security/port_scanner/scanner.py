import socket
import sys
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor

# ? port tunggal untuk scan 1 port
def scan_single_port(target_ip,port):
    try :
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.settimeout(1.5)
        result=s.connect_ex((target_ip,port))
        if result == 0 :
            print(f"[+] port {port:<5} : terbuka")
        s.close()    
    except Exception:
        pass 

def main():
    print("="*50)
    print(" mult threaded python port scanner")      
    print("="*50)      
    target=input("masukkan ip target/domain: ")
    try:
        target_ip=socket.gethostbyname(target)
    except socket.gaierror:
        print("gagal menerjemahkan hostname ip tidak valid")
        sys.exit()
    try:
        start_port=int(input("masukkan port awal (contoh 1)"))
        end_port=int(input("masukkan port akhir (contoh 1024)"))
    except ValueError:
        print("\n[-] error:input port harus berupa angka")
        sys.exit()        
    print("-"*50)    
    print(f"memindai target : {target_ip} ({target})")
    print(f"mencakup port: {start_port} sampai port {end_port}")
    print(f"waktu mulai : {str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))}")
    print("-"*50)    
    print("scanning sedang berjalan...\n")

    waktu_mulai=datetime.now()    

    try:
        with ThreadPoolExecutor(max_workers=100) as excecutor:
          ports=range(start_port,end_port+1)
          excecutor.map(lambda p:scan_single_port(target_ip=target_ip,port=p),ports)  
    except KeyboardInterrupt:
        print("\n[-] pemindaian dihentikan paksa oleh pengguna")
        sys.exit()
    waktu_selesai=datetime.now()
    total_waktu=waktu_selesai-waktu_mulai
    print("\n"+'-'*50)    
    print(f"pemindaian selesai dalam waktu: {total_waktu.total_seconds():.2f} detik")    
    print("\n"+'-'*50)    

if __name__ == "__main__":
    main()