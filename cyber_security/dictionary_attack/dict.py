import os
import time
lokasi_folder = os.path.dirname(os.path.abspath(__file__))
lokasi_file = os.path.join(lokasi_folder, "passw.text")
username="admin"
passwordlogin="admin1922"
waktu_mulai=time.time()

with open(lokasi_file,'r') as dicts:
    for password in dicts:
        if password ==passwordlogin:
            print("password has been crack ",password)

waktu_berakhir=time.time() 
total=waktu_berakhir-waktu_mulai
print(f"total waktu {total:.4f}")