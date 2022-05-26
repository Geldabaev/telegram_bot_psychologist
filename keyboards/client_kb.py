from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton

ok_kb = KeyboardButton('/Ok')
# resize_keyboard=True чтобы клавиатура не была большой слишком
# one_time_keyboard=True скрывается, но не исчежает после нажатия
kb_client_ok = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
# Добавляем кнопки в клавиатуру
kb_client_ok.add(ok_kb)


kb_sos1 = KeyboardButton('1-3')
kb_sos2 = KeyboardButton('4-6')
kb_sos3 = KeyboardButton('7-10')
kb_client_sos = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_client_sos.add(kb_sos1).add(kb_sos2).add(kb_sos3)


kb_dal = KeyboardButton('Далее')
kb_client_dal = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_client_dal.add(kb_dal)


kb_con = KeyboardButton('Личная консультация')
kb_sam = KeyboardButton('Самопомощь')
kb_con_sam = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_con_sam.row(kb_con, kb_sam)


#--------------------------------------------------------------------
kb_sam1 = KeyboardButton('РАБОТА С ЭМОЦИЯМИ')
kb_sam2 = KeyboardButton('РАБОТА С МЫСЛЯМИ')
kb_sam3 = KeyboardButton('РАБОТА С СИТУАЦИЕЙ')
kb_sam4 = KeyboardButton('ПАНИЧЕСКАЯ АТАКА')
kb_sam5 = KeyboardButton('СТРЕСС')
kb_self_help = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_self_help.add(kb_sam1).add(kb_sam2).add(kb_sam3).add(kb_sam4).add(kb_sam5)


kb_strah = KeyboardButton('страх')
kb_grust = KeyboardButton('грусть')
kb_zlo = KeyboardButton('злость')
kb_ap = KeyboardButton('апатия')
kb_zapis = KeyboardButton('Запись к психологу')
kb_emoc = KeyboardButton('эмоции')
kb_back = KeyboardButton('вернуться')

kb_client_strah = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_client_grust = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_client_zlo = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_client_ap = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
# для следущего не требуется создавать отдельный хендлер, хенделр личная консультация берет это на себя
# мы создали его только для кнопки
kb_client_zapis = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_client_emoc = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_client_back = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

kb_client_emoc.row(kb_strah, kb_grust, kb_zlo, kb_ap, kb_back).add(kb_zapis)
kb_client_strah.row(kb_emoc, kb_grust, kb_zlo, kb_ap, kb_back).add(kb_zapis)
kb_client_grust.row(kb_strah, kb_emoc, kb_zlo, kb_ap, kb_back).add(kb_zapis)
kb_client_zlo.row(kb_strah, kb_grust, kb_emoc, kb_ap, kb_back).add(kb_zapis)
kb_client_ap.row(kb_strah, kb_grust, kb_zlo, kb_emoc, kb_back).add(kb_zapis)
#-------------------------------------------------------------------------

# РАБОТА С МЫСЛЯМИ
kb_situac = KeyboardButton('Работа с ситуацией')
kb_work_emoc = KeyboardButton('Работа с эмоциями')
kb_client_misly = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_client_misly.row(kb_work_emoc, kb_situac, kb_zapis, kb_back)

# РАБОТА С СИТУАЦИЕЙ
kb_misly = KeyboardButton('Работа с мыслями')
kb_client_cituacy = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_client_cituacy.row(kb_work_emoc, kb_misly, kb_zapis, kb_back)

# ПАНИЧЕСКАЯ АТАКА
kb_client_what_to_do = InlineKeyboardMarkup(row_width=2)
kb_do = InlineKeyboardButton(text='Что делать?', callback_data='whatdo')
kb_in_zapis = InlineKeyboardButton(text='Запись к психологу', callback_data='zapis')
kb_client_what_to_do.add(kb_do, kb_in_zapis)

kb_chto_z_back = InlineKeyboardMarkup(row_width=3)
kd_chto = InlineKeyboardButton(text='Что это такое?', callback_data='chto')
kb_chto_z_back.add(kd_chto, kb_in_zapis)
#-------------------------------------------------------------------
# РАЗДЕЛ СТРЕСС

kb_stress_dl = KeyboardButton('Длительный стресс')
kb_stress_kr = KeyboardButton('Короткий интенсивный стресс')
kb_stress = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_stress.add(kb_stress_dl).add(kb_stress_kr).add(kb_zapis)


# Короткий интенсивный стресс
kb_cht_pr = KeyboardButton('Что происходит?')
kb_kr_stress = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_kr_stress.add(kb_cht_pr).add(kb_stress_dl).add(kb_zapis)


# Длинный стресс
cht_kr_zap = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
cht_kr_zap.add(kb_cht_pr).add(kb_stress_kr).add(kb_zapis)