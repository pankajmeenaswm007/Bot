import telebot
import pywhatkit
import time
 
Token="6440488829:AAEXMg501ZTH6exI_7-DzINm3bIbCVm-Tg8"

bot=telebot.TeleBot(Token)

@bot.message_handler(['start','start'])
def start(message):
    bot.reply_to(message," Welcome to Bizhooter - AutoWhatsSender ")

@bot.message_handler(['about'])
def about(message):
    msg="""Bizhooter bluk message sender
    📢📢📢📢📢📢📢

    मिनटों में अपने प्लान को लाखो लोगो को भेजें
    Send 1 lakh WhatsApp MSG one click
    किसी भी कम्पनी में अब नेटवर्क बनाना हुआ आसान, मिनटों में अपना प्लान, सर्विस और प्रोडक्ट को लाखो लोगो तक whatsapp करे
    https://youtu.be/Je2JWLCjbSU

    TRIAL......FREE....TRIAL.....FREE

    👉 Bizhooter APP link-
    https://play.google.com/store/apps/details?id=com.bizhooter&referrer=zklfxe

    👉 Full Tutorial video Hindi
    https://youtu.be/MrnjXcULO7c

    👉 English tutorial
    https://youtu.be/aN9hy36lqMQ

    👉 Support Group
    https://chat.whatsapp.com/C9pCxlO3JFBEeZapHDg1Tt
    -------------------------------------
    ----------------------------------------------
    👉 One year charge = 299rs
    👉 Life time charge = 499rs
 
    Call/whatsapp करे 8824703209

    Reseller Partner बनो लाखों कमाओ
    Pay 1499rs earn profit 15000rs
    Pay  2999rs earn profit 40000rs
    Pay 4999rs earn profit 100000rs

    50% Direct referral bonus

    👉 नंबर नहीं बैन होने की गारेंटी
    👉किसी भी नंबर से किसी को भी मैसेज भेजे
    👉वॉट्सएप ग्रुप से सेकंडों में नंबर निकाले 
    👉लाखो नंबर पर मैसेज भेजे मिंटो में
    👉कितने भी ग्रुप में शिड्यूल मैसेज भेजे
    👉ऑटो रिप्लाइ सिस्टम 
    👉वेलकम मैसेज
    👉किसी भी फाइल से कॉन्टेक्ट import/export करे
    👉जब मर्जी हो तब कैंपेन को resume/on/off करें 
    👉गूगल से डाटा एक्स्ट्रक्ट करे किसी भी
    👉 मल्टी WhatsApp account सपोर्ट 
    👉बहुत सारे anti banned फीचर जो आपके व्हाट्सएप ब्लॉक नहीं होता
    👉 लेपटॉप/ डेस्कटॉप की जरूरत नहीं मोबाइल पर ही सब कुछ
    👉 बटन और लिंक api
    👉 मीडिया फोटो,ऑडियो,वीडियो,कैप्शन
    👉और भी बहुत कुछ...

    Note- Life Time प्लान में आपका whatsapp banned नहीं होता है

    Registration
    लिंक पर क्लिक कर के आप इसे इंस्टॉल कर सकते है 
    उसके बाद ईमेल/ मोबाइल नंबर डालकर ओटीपी डाले  रजिस्ट्रेशन हो जाएगा फिर आप अपना प्लान सेलेक्ट करे कि कितने दिन आपको यूज करना है
    एक्टिवेशन के लिए पैसा 8824703209 पर phonepe/paytm करे तथा स्क्रेशोट मुझे 8824703209 पर भेजे साथ में अपना नाम, मोबाइल नंबर भेजे जिस नंबर से रजिस्ट्रेशन किया है , या फिर खुद ही subscription by getway  में जाकर गेटवे से एक्टिवेट कर सकते है

    Helpline number 8824703209"""
    bot.reply_to(message,msg)

@bot.message_handler(['whatsapp'])
def whatsapp(message):
    curr = time.localtime()
    bot.reply_to(message,"Support Group https://chat.whatsapp.com/C9pCxlO3JFBEeZapHDg1Tt")

@bot.message_handler(['AppNotWorking'])
def AppNotWorking(message):
    bot.reply_to(message," Please send Your problem screenrocoding  whatsapp +918824703209   ")

@bot.message_handler(['download'])
def download(message):
    bot.reply_to(message,"  Bizhooter Play Store Link  https://play.google.com/store/search?q=bizhooter&c=apps   Website Link  https://autowhatssender.com")

@bot.message_handler(['features'])
def features(message):
    msg="""  LIFE TIME VALIDITY ( Full Technical Support )
    ✅Bulk Send Unlimited Messages
    ✅Bulk Send Messages to Groups
    ✅No Laptop/Desktop Required
    ✅Grab Member From Group
    ✅Send Images/Videos/Files
    ✅Bulk Grab Wa Group Links
    ✅ Welcome Massage
    ✅Whatsapp Autoreply Bot
    ✅B2B Google Map Extractor
    ✅Allows Unlimited Messages
    ✅Multimedia Support
    ✅Image With Caption
    ✅Multi-Channel Support
    ✅Customized Messages
    ✅Video Support
    ✅Multiple Account Supported
    ✅Business Product Catalogue
    ✅Numbers Filter
    ✅ Whatsapp Group Contact Extract
    ✅Advance Settings
    ✅Anti Banned Features
    ✅Auto Reply
    ✅Dynamic Chatbot
    ✅Multi Group Posting
    ✅Message Scheduling
    ✅Import from WhatsApp
    ✅Sent History
    ✅Refer & Earn
    ✅Unsubscribe List
    ✅Dropped campaign Resume
    ✅Export Your grabbed Contact
    ✅ New Coming Features Including"""
    bot.reply_to(message,msg)

@bot.message_handler(['support'])
def support(message):
    bot.reply_to(message," Helpline Numbers 1.+918824703209 2.+918302880499  3.+919079385727           Email = autobulkmarketing@gmail.com")

@bot.message_handler(['help'])
def help(message):
    bot.reply_to(message,"Of course, I'm here to help! How can I assist you today? Please provide more details or let me know what you need assistance with, and I'll do my best to provide the information or guidance you're looking for.")

@bot.message_handler(['videos'])
def videos(message):
    bot.reply_to(message,"1.Full Details Videos https://youtu.be/aN9hy36lqMQ    2. Demo Video https://www.youtube.com/shorts/Rj2NSigLCs4?feature=share     3. B2B Marketing https://youtu.be/T4C99wSxOeA")

@bot.message_handler(['subscription'])
def subscription(message):
    msg="""Personal use subscription
    👉 One year charge = 299rs
    👉 Life time charge = 499rs
 
    Reseller member subscription

    Reseller Partner बनो लाखों कमाओ
    Pay 1499rs earn profit 15000rs
    Pay  2999rs earn profit 40000rs
    Pay 4999rs earn profit 100000rs"""
    bot.reply_to(message,msg)


@bot.message_handler()
def custom(message):
    try:
        msg=eval(message.text.strip())

    except Exception as e:
        msg=""" Bizooter -AutoWhatsender I can help you. If you need any help You can control me by sending these commands:
        
        /about - Details about the app

        Download
        /download - Bizhooter Download link and website

        Bizooter -AutoWhatsender Videos 
        /videos - Compleate information amd process

        Bizooter -AutoWhatsender Features
        /features - App Features

        /subscription - App subscription

        /AppNotWorking - Not working Problem Solve Few Minutes

        /whatsapp - whatsapp gruops

        Support 
        /support - Helpline number and email
        /help - HELP
       
         """

    bot.reply_to(message,msg)


bot.polling()