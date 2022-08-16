# Laporan Uang Bot
Pencatatan pengeluaran uang, menggunakan Bot Telegram yang terintegrasikan oleh Google SpreadSheets

## Mendapatkan Acces Token/Bot Token
- Buka telegram dan cari @BotFather
- Pilih create new bot, masukan nama bot
- Buat username bot (tes_bot)
- Kamu akan mendapatkan acces token nya
## Cara Menggunakan
- Buka console cloud google : https://console.cloud.google.com
- Buat service account dan buat key baru, download json nya dan simpan satu directory sama file python nya, enable juga api google drive dan google spreadsheets
- Buka bot.py edit service_account('namafile.json') sesuaikan dengan key json kalian download
- Jika bot sudah dijalankan masukan url spreadsheets dan bot token
## Buat Judul Kolom Spreadsheets
- Tanggal
- Kategori
- Harga
- Item
- Nama Pelapor
- ID Pelapor
## Penting
