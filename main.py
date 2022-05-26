from aiogram.utils import executor
from create_bot import dp



# сообщение нам о том что бот запущен
async def on_startup(_):
    print('Бот вышел в онлайн')


# переносим регистрацию хандлеров
from handlers import client, admin, other

client.register_handlers_client(dp)
other.register_handlers_other(dp)

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
# без skip_updates=True после выхода бота в онлайн нас засыпят сообщениями которые накопились