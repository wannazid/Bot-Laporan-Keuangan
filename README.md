# Laporan Uang Bot
Pencatatan pengeluaran uang, menggunakan Bot Telegram yang terintegrasikan oleh Google SpreadSheets

<img src="https://raw.githubusercontent.com/wannazid/Bot-Laporan-Keuangan/main/Screenshot_2022-08-16-19-53-16-467_org.telegram.messenger.jpg" width="45%"> <img src="https://raw.githubusercontent.com/wannazid/Bot-Laporan-Keuangan/main/Screenshot_2022-08-16-19-51-55-618_com.google.android.apps.docs.editors.sheets.jpg" width="45%">
## Menjalankan Bot
```bash
Install Git Now
```
```bash
git clone https://github.com/wannazid/Bot-Laporan-Keuangan
```
```bash
cd Bot-Laporan-Keuangan
```
```bash
pip install -r req.txt
```
```bash
python3 laporanuang.py
```
![alt text](https://github.com/wannazid/Bot-Laporan-Keuangan/blob/main/IMG_20220816_225601.jpg)
## Mendapatkan Acces Token/Bot Token
- Buka telegram dan cari @BotFather
- Pilih create new bot, masukan nama bot
- Buat username bot (tes_bot)
- Kamu akan mendapatkan acces token nya
## Cara Menggunakan
- Buka console cloud google : https://console.cloud.google.com
- Buat service account dan buat key baru, download json nya dan simpan satu directory sama file python nya, enable juga api google drive dan google spreadsheets
- Buka bot.py edit service_account('namafile.json') sesuaikan dengan key json kalian download
- Jangan lupa bagikan user yang bisa edit file sheets nya, kalian masukin email pas buat project service account
- Jika bot sudah dijalankan masukan url spreadsheets dan bot token
## Buat Judul Kolom Spreadsheets
- Tanggal
- Kategori
- Harga
- Item
- Nama Pelapor
- ID Pelapor (ID Telegram)
## Cara Memasukan
- /new (kategori) #harga (item)

contoh : /new dapur #10.000 bawang-putih,bawang-merah

- Perhatian : untuk item dan kategori jangan sampai menggunakan spasi/space

contohnya : /new dapur #10.000 bawang putih

### Inspiration From 
- https://github.com/tegohsx/laporan-keuangan-bot
## Thanks For Use This Bot
