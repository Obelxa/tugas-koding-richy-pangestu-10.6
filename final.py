from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes


key_token = "6333600200:AAHLT9UmJiAmFQdRMe1FS2bzm_dzGHYZgKc" 
user_bot: Final = "LI_ZURE_BOT" 


async def start_command(update: Update, context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Halo! Terimakasih karena anda ingin berbincang dengan saya ")
    
async def help_command(update: Update, context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Kirim pesan, bot akan membalas pesan..")

async def custom_command(update: Update, context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("ini command custom")
#respon

async def handle_message(update: Update, context:ContextTypes.DEFAULT_TYPE):
    proccesed : str = update.message.text
    print(f"Pesan diterima : {proccesed}")
    text_accept = proccesed.lower()
    if 'halo' in text_accept:
        await update.message.reply_text("halo!")
    elif 'kamera budget pelajar apa yaa?' in text_accept:
        await update.message.reply_text("saya memiliki beberapa kamera dari berbagai brand, yang pertama dari merek Nikon, di brand ini saya menyarankan anda mengambil nikon seri D5200 dengan harga Rp.3,000,000+. Untuk brand Canon, Saya menyarankan mengambil Canon 600D dengan harga 4,500,000. Untuk Sony saya menyarankan anda untuk mengambil Sony A5100 dengan harga Rp.4,200,000,dan yang terakhir saya menyarankan anda untuk mengambil kamera Fujifilm XA-5 dengan harga Rp.4,500,000. 'PERLU DIINGAT KEMBALI BAHWA HARGA YANG TERTERA ADALAH HARGA KAMERA YANG BEKAIS PAKAI ")
    elif 'liz' in text_accept:
        await update.message.reply_text(f"Ada yang bisa saya bantu?")
    else:
        await update.message.reply_text("saya tidak mengerti apa yang anda katakan!!")



async def photo_message(update: Update, context:ContextTypes.DEFAULT_TYPE):
    return await update.message.reply_text("wah bagus juga..")


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')




    
if __name__ == '__main__':
    print('starting bot....')
    app = Application.builder().token(key_token).build()

    #commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))

    # messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))
    app.add_handler(MessageHandler(filters.PHOTO, photo_message))

    #errors
    app.add_error_handler(error)

    # polls 
    print('polling.....')
    app.run_polling(poll_interval=3)