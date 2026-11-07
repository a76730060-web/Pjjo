import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton

# Фиксируем цикл событий для Python 3.9 на macOS
loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)

# Вставь свой токен внутри кавычек
BOT_TOKEN = "9039798400:AAHsyY1PaVHoEJS-LesTYp24iN65q0Lb61Y"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

catalog_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Omega-3 Max Pure (120 капс.) — 1 890 ₽", callback_data="prod_omega")],
        [InlineKeyboardButton(text="L-Theanine Focus Mind (60 капс.) — 1 450 ₽", callback_data="prod_theanine")],
        [InlineKeyboardButton(text="Magnesium + B6 Night Calm — 1 200 ₽", callback_data="prod_magnesium")],
        [InlineKeyboardButton(text="Daily Multi-Formula A-Z — 1 650 ₽", callback_data="prod_vitamins")],
        [InlineKeyboardButton(text="D3 + K2 Active Complex — 990 ₽", callback_data="prod_d3")],
        [InlineKeyboardButton(text="✨ Neuro-Balance Deep Care [Набор 3-в-1] — 2 500 ₽", callback_data="prod_promo")]
    ]
)

@dp.message(CommandStart())
async def cmd_start(message: Message):
    greeting = (
        "Здравствуйте! Вы подключились к официальному сервису распределения продукции <b>NOVAGEN</b>.\n\n"
        "Мы создаем решения для тех, кто ценит чистоту восприятия и безупречный биологический баланс. "
        "Вся продукция сертифицирована по внутреннему регламенту безопасности.\n\n"
        "Пожалуйста, выберите интересующую позицию для проверки наличия и оформления отправки:"
    )
    await message.answer(greeting, reply_markup=catalog_keyboard, parse_mode="HTML")

@dp.callback_query(F.data.in_(["prod_omega", "prod_theanine", "prod_magnesium", "prod_vitamins", "prod_d3"]))
async def normal_product(callback: CallbackQuery):
    await callback.answer()
    text = (
        "📦 <b>Позиция подтверждена к отправке</b>\n\n"
        "Товар находится на центральном складе. Стандартный срок сборки: 1–3 рабочих дня.\n"
        "Отправка осуществляется сервисами СДЭК и Почта России.\n\n"
        "Для продолжения напишите в этот чат ваш город и ФИО получателя."
    )
    await callback.message.answer(text, parse_mode="HTML")

@dp.callback_query(F.data == "prod_promo")
async def promo_product(callback: CallbackQuery):
    await callback.answer()
    text = (
        "🌿 <b>Neuro-Balance Deep Care (Комплексная стабилизация)</b>\n"
        "<i>Специальная цена по программе адаптации: 2 500 ₽ (вместо 5 000 ₽)</i>\n\n"
        "Наш флагманский курс глубокого снятия стресса и гармонизации нервной системы. "
        "Устраняет лишнюю реактивность, тревожные триггеры и эмоциональное сопротивление. "
        "Вы почувствуете долгожданную ровную тишину уже после первого цикла приема.\n\n"
        "📌 <b>Условия передачи комплекса:</b>\n"
        "• Продукт отпускается только по прямому распределению (не для перепродажи).\n"
        "• Доставка выполняется выделенной службой логистики NOVAGEN лично в руки.\n"
        "• Курьер не звонит заранее — визит осуществляется в интервале спокойных часов по вашему геолокационному узлу.\n"
        "• Обязательное условие: непрерывность курса. Не прерывайте фазу стабилизации самостоятельно.\n\n"
        "Для внесения вас в распределительный реестр отправьте контактный номер или адрес постоянного пребывания."
    )
    await callback.message.answer(text, parse_mode="HTML")

@dp.message()
async def any_text_handler(message: Message):
    reply = (
        "✅ <b>Данные зафиксированы в реестре NOVAGEN.</b>\n\n"
        "Ваша заявка и сетевой идентификатор переданы в региональный отдел распределения. "
        "Ожидайте сотрудника службы сопровождения. Пожалуйста, оставайтесь по указанному адресу и не блокируйте уведомления."
    )
    await message.answer(reply, parse_mode="HTML")

async def main():
    print("Бот NOVAGEN успешно запущен и ждет сообщений...")
    await dp.start_polling(bot)

loop.run_until_complete(main())
