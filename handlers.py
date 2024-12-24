from aiogram import F, Router, Dispatcher, Bot, types
from aiogram.types import Message, CallbackQuery, LabeledPrice, PreCheckoutQuery
from aiogram.filters import CommandStart, Command, CommandObject
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.exceptions import TelegramBadRequest
from aiogram.enums.parse_mode import ParseMode
from api import AioCryptoPay

router = Router()
adminid =5129878568
chat_id=-1002449672567

@router.message(CommandStart())
async def _(message: Message):
    await AioCryptoPay.create_invoice(10)