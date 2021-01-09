from aiogram import types
from loader import dp, bot

from keyboards.inline import info_markup
import datetime
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import feedparser


@dp.message_handler(text="ℹ️ Інфо")
async def bot_info(message: types.Message):
    await message.answer('<b>ІНФОРМАЦІЙНІ РЕСУРСИ</b>')
    await message.answer('Новини в митній сфері, зміни в митному законодавстві, законодавство з питань фінансових гарантій, митні класифікатори та сторонні ресурси',
                         reply_markup=info_markup)

@dp.callback_query_handler(text_contains="news")
async def info_news(call: types.CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer('📰 <b>МИТНІ НОВИНИ</b>')
    await call.message.answer('Останні новини в митній сфері, зміни в митному законодавстві, контрабанда та порушення митних правил')
    url = 'http://www.qdpro.com.ua/rss'
    posts = feedparser.parse(url)
    posts.entries = sorted(list(posts.entries)[:10], key=lambda k: k['published'])
    for entry in posts.entries:
        link_markup = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text="📖 Читати далі...", url=entry['link']),
                ],
            ],
        )
        fdate = datetime.datetime.strptime(entry.get('published'), '%a, %d %b %Y %H:%M:%S %z').strftime('%d.%m.%Y %H:%M')
        await call.message.answer(entry['title']+'|'+fdate, reply_markup=link_markup)

@dp.callback_query_handler(text_contains="laws")
async def info_laws(call: types.CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer('⚖️ <b>ЗАКОНОДАВСТВО</b>')
    await call.message.answer('Нормативно-правові акти з питань фінансових гарантій')   
    link_markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="📖 Читати далі...", url='https://zakon.rada.gov.ua/laws/show/4495-17#n2535'),
            ],
        ],
    )
    await call.message.answer('1️⃣ Митний кодекс України | № 4495-VI, 13.03.2012, Кодекс, Верховна Рада України', reply_markup=link_markup)
    link_markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="📖 Читати далі...", url='https://zakon.rada.gov.ua/laws/show/461-2012-%D0%BF#Text'),
            ],
        ],
    )
    await call.message.answer('2️⃣ Про затвердження переліку товарів, ввезення яких на митну територію України та/або переміщення територією України прохідним та внутрішнім транзитом здійснюється за умови обов’язкового надання митним органам забезпечення сплати митних платежів | №461, 21.05.2012, Постанова, Кабінет Міністрів України', reply_markup=link_markup)
    link_markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="📖 Читати далі...", url='https://zakon.rada.gov.ua/laws/show/z0860-20#Text'),
            ],
        ],
    )
    await call.message.answer('3️⃣ Про затвердження форм бланків фінансових гарантій та порядку їх заповнення | №404, 07.07.2020, Наказ, Міністерство фінансів України', reply_markup=link_markup)
    link_markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="📖 Читати далі...", url='https://zakon.rada.gov.ua/laws/show/390-2013-%D0%BF#Text'),
            ],
        ],
    )
    await call.message.answer('4️⃣ Про визначення пунктів пропуску через державний кордон України, через які здійснюється переміщення підакцизних товарів, та визнання такими, що втратили чинність, деяких актів Кабінету Міністрів України | №390, 29.05.2013, Постанова, Кабінет Міністрів України', reply_markup=link_markup)
    link_markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="📖 Читати далі...", url='https://zakon.rada.gov.ua/laws/show/85-2018-%D0%BF#Text'),
            ],
        ],
    )
    await call.message.answer('5️⃣ Про затвердження Порядку надання розстрочення сплати податку на додану вартість та застосування забезпечення виконання зобов’язань під час ввезення на митну територію України обладнання для власного виробництва на території України | №85, 07.02.2018, Постанова, Кабінет Міністрів України', reply_markup=link_markup)

@dp.callback_query_handler(text_contains="termins")
async def info_termins(call: types.CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer('🔠 <b>ТЕРМІНОЛОГІЯ</b>')
    await call.message.answer('Термінологічний словник з питань фінансових гарантій')
    await call.message.answer('''1️⃣ <u>Гарант (незалежний фінансовий посередник)</u> – юридична особа, створена відповідно до законодавства України та внесена до Реєстру гарантів, діє на підставі Митного кодексу України та Угоди про надання фінансових гарантій з Держмитслужбою та має право на видачу фінансових гарантій митним органам.''')
    await call.message.answer('''2️⃣ <u>Фінансова гарантія</u> є безвідкличним зобов’язанням гаранта, внесеного до реєстру гарантів, виплатити на вимогу митного органу кошти в межах певної суми у разі невиконання забезпечених цією гарантією зобов’язань із сплати митних платежів.''')
    await call.message.answer('''3️⃣ <u>Індивідуальна фінансова гарантія</u> надається у паперовому або електронному вигляді на суму митних платежів за:
1) однією митною декларацією в межах однієї зовнішньоторговельної операції;
2) однією митною декларацією в межах однієї транзитної операції;
3) одним документом контролю за переміщенням товарів;
4) однією операцією з переміщення через митний кордон України товарів громадянами у випадках, визначених розділом XII Митного кодексу України.''')
    await call.message.answer('''4️⃣ <u>Багаторазова фінансова гарантія</u> надається для забезпечення сплати митних платежів за кількома митними деклараціями або документами контролю за переміщенням товарів при ввезенні товарів на митну територію України з метою транзиту або для вільного обігу на цій території для одного власника в рамках одного зовнішньоекономічного договору.''')
    await call.message.answer('''5️⃣ <u>Загальна фінансова гарантія</u> використовується для забезпечення сплати митних платежів за кількома зобов’язаннями АЕО, що випливають з митних процедур відповідно до Митного кодексу України у будь-якій митниці на всій митній території України незалежно від митного режиму.''')
    await call.message.answer('''6️⃣ <u>Гарантійний випадок</u> – факт невиконання особою, відповідальною за сплату митних платежів, зобов’язань, забезпечених фінансовою гарантією, що випливають з митних процедур, у зв’язку з настанням якого гарант зобов’язується сплатити митному органу кошти в сумі митних платежів за відповідною фінансовою гарантією.''')
