


import os
from colorama import Fore, Style  # Import modul colorama

# Instal modul colorama jika belum diinstal
try:
    from colorama import init
    init(autoreset=True)
except ImportError:
    print("Instalasi colorama dibutuhkan. Jalankan perintah: pip install colorama")
    exit()

os.system("ls")
p = input("Nama : ")                                                                                                                                   
c = int(input("Awal Chapter : "))
b = int(input("End Chapter : "))
a = c
while a <= b:
    os.system(f"mkdir {a}")
    os.system(f"mv {p}-{a}.zip {a} && cd {a} && unzip {p}-{a}.zip && rm {p}-{a}.zip && cd ..")
    if a < 10:
        os.system(f"mv {p}-0{a}.zip {a} && cd {a} && unzip {p}-0{a}.zip && rm {p}-0{a}.zip && cd ..")
    a += 1

# ... Kode sebelumnya

# Setelah selesai menjalankan while a <= b, tambahkan pengkondisian baru untuk melihat jumlah file dalam rentang folder dari a hingga b
a = c
while a <= b:
    folder_path = str(a)
    file_count = len([f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))])
    
    if file_count == 0:
        print(f"{Fore.RED}Folder {folder_path} kosong.{Style.RESET_ALL}")
    else:
        print(f"Jumlah file di dalam folder {folder_path}: {file_count}")
    
    a += 1
