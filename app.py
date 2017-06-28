# -*- coding: utf-8 -*-
import os
from flask import Flask
import telepot
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, ForceReply
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
from telepot.namedtuple import InlineQueryResultArticle, InlineQueryResultPhoto, InputTextMessageContent



import sys
# sys.setdefaultencoding() does not exist, here!
reload(sys)  # Reload does the trick!
sys.setdefaultencoding('UTF8')

app = Flask(__name__)

@app.route('/')
def hello():
    return 'strix bot'

def handle(msg):
 content_type, chat_type, chat_id = telepot.glance(msg)
 if content_type == 'text':
    command = msg['text']
    print ('Got command: %s' % command)
    mss = command
    a='راه های ارتباطی'
    b='کاروما چیست؟'
    bb='کاروما تیمی جوان و نوپا, متشکل از مهندسین متعهد و باسابقه می باشد که در امور تخصصی, فنی و مهندسی مانند ایده پردازی، طراحی، نظارت و اجرا توانا بوده و در سال1395 فعالیت خود را آغاز نمودند'
    c='تیم کاروما'
    d='چرا باید کاروما را انتخاب کنید'
    dd='کاروما تركیبی قوی از افراد متخصص، جوان و کارآمد است که خواسته ها و نیازهای شما را شناسایی کرده و با بهترین نیروی انسانی و بهره برداری از مناسب ترین امکانات فنی و نرم افزاری قادر به ارائه راهکار ها و خدمات تخصصی به شماست.یک همکاری خوب نیازمند تیمی مستعد،نوآور و خلاق با قدرت ریسک پذیری میباشد. کاروما با تکیه بر نیروی انسانی خود به خوبی از پس خواسته های شما بر می آید'  
    markup = ReplyKeyboardMarkup(keyboard=[[d,b],[a,c]])
    markup2 = InlineKeyboardMarkup(inline_keyboard=[
                     [dict(text='سایت بهین اجرا کاروما', url='http://behkaroma.ir')],
                     [dict(text='کانال تلگرام', url='http://t.me/behkaroma')],
                     [dict(text='اینستاگرام', url='http://instagram.com/behkaroma')],
                     [dict(text='توییتر', url='http://twitter.com/behkaroma')],
                     [dict(text='لینکدین', url='http://www.linkedin.com/company/behkaroma')],
                     [dict(text='فیسبوک', url='https://www.facebook.com/Behkaroma-306939019727925')],

                 ])
    markup3 = InlineKeyboardMarkup(inline_keyboard=[
                     [dict(text='رضا نیک صفت', url='http://t.me/Rezaniksefat')],
                     [dict(text='مهران مطیعی', url='http://t.me/straxico')],
                     [dict(text='امیر حسین طاهر', url='http://t.me/Coantomi')],
                     [dict(text='خاطره مسیحا', url='http://t.me/Khaterekhanum')],
                     [dict(text='یاسمن زارع زاده', url='http://t.me/yass_z')],
                     [dict(text='گلبرگ عبدل پناه', url='https://t.me/GlbrgAp')],
                     [dict(text='فاطمه اعتمادی', url='https://t.me/FatemehEt_1996')],

                 ])
    
    
    
    if mss==a:
     bot.sendMessage(chat_id, 'راه های ارتباطی با کاروما', reply_markup=markup2)
    elif mss==b:
     bot.sendMessage(chat_id, text= bb )
    elif mss==c:
     bot.sendMessage(chat_id, 'اعضای تیم کاروما', reply_markup=markup3)
    elif mss==d:
     bot.sendMessage(chat_id, text= dd )
    else :
      bot.sendMessage(chat_id, text= 'کاروما',reply_markup=markup )








def on_callback_query(msg):
    query_id, from_id, data = telepot.glance(msg, flavor='callback_query')
    print('Callback query:', query_id, from_id, data)

    if data == 'notification':
        bot.answerCallbackQuery(query_id, text='Notification at top of screen')
    elif data == 'tell':
        bot.answerCallbackQuery(query_id, text='01333507643', show_alert=True)







bot = telepot.Bot('341566965:AAFyS569nVLsoVqmGwWEtbzlfdEKW8cqnw4')
bot.message_loop(handle)
print ('I am listening ...')

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
    

while 1:
    time.sleep(10)
