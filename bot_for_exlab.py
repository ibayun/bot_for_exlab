from aiogram import executor
from create_bot import dp

from handlers import client, admin, other

#client.handlers_client(dp)
admin.register_handlers_admin(dp)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

