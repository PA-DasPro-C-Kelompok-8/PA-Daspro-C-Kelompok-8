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

![image](https://github.com/user-attachments/assets/31e94486-61df-4ab1-838f-da03cfceaee8)

pada menu ini anda akan disuruh melakukan input username dan password dan kemudian akan dicek role yang dimiliki pada akun tersebut jika terpenuhi makan login berhasil dan akan beralih menu user

# Menu admin

![image](https://github.com/user-attachments/assets/90e7210a-adbb-4119-8127-fe5d29c997f2)

pada menu ini terdapat 8 pilihan yang dimana penjelasan nya sebagai berikut

## Pilihan Tambah barang

![image](https://github.com/user-attachments/assets/a6ad47d9-98f9-425f-8e2b-9c0dda0e2069)

pertama akan menampilkan seluruh daftar yang ada

![image](https://github.com/user-attachments/assets/0fed9974-e274-4020-8649-e73547dea760)

kemudian akan input ID, Nama, Harga , dan stok

![image](https://github.com/user-attachments/assets/342976eb-f207-46a8-9d12-e2d046acf0f7)

ketika semua syarat terpenuhi maka akan menampilkan keterangan seperti diatas

## Pilihan menu lihat daftar barang 

![image](https://github.com/user-attachments/assets/eb91645e-a398-488f-a1e9-fddee94bf179)

Fungsi ini akan menampilkan semua barang yang dimiliki

## Pilihan menu Update barang

![image](https://github.com/user-attachments/assets/5290e83f-6f07-487c-a8a1-c0e7937f0a21)

Pertama tama menampilkan seluruh daftar barang yang ada 

![image](https://github.com/user-attachments/assets/24368091-84b4-41fc-a200-f51cb0206fe9)

kemudian akan ada output bahwa barang ditemukan dan melakukan input ganti nama,harga dan stock

![image](https://github.com/user-attachments/assets/736bbe27-bfcf-42b3-955f-4dc5517abae7)

jika kondisi terpenuhi maka akan ada output seperti diatas

## Pilihan hapus barang

![image](https://github.com/user-attachments/assets/0e011b34-f5bb-4c2b-ab59-8ea5245b7b78)

pertama akan menampilkan seluruh barang yang ada 

![image](https://github.com/user-attachments/assets/cd162959-91a1-4800-90d7-95a2e423e9b7)

lalu kemudian akan diminta untuk melakukan input ID barang, namun diatas terjadi kesalahan kodingan

![image](https://github.com/user-attachments/assets/5315d4c3-e38a-4a67-9159-0d895dba7ced)

ketika ID ditemukan maka otomatis barang akan di hapus dan menampilkan output seperti diatas

## Pilihan cari barang

![image](https://github.com/user-attachments/assets/25b84caf-d58b-4161-ad59-f9b6a6edd444)

pada menu ini akan diminta untuk input nama barang yang ingin dicari

![image](https://github.com/user-attachments/assets/4b761084-02fe-498c-9a6e-9745122ab586)

jika ditemukan maka akan ada output seperti diatas

## Pilihan Lihat daftar penyewaan

![image](https://github.com/user-attachments/assets/8a73a70d-bf15-45cd-bab4-988da052bd3a)

Pada fungsi ini akan menampilkan seluruh daftar penyewaan yang ada

## Pilihan mengembalikan barang

![image](https://github.com/user-attachments/assets/9ebb1d21-db48-41b8-9e97-2e2cca83353c)

pada fungsi ini akan diminta menginput nama penyewa dan nama barang yang disewa dan ketika ditemukan maka akan langsung otomatis dikembalikan

## pilihan menu keluar

![image](https://github.com/user-attachments/assets/edc96f63-7847-4a78-8356-3c241907f22f)

ketika memilih menu keluar maka akan ada output seperti diatas dan akan kembali ke menu login








