# Laporan Uang Bot
Pencatatan pengeluaran uang, menggunakan Bot Telegram yang terintegrasikan oleh Google SpreadSheets

<img src="https://raw.githubusercontent.com/wannazid/Bot-Laporan-Keuangan/main/Screenshot_2022-08-16-19-53-16-467_org.telegram.messenger.jpg" width="45%"> <img src="https://raw.githubusercontent.com/wannazid/Bot-Laporan-Keuangan/main/Screenshot_2022-08-16-19-51-55-618_com.google.android.apps.docs.editors.sheets.jpg" width="45%">
## Full Tutorial Lengkap
- https://youtu.be/Ja0PQAJ-I1E
## Menjalankan Bot
```bash
Download This Respository
```
```bash
Edit file python

bot_token = 'editnow'
sheets_url = 'editnow'
service_account('filejson.json')
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
- Buat new project dan service account dan buat key baru, download json nya dan simpan satu directory sama file python nya, enable juga api google drive dan google spreadsheets
- Buka laporanuang.py edit service_account('namafile.json') sesuaikan dengan key json kalian download, bot_token dan beserta sheets_url nya
- Jangan lupa bagikan user yang bisa edit file sheets nya, kalian masukin email pas buat project service account
- Jangan lupa membuat judul kolom yang ada dibawah ini
- Baru jalankan file python nya jika tidak akan error nantinya
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
