from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


info_markup = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="📰 Новини", callback_data='news'),
        ],
        [
            InlineKeyboardButton(text="⚖️ Законодавство", callback_data='laws'),    
        ],
        [
            InlineKeyboardButton(text="🔠 Термінологія", callback_data='termins'),    
        ],
        [
            InlineKeyboardButton(text="🗂 УКТЗЕД", url='https://www.mdoffice.com.ua/ua/aGetExplain.doCollaps?par=1&goods_code='),    
        ],
        [
            InlineKeyboardButton(text="🔎 Пошук в УКТЗЕД", url='https://www.mdoffice.com.ua/ua/aMDOTNVD2020.TNVDFindForm'),    
        ],
        [
            InlineKeyboardButton(text="📗 Митний тариф", url='https://cabinet.customs.gov.ua/tnvinfo'),    
        ],
        [
            InlineKeyboardButton(text="🗺 Митна мапа", url='https://www.mdoffice.com.ua/pls/MDOffice/maps.main.iframe'),    
        ],
        [
            InlineKeyboardButton(text="🏢 Митні органи", url='https://www.mdoffice.com.ua/ua/aMDOClassDic.doCollaps?dic_num=10'),    
        ],
        [
            InlineKeyboardButton(text="💱 Курси валют", url='https://www.mdoffice.com.ua/ru/aMDOCurr.html'),    
        ],
    ],
)