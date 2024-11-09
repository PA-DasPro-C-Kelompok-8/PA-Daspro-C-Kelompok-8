# PA-Daspro-C-Kelompok-8
# aplikasi penyewaan peralatan mendaki gunung
## Anggota
### Nama : Danial Hirzan Akbary
### NIM : 2409116098
### Nama : Muhammad Fawwaz Ibnu Rasya
### NIM : 2409116091
### Nama : Yulius Pune'
### NIM : 2409116110

# flowchart

![image](https://github.com/user-attachments/assets/c2abc302-cdac-4ddc-95d3-d9370e95d493)

![image](https://github.com/user-attachments/assets/2513d3a4-3a49-41a4-b3da-a0a6db3c38e0)

![image](https://github.com/user-attachments/assets/990ff083-867a-4125-b2a2-57e6350a4f6c)

# Deskripsi program

program ini merupakan program penyewaan peralatan mendaki gunung yang dimana terdapat 2 role yakni user dan admin. yang dimana admin dapat melakukan crud dan fungsi fungsi lainya yang biasa dilakukan admin dan user dapat melakukan transaksi serta mengisi saldo dan sorting.

# Library

Prettytable
Digunakan untuk menampilkan data peralatan secara rapi dalam bentuk table di konsol.

Os
Library yang memungkinkan penghapusan layer konsol untuk menjaga tampilan tetap bersih setelah setiap operasi.

Pwinput
Library yang digunakan untuk input kata sandi yang tersembunyi,memberikan keamanan tambahan untuk akun admin dan penyewa.

Time
Digunakan untuk menampikan dan mencatat waktu transaksi.

Json
Digunakan untuk menyimpan dan membaca data dalam format JSON, termasuk informasi akun pengguna, daftar peralatan, dan transaksi penyewaan.

# fitu-fitur

## fitur admin

1. Tambah Barang             
2. Lihat Daftar Barang       
3. Update barang             
4. Hapus Barang              
5. Cari barang               
6. Lihat daftar penyewaan    
7. Mengembalikan barang      
8. Keluar

## fitur user

1. Lihat Daftar Barang       
2. Sewa barang               
3. Lihat barang yang disewa  
4. Isi saldo                 
5. Lihat saldo               
6. Sorting Harga            
7. Keluar

# OUTPUT

## Hal pertama muncul

![image](https://github.com/user-attachments/assets/8956b8a0-36f6-47c8-b356-524bdc482eb6)

merupakan penjelasan awal tentang toko kami

## menu mulai

![image](https://github.com/user-attachments/assets/d41e917a-4636-4f47-a8b5-c46d761f57e3)

merupakan menu yang pertama kali muncul saat program dirun yang dimana terdapat sebuah pilihan jika memilih 1 melakukan registrasi dan jika memilih 2 melakukan login

## Registrasi

![image](https://github.com/user-attachments/assets/1a590c18-68be-45c0-a83d-03f599a05ab2)

pertana-tama melakukan input username dan password lalu kemudian menampilkan bahwa registrasi terlah berhasil yang dimana akan langsung berlanjut ke menu login

## Menu login

![image](https://github.com/user-attachments/assets/2c1c3a7d-5cc4-42b4-b041-ac917633f04a)

pada fungsi ini terdapat 2 pilihan login yang dimana pilihan bertama login sebgai admin dan pilihan ke dua login sebagai user

### Login Admin

![image](https://github.com/user-attachments/assets/dddf5337-eb0f-4e4c-bd6e-3dc44c3d2e69)

pada menu ini anda akan disuruh melakukan input username dan password dan kemudian akan dicek role yang dimiliki pada akun tersebut jika terpenuhi makan login berhasil dan akan beralih menu admin

### Login user

