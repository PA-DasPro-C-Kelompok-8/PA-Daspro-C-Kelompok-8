from prettytable import PrettyTable
import json
import pwinput
from datetime import datetime,timedelta
import os

print("=======================================SELAMAT DATANG DI CONSINA==============================================")
print(":  Toko kami menyediakan perlengkapan hiking terbaik bagi para pecinta petualangan alam. Kami menghadirkan   :")
print(":   berbagai macam produk berkualitas tinggi mulai dari tas hiking, tenda, matras, jaket tahan air, hingga   :")
print(":     hingga aksesori outdoor lainnya. Semua barang dipilih secara teliti untuk memastikan kenyamanan dan    :")
print(":      keamanan selama di alam bebas. Temukan peralatan hiking impian Anda di sini dan siapkan diri untuk    :")
print(":                                           penjelajahan berikutnya!                                         :")
print("==============================================================================================================")
os.system ("cls")
json_path = "C:\\PA DDP\\PA\\user.json"
def load():
    with open(json_path, "r") as jsonuser:
        data = json.load(jsonuser)
    return data

def save(data):
    with open(json_path, "w") as jsonuser:
        json.dump(data, jsonuser, indent=4)

json_sewa = "C:\\PA DDP\\PA\\barang_sewa.json"
def sewa_load():
    with open(json_sewa, "r") as jsonsewa:
        data = json.load(jsonsewa)
    return data

def sewa_save(data_sewa):
    with open(json_sewa, "w") as jsonsewa:
        json.dump(data_sewa, jsonsewa, indent=4)

json_barang = "C:\\PA DDP\\PA\\barang.json"
def barang_load():
    with open(json_barang, "r") as jsonbarang:
        data_barang = json.load(jsonbarang)
        return data_barang

def barang_save(data_barang):
    with open(json_barang, "w") as file:
        json.dump(data_barang,file, indent=4)

def register():
    while True:
        try:
            p_register = load()
            print("====================================")
            print(":             silahkan             :")
            print(":             melakukan            :")
            print(":             registrasi           :")
            print("====================================")
            name = str(input("Masukan nama anda : "))
            if not name.isalnum() or len(name) > 12:
                print("====================================")
                print(":Nama hanya boleh menggunakan huruf: ")
                print(":    dan tidak boleh lebih dari    : ")
                print(":           12 karakter            : ")
                print("====================================")
                continue
            elif any(user["Nama"] == name for user in p_register):
                print("====================================")
                print(":    Nama yang anda input telah    :")
                print(":            digunakan             :")
                print("====================================")
                continue
            password = pwinput.pwinput("Masukan password anda : ")
            akun = {
                "Nama": name,
                "Password": password,
                "Saldo": 0,
                "Role": "user"
            }
            p_register.append(akun)
            save(p_register)
            print("====================================")
            print(":        Registrasi berhasil       :")
            print("====================================")
            menu_login()
        except (ValueError, KeyboardInterrupt):
            print("====================================")
            print(":   Input tidak valid, dan mohon   :")
            print(":      Jangan tekan ctrl + c       :")
            print("====================================")

def menu_login():
    while True:
        try:
            print("====================================")
            print(":             Menu Login           :")
            print(":           1) Login Admin         :")
            print(":           2) Login User          :")
            print("====================================")
            load_login = load()
            pilihan = int(input("masukan pilihan anda : "))
            if pilihan == 1:
                print("====================================")
                print(":    Anda memilih pilihan NO 1     :")
                print("====================================")
                admin_login()
            elif pilihan == 2:
                print("====================================")
                print(":    Anda memilih pilihan NO 2     :")
                print("====================================")
                user_login()
        except (ValueError, KeyboardInterrupt):
            print("====================================")
            print(":   Input tidak valid, dan mohon   :")
            print(":      Jangan tekan ctrl + c       :")
            print("====================================")

def mulai():
    try:
        while True:
            print("====================================")
            print(":       Sudah memiliki akun?       :")
            print("====================================")
            print(":  Silahkan melakukan registrasi   :")
            print(":   jika belum dengan ketik (1)    :")                                
            print("====================================")
            print(":  jika sudah langsung saja login  :")
            print(":         degan ketik (2)          :")
            print("====================================")
            pilihan = int(input("masukan pilihan anda"))
            if pilihan == 1 :
                print("====================================")
                print(":    Anda memilih pilihan NO 1     :")
                print("====================================")
                register()
                break
            elif pilihan == 2:
                print("====================================")
                print(":    Anda memilih pilihan NO 2     :")
                print("====================================")
                menu_login()
                break
            else:
                print("====================================")
                print(":    Pilihan anda tidak valid      :")
                print(":   Silahkan masukan angka 1/2     :")
                print("====================================")
    except (ValueError, KeyboardInterrupt):
        print("====================================")
        print(":   Input tidak valid, dan mohon   :")
        print(":      Jangan tekan ctrl + c       :")
        print("====================================")

def admin_login():
    try:
        while True:
            load_login = load()
            username = input("masukan nama akun anda : ")
            password = pwinput.pwinput("masukan password akun anda : ")
            for user in load_login:
                if user["Nama"] == username:
                    if user["Role"] == "admin":
                        if user["Password"] == password:
                            print("====================================")
                            print(":  Login berhasil selamat datang   :")
                            print(":          ",{username},"          :")
                            print("====================================")
                            admin_main()
                            break
                        elif user["Password"] != password:
                            print("====================================")
                            print(":       Password anda salah        :")
                            print("====================================")
                            admin_login()
                            break
                    elif user["Role"] != "admin":
                        print("====================================")
                        print(":      Maaf anda bukan admin       :")
                        print("====================================")
                        admin_login()
                        break
                elif user["Nama"] != username: 
                    print("====================================")
                    print(":        Username anda salah        :")
                    print("====================================")
                    admin_login()
                    break
            else:
                print("=====================================")
                print(": Terjadi kesalahan input coba lagi :")
                print("=====================================")
    except (ValueError, KeyboardInterrupt):
        print("====================================")
        print(":   Input tidak valid, dan mohon   :")
        print(":      Jangan tekan ctrl + c       :")
        print("====================================")

def user_login():
    try:
        while True:
            load_login = load()  # Memuat data pengguna dari JSON
            username = input("Masukkan nama akun anda: ")
            password = pwinput.pwinput("Masukkan password akun anda: ")
            login_success = False
            for user in load_login:
                if user["Nama"] == username:
                    if user["Role"] == "user":
                        if user["Password"] == password:
                            print("====================================")
                            print(":  Login berhasil, selamat datang  :")
                            print(":          {username}             :")
                            print("====================================")
                            user_main()
                            login_success = True
                            break  # Keluar dari loop `for` jika login berhasil
                        else:
                            print("====================================")
                            print(":       Password anda salah        :")
                            print("====================================")
                    else:
                        print("====================================")
                        print(":  Maaf, anda tidak memiliki akses  :")
                        print("====================================")
                    break  # Keluar dari loop `for` jika username ditemukan
            if login_success:
                return  # Keluar dari fungsi `user_login` jika login berhasil
            else:
                print("=====================================")
                print(":   Username atau password salah    :")
                print("=====================================")
    except (ValueError, KeyboardInterrupt):
        print("====================================")
        print(":   Input tidak valid, dan mohon   :")
        print(":      Jangan tekan ctrl + c       :")
        print("====================================")



def user_main():
    try:
        while True:
            print("=======================================")
            print(":             Menu User               :")
            print("=======================================")
            print(":        1. Lihat Daftar Barang       :")
            print(":        2. Sewa barang               :")
            print(":        3. Lihat barang yang disewa  :")
            print(":        4. Isi saldo                 :")
            print(":        5. Lihat saldo               :")
            print(":        6. Sorting Harga             :")
            print(":        7. Keluar                    :")
            print("=======================================")
            pilih = int (input("masukan pilihan anda = "))
            if pilih == 1:
                lihat_daftar()
            elif pilih == 2:
                sewa()
                break
            elif pilih == 3:
                daftar_sewa_user()
                break
            elif pilih == 4:
                isi_saldo()
                break
            elif pilih == 5:
                lihat_saldo()
                break
            elif pilih == 6:
                tampilkan_barang_berdasarkan_harga()
                break
            elif pilih == 7:
                print("====================================")
                print(":  Anda memilih keluar menu admin  :")
                print(":      silahkan login ulang        :")
                print("====================================")
                menu_login()
                break
            else:
                print("====================================")
                print(":    Pilihan anda tidak valid      :")
                print("====================================")
                continue
    except (ValueError, KeyboardInterrupt):
        print("====================================")
        print(":   Input tidak valid, dan mohon   :")
        print(":      Jangan tekan ctrl + c       :")
        print("====================================")

def admin_main():
    try:
        while True:
            print("=======================================")
            print(":             Menu Admin              :")
            print("=======================================")
            print(":        1. Tambah Barang             :")
            print(":        2. Lihat Daftar Barang       :")
            print(":        3. Update barang             :")
            print(":        4. Hapus Barang              :")
            print(":        5. Cari barang               :")
            print(":        6. Lihat daftar penyewaan    :")
            print(":        7. Mengembalikan barang      :")
            print(":        8. Keluar                    :")
            print("=======================================")
            pilihan = int(input("Plih menu: "))
            if pilihan == 1:
                tambah_barang()
                break
            elif pilihan == 2:
                lihat_daftar()
            elif pilihan == 3:
                update()
                break
            elif pilihan == 4:
                hapus_item()
                break
            elif pilihan == 5:
                search()
                break
            elif pilihan == 6:
                daftar_sewa()
                break
            elif pilihan == 7:
                kembalikan_barang()
                break
            elif pilihan == 8:
                print("====================================")
                print(":  Anda memilih keluar menu admin  :")
                print(":      silahkan login ulang        :")
                print("====================================")
                menu_login()
                break
            else:
                print("====================================")
                print(":    Pilihan anda tidak valid      :")
                print("====================================")
    except (ValueError, KeyboardInterrupt):
        print("====================================")
        print(":   Input tidak valid, dan mohon   :")
        print(":      Jangan tekan ctrl + c       :")
        print("====================================")

def lihat_daftar():
    data_barang = barang_load()
    table = PrettyTable()
    table.field_names = ["ID", "Nama Produk", "Harga per Hari", "Stok","status"]
    for barang in data_barang['produk']:
        table.add_row([barang["ID"], barang["Nama barang"], barang["Harga"], barang["Stok"],barang["status"]])
    print(table)

def tambah_barang():
    load = barang_load()
    lihat_daftar()
    while True:
        try:
            id_barang = input("masukan ID barang : ")
            nama_barang = str(input("masukan nama barang : "))
            harga = int(input("masukan harga barang : "))
            stok_barang = int(input("masukan stok yang dimiliki : "))
            if any(barang["Nama barang"].lower() == nama_barang.lower() for barang in load["produk"]):
                print("====================================")
                print(":   Nama barang sudah ada didalam  :")
                print(":           Daftar barang          :")
                print("====================================")
                continue
            elif harga < 5000:
                print("====================================")
                print(":  Harga barang harus lebih dari   :")
                print(":             5000                 :")
                print("====================================")
                continue
            elif not(id_barang.isdigit()):
                print("====================================")
                print(":    Pastikan anda mengisi ID      :")
                print(":    Dengan menggunakan angka      :")
                print("====================================")
                continue
            elif any(barang["ID"] == id_barang for barang in load["produk"]):
                print("====================================")
                print(":       ID telah digunakan         :")
                print("====================================")
                continue
            new_barang ={
                "ID" : int(id_barang),
                "Nama barang" : nama_barang,
                "Harga" : harga,
                "Stok" : stok_barang,
                "status" : "tersedia"
            }
            load["produk"].append(new_barang)
            barang_save(load)
            print("====================================")
            print(":   Penambahan barang berhasil     :")
            print("====================================")
            admin_main()
            break
        except (ValueError, KeyboardInterrupt):
            print("====================================")
            print(":   Input tidak valid, dan mohon   :")
            print(":      Jangan tekan ctrl + c       :")
            print("====================================")


def hapus_item():
    load = barang_load()
    lihat_daftar()
    try :
        while True:
            id_barang = int(input("masukan nama barang = "))
            for barang in load["produk"]:
                if barang["ID"] == id_barang :
                    hapus_barang = barang
                    if hapus_barang :
                        load["produk"].remove(hapus_barang)
                        barang_save(load)
                        print("=====================================")
                        print(":     Barang berhasil dihapus       :")
                        print("=====================================")
                        admin_main()
                        return
                    else:
                        print("====================================")
                        print(":       ID tidak ditemukan         :")
                        print("====================================")
    except (ValueError, KeyboardInterrupt):
        print("====================================")
        print(":   Input tidak valid, dan mohon   :")
        print(":      Jangan tekan ctrl + c       :")
        print("====================================")


def aturan():
    print("===============ATURAN PENYEWAAN=================")
    print(":-Usia minimal untuk penyewaan adalah 18 tahun :")
    print(":-durasi penyewaan minimal 1 hari dan maksimal :")
    print(": 14 hari                                      :")
    print(":-Penyewa wajib mengembalikan barang sesuai    :")
    print(": dengan tanggal yang telah disepakati.        :")
    print(":-Keterlambatan pengembalian akan dikenakan    :")
    print(": biaya tambahan per hari.                     :")
    print(":-Uang jaminan (deposit) wajib dibayarkan dan  :")
    print(": akan dikembalikan setelah barang diperiksa.  :")
    print(":-Pembatalan penyewaan harus dilakukan minimal :")
    print(": 24 jam sebelum waktu pengambilan.            :")
    print(":-Jika pembatalan dilakukan kurang dari 24 jam :")
    print(": uang muka tidak akan dikembalikan.           :")
    print("================================================")

def kembalikan_barang():
    load_sewa = sewa_load()
    load_barang = barang_load()
    nama_penyewa = input("Masukkan nama penyewa: ")
    barang_dikembalikan = input("Masukkan nama barang yang dikembalikan: ")
    
    # Menemukan sewa yang cocok berdasarkan nama penyewa dan barang
    for sewa_item in load_sewa['sewa']:
        if sewa_item['Nama'] == nama_penyewa and sewa_item['Nama barang'] == barang_dikembalikan:
            # Mengonfirmasi jika barang ditemukan
            print(f"Barang ditemukan: {sewa_item['Nama barang']}")
            # Mengurangi jumlah barang yang disewa
            for produk_item in load_barang['produk']:
                if produk_item['Nama barang'] == barang_dikembalikan:
                    produk_item['Stok'] += sewa_item['Jumlah']  # Mengembalikan stok
                    sewa_item['Jumlah'] = 0  # Barang sudah dikembalikan
                    print(f"Barang {barang_dikembalikan} berhasil dikembalikan. Stok sekarang: {produk_item['Stok']}")
                    # Simpan data yang telah diperbarui
                    sewa_save(load_sewa)
                    barang_save(load_barang)
                    return  # Mengakhiri fungsi setelah pengembalian sukses

    # Jika sewa tidak ditemukan
    print("Data sewa tidak ditemukan untuk nama dan barang yang diberikan.")

def search():
    while True:
        load = barang_load()
        hasil_pencarian = []
        try:
            cari_barang = str(input("masukan nama barang yang ingin di cari : "))
            for barang in load["produk"]:
                if barang["Nama barang"].lower() == cari_barang.lower():
                    table = PrettyTable()
                    table.field_names = ["ID", "Nama Barang", "Harga per Hari", "Status","stock"]
                    table.add_row([barang["ID"],barang["Nama barang"],barang["Harga"],barang["status"],barang["Stok"]])
                    print(table)
                    admin_main()
                    break
                else:
                    print("====================================")
                    print(":     Barang tidak ditemukan       :")
                    print("====================================")
            return hasil_pencarian
        except (ValueError, KeyboardInterrupt):
            print("====================================")
            print(":   Input tidak valid, dan mohon   :")
            print(":      Jangan tekan ctrl + c       :")
            print("====================================")


def daftar_sewa():
    user_rentals = sewa_load()
    table = PrettyTable()
    table.field_names = ["Nama User", "ID Barang", "Nama Barang", "Harga per Hari", "Lama Sewa (Hari)", "Tanggal Sewa", "Tanggal Kembali"]
    if user_rentals["sewa"]:
        for rental in user_rentals["sewa"]:
            table.add_row([rental['Nama'], rental['ID'], rental['Nama barang'], rental['Harga'], rental['Lama'], rental['Tgl_sewa'], rental['Tgl_kembali']])
        print("\nDaftar Semua Barang yang Disewa:")
        print(table)
        admin_main()
    else:
        print("Tidak ada barang yang disewa oleh pengguna.")
    admin_main()

def update():
    print("====================================")
    print(":           Menu Update            :")
    print("====================================")
    lihat_daftar()
    try:
        load = barang_load()  # Memuat data barang
        while True:
            barang_id = int(input("Masukkan ID barang yang ingin diupdate : "))
            found = False
            for barang in load["produk"]:
                if barang["ID"] == barang_id:
                    found = True
                    print(f"Barang ditemukan: {barang['Nama barang']}")
                    new_name = input("Masukkan nama barang yang baru : ").strip()
                    new_harga = input("Masukkan harga barang yang baru : ").strip()
                    new_stock = input("Masukkan stok barang yang baru : ").strip()
                    if not (2 <= len(new_name) <= 50):
                        print("======================================")
                        print(": Minimal karakter 2 dan maksimal 50 :")
                        print("======================================")
                        continue
                    elif not (new_name.strip() and new_harga.isdigit() and new_stock.isdigit()):
                        print("========================================")
                        print(": Data tidak valid, pastikan inputan   :")
                        print(":            Sudah sesuai              :")
                        print("========================================")
                        continue
                    elif not (10000000 >= int(new_harga) >= 100):
                        print("========================================")
                        print(":  Minimal harga RP 1000 dan maksimal  :")
                        print(":            RP 10000000               :")
                        print("========================================")
                        continue
                    elif not (100 >= int(new_stock) > 0):
                        print("========================================")
                        print(":   Minimal stock 1 dan maksimal 100   :")
                        print("========================================")
                        continue
                    
                    # Memeriksa apakah nama produk baru sudah ada di daftar
                    if any(barang["Nama barang"].lower() == new_name.lower() for barang in load["produk"]):
                        print("========================================")
                        print(":       Produk sudah ada               :")
                        print("========================================")
                        continue
                    
                    # Update informasi barang
                    barang["Nama barang"] = new_name
                    barang["Harga"] = int(new_harga)
                    barang["Stok"] = int(new_stock)
                    
                    # Simpan perubahan
                    barang_save(load)
                    print("========================================")
                    print(":       Produk berhasil diupdate       :")
                    print("========================================")
                    admin_main()
                    return 
            if not found:
                print("========================================")
                print(":         ID tidak ditemukan           :")
                print("========================================")
    except (ValueError, KeyboardInterrupt):
        print("====================================")
        print(":   Input tidak valid, dan mohon   :")
        print(":      Jangan tekan ctrl + c       :")
        print("====================================")

def daftar_sewa_user():
    load = sewa_load()
    nama = input("Masukkan nama pengguna: ")
    user_rentals = [rental for rental in load['sewa'] if rental['Nama'].lower() == nama.lower()]
    
    if not user_rentals:
        print(f"Tidak ada barang yang disewa oleh {nama}.")
        return
    
    # Membuat tabel untuk menampilkan data
    table = PrettyTable()
    table.field_names = ["ID", "Nama Barang", "Harga per Hari", "Jumlah", "Jumlah Hari Sewa", "Tanggal Sewa", "Tanggal Pengembalian"]
    
    for rental in user_rentals:
        table.add_row([rental['ID'], rental['Nama barang'], rental['Harga'], rental['Jumlah'], rental['Lama'], rental['Tgl_sewa'], rental['Tgl_kembali']])
    
    print(f"\nDaftar Barang yang Disewa oleh {nama}:")
    print(table)
    user_main()

def update_user_saldo(user_name, amount):
    users = load()  # Harus langsung menjadi list pengguna tanpa key 'users'
    for user in users:
        if user['Nama'].lower() == user_name.lower():
            if user['Saldo'] >= amount:
                user['Saldo'] -= amount
                save(users)  # Pastikan `save()` menyimpan data pengguna yang diperbarui
                return user['Saldo']
            else:
                print("Saldo Anda tidak mencukupi untuk transaksi ini.")
                return None
    print("Pengguna tidak ditemukan.")
    return None

def sewa():
    produk_data = barang_load()  # Ambil data barang
    rental_load = sewa_load()
    users = load()  # Data pengguna langsung dalam bentuk list
    
    user_name = input("Masukkan nama Anda: ")
    
    # Cari data pengguna
    user = next((u for u in users if u['Nama'].lower() == user_name.lower()), None)
    if not user:
        print("Pengguna tidak ditemukan.")
        return
    
    while True:
        try:
            # Menampilkan daftar barang dan aturan
            lihat_daftar()
            id_barang = int(input("Masukkan ID barang yang ingin disewa: "))
            lama_hari = int(input("Masukkan jumlah hari sewa: "))
            jumlah_barang = int(input("Masukkan jumlah barang: "))
            
            for produk in produk_data["produk"]:
                if produk["ID"] == id_barang:
                    if produk["Stok"] >= jumlah_barang:
                        total_harga = produk["Harga"] * jumlah_barang * lama_hari
                        # Periksa saldo pengguna sebelum melakukan transaksi
                        sisa_saldo = update_user_saldo(user_name, total_harga)
                        if sisa_saldo is None:
                            return  # Batalkan transaksi jika saldo tidak cukup
                        
                        # Update stok produk
                        produk["Stok"] -= jumlah_barang
                        # Hitung tanggal kembali
                        tanggal_sekarang = datetime.now()
                        kembali = tanggal_sekarang + timedelta(days=lama_hari)
                        
                        # Tambahkan transaksi ke data sewa
                        sewa_data = {
                            "Nama": user_name,
                            "ID": produk["ID"],
                            "Nama barang": produk["Nama barang"],
                            "Harga": produk["Harga"],
                            "Jumlah": jumlah_barang,
                            "Lama": lama_hari,
                            "Tgl_sewa": tanggal_sekarang.strftime('%Y-%m-%d'),
                            "Tgl_kembali": kembali.strftime('%Y-%m-%d'),
                            "Jumlah harga": total_harga
                        }
                        rental_load['sewa'].append(sewa_data)
                        # Simpan perubahan ke file JSON
                        sewa_save(rental_load)
                        barang_save(produk_data)
                        
                        # Tampilkan struk
                        print("===================================================================")
                        print(":                        Struk Belanja                            :")
                        print("===================================================================")
                        print(f": Nama Barang      : {produk['Nama barang']}")
                        print(f": Jumlah Barang    : {jumlah_barang}")
                        print(f": Lama Sewa (hari) : {lama_hari}")
                        print(f": Tanggal Sewa     : {tanggal_sekarang.strftime('%Y-%m-%d')}")
                        print(f": Tanggal Kembali  : {kembali.strftime('%Y-%m-%d')}")
                        print(f": Jumlah Harga     : Rp{total_harga}")
                        print("===================================================================")
                        print(f"Saldo Tersisa Anda: Rp{sisa_saldo}")
                        print("===================================================================")
                        user_main()
                        return
                    else:
                        print("Stok barang tidak mencukupi.")
                        return
            print("ID barang tidak ditemukan.")
        except (ValueError, KeyboardInterrupt):
            print("====================================")
            print(":   Input tidak valid, dan mohon   :")
            print(":      Jangan tekan ctrl + c       :")
            print("====================================")

def isi_saldo():
    users = load()  # Pastikan load mengembalikan data dengan format yang benar
    # Meminta nama pengguna dan jumlah saldo yang akan ditambahkan
    user_name = input("Masukkan nama pengguna: ")
    try:
        saldo_tambahan = int(input("Masukkan jumlah saldo yang ingin ditambahkan: "))
        if saldo_tambahan <= 0 or saldo_tambahan >= 10000000:
            print("=====================================")
            print(": Jumlah saldo harus lebih dari nol :")
            print(":      dan kurang dari 10 juta      :")
            print("=====================================")
            return
    except (ValueError, KeyboardInterrupt):
        print("====================================")
        print(":   Input tidak valid, dan mohon   :")
        print(":      Jangan tekan ctrl + c       :")
        print("====================================")
        return

    # Jika data berbentuk list, gunakan 'users' langsung, tanpa ['users']
    user = next((u for u in users if u['Nama'].lower() == user_name.lower()), None)

    # Memeriksa apakah pengguna ditemukan
    if user:
        # Menambahkan saldo ke akun pengguna
        user['Saldo'] += saldo_tambahan
        save(users)  # Simpan data yang diperbarui ke file JSON

        print(f"Saldo berhasil ditambahkan. Saldo baru untuk {user['Nama']}: Rp{user['Saldo']}")
        user_main()
    else:
        print("Pengguna tidak ditemukan.")

def lihat_saldo():
    try:
        users_data = load()  # Memuat data pengguna dari file JSON
        user_name = input("Masukkan nama pengguna: ")  # Input nama pengguna
        
        for user in users_data:
            if user['Nama'].lower() == user_name.lower():  # Menemukan pengguna berdasarkan nama
                print(f"Saldo untuk {user['Nama']}: Rp{user['Saldo']}")
                user_main()  # Kembali ke menu utama setelah menampilkan saldo
                return  # Menyelesaikan fungsi setelah menampilkan saldo
        
        print("Pengguna tidak ditemukan.")  # Jika pengguna tidak ditemukan
    except (ValueError, KeyboardInterrupt):
        print("====================================")
        print(":   Input tidak valid, dan mohon   :")
        print(":      Jangan tekan ctrl + c       :")
        print("====================================")

def tampilkan_barang_berdasarkan_harga():
    inventory =  barang_load()
    
    # Mengurutkan produk berdasarkan harga
    sorted_products = sorted(inventory['produk'], key=lambda x: x['Harga'])
    
    # Menampilkan hasil dalam tabel
    table = PrettyTable()
    table.field_names = ["ID", "Nama Barang", "Harga", "Stok"]
    
    for product in sorted_products:
        table.add_row([product['ID'], product['Nama barang'], product['Harga'], product['Stok']])
    
    print(table)
    user_main()



mulai()