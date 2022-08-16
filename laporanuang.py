import gspread
import logging
from datetime import datetime
from aiogram import Bot, Dispatcher, types, executor

# Masukan Bot Token Kalian
# Masukan URL GoogleSpreadSheets 
bot_token = 'ACCES TOKEN'
sheets_url = 'SHEETS URL EDIT'

# Ubah Menjadi Nama File Json Key Kalian
# Harus Satu Folder Dengan bot.py File .json nya
gsheets = gspread.service_account(filename='filenya.json')
open_sheets = gsheets.open_by_url(sheets_url)

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
logging.info('Try logged in !')
bot = Bot(token=bot_token)
dp = Dispatcher(bot=bot)
logging.basicConfig(level=logging.INFO)

@dp.message_handler(commands=['help','start'])
async def cara_pengunaan(pesan: types.Message):
	await pesan.answer('''
	
	Selamat Datang Di Bot Laporan Pengeluaran Uang ^_^
	
	Contoh Pengunaan :
		
		/new kategori #harga item
		/new makanan #5.000 roti,minuman
		
	Perhatian :
		
		• Jangan menggunakan spasi dalam kategori,item maupun harga
		
		Contoh tidak pake spasi :
			
			/new makanan #5.000 roti,makanan
			
		Contoh menggunakan spasi :
			
			/new makanan #5.000 roti makanan
			
	Bisa menggunakan , - _ dan sebagaianya.
	
	''')

@dp.message_handler(commands=['new'])
async def laporan_uang(pesan: types.Message):
	x = pesan.text.replace('/new','')
	name = pesan.from_user.first_name
	id_name = pesan.from_user.id
	xy = x.split('#')
	dt = datetime.now()
	tgln = dt.strftime("%Y-%m-%d/%H:%M:%S")
	inserts = open_sheets.sheet1
	try:
		all = str(tgln)+xy[0]+xy[1]+' '+name+' '+str(id_name)
		splits = all.split()
		ins = inserts.append_row(splits)
		await pesan.answer('Laporan Berhasil !')
	except:
		await pesan.answer('Laporan Gagal, Pastikan Cara Pengunaanya Benar !')
	
if __name__ == '__main__':
	executor.start_polling(dp,skip_updates=True)