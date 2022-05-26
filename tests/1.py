# from aiogram import types, Dispatcher
# from create_bot import dp, bot
# from keyboards import kb_client_ok, kb_client_sos, kb_client_dal, kb_con_sam, kb_self_help, in_emoc, kb_client_work_with_emotions
# from aiogram.types import ReplyKeyboardRemove
# from aiogram.dispatcher.filters import Text
#
# # @dp.message_handler(commands=['start', 'help'])
# async def commands_start(message : types.Message):
#     await message.answer("Здравствуй! Я - бот. Я задам несколько вопросов.", reply_markup=kb_client_ok)
#
#
# # @dp.message_handler(commands=['Ok'])
# async def otv_ok(message : types.Message):
#     await message.answer("Определи своё психоэмоциональное состояние. Выбери цифру, где 1 - неприятно, но терпимо. 10 - невыносимо.", reply_markup=kb_client_sos)
#
#
# # @dp.message_handler(commands=['1_3'])
# async def otv_one_three(message : types.Message):
#     await message.reply("Вроде бы не всё так плохо? Ты можешь договориться с психологом о встрече в любой день с понедельника по пятницу, предварительно записавшись (ниже). Это конфидециально. Но в любом случае обрати внимание на свой режим труда/отдыха. Что ты можешь сделать для того, чтобы день был менее напряжённым? Исключи любые психоактивные вещества. Обязательно высыпайся! Отследи, что или кто добавляет дополнительный стресс? Подумай, что предаёт тебе сил? Запиши это в свои заметки. Забота о себе сейчас в приоритете.", reply_markup=kb_client_dal)
#
#
# # @dp.message_handler(commands=['4_6'])
# async def otv_four_six(message : types.Message):
#     await message.reply("Ок, давай поступим так: ты можешь договориться с психологом о встрече в любой день с понедельника по пятницу, предварительно записавшись. Это конфидециально. Чтобы ситуация не вышла из под контроля постарайся пока не принимать важных решений, если есть возможность дать себе время, поразмышляй о том, что сейчас в наиболее важно и по какой причине? Записывай свои мысли. Старайся позаботиться о своём режиме труда/отдыха, потому что это очень важно для психики. Для записи к психологу, жми.", reply_markup=kb_client_dal)
#
#
# # @dp.message_handler(commands=['7_10'])
# async def otv_seven_ten(message : types.Message):
#     await message.reply("Чтобы снять приступ сильной тревоги, сделай несколько глубоких вдохов с задержками, если можешь, выйди на свежий воздух. Дай себе время. В кризис самое главное остановиться и дать психике возможность поработать в 'default режиме' для самовосстановления. Перезагрузиться. В трудный период необходимо почувствовать опору. Вспомни, что тебе предаёт сил? Звонок близкому? Беседа с другом? Выписывание мыслей? Физическая активность? Музыка? Любые средства хороши для сохраниения себя в кризис. Если произошло психотравмирующее событие, с ним нужно работать. Чтобы получить профессиональную помощь запишись к психологу в любой день с понедельника по пятницу. Это конфидециально и безопасно.  Нажми для записи.", reply_markup=kb_client_dal)
#
#
# # @dp.message_handler(commands=['Далее'])
# async def dal_further(message : types.Message):
#     await message.answer("Выбери пожалуйста, что тебе сейчас больше подходит?", reply_markup=kb_con_sam)
#
#
# # @dp.message_handler(commands=['Личная_консультация'])
# async def link_expert(message : types.Message):
#     await message.answer("Напишите нам:\nhttps://t.me/psychology_ncfu")
#
#
# # @dp.message_handler(commands=['Самопомощь'])
# async def self_help(message : types.Message):
#     await message.answer("Что вам подходит?", reply_markup=kb_self_help)
#
#
# # РАСЗДЕЛ РАБОТА С ЭМОЦИЯМИ
# # @dp.message_handler(commands=['РАБОТА_С_ЭМОЦИЯМИ'])
# async def work_with_emotions(message : types.Message):
#     await message.answer("Эмоции - это реакция психики и тела на стимул. Если ты не отреагируешь, то напряжение будет расти и может проявиться в другом качестве или даже повлечь за собой соматические проявления. Напряжение можно снимать физической нагрузкой и упражнениями, которые соответствуют зоне напряжения. Выбери основную негативную эмоцию. Отследи, при каких обстоятельствах она проявляется ярче всего. Возможно само только осознание уже поможет реагировать более конструктивно. Но часто истинная причина не на поверхности, а в подсознании. Тут не обойтись без погружения в себя.", reply_markup=in_emoc)
#     await message.answer("Выберите одну из выше перечисленных эмоции или другой вариант", reply_markup=kb_client_work_with_emotions)
#
# # чтобы поймать то что за страхом
# @dp.callback_query_handler(text='strah')
# async def www_call(callback : types.CallbackQuery):
#     await callback.message.answer('Эмоция страха отнимает много сил. Из-за страха человек раздражен, насторожен, агрессивен. Тревога, это тоже разновидность страха. Тревога может переходить в панические атаки, что серьёзно портит человеку жизнь, по этому старайся не раскручивать тревогу. Избавляйся от напряжения через физ нагрузку, дыхательные техники, крик (можно выехать за город). Если состояние страха сохраняется, нужно искать первопричину. Возможно со специалистом, поскольку многие процессы проходят в психике бессознательно и самостоятельно увидеть их невозможно.')
#     await callback.answer('СТРАХ')
#
# # чтобы поймать то что за грустью
# @dp.callback_query_handler(text='grust')
# async def www_call(callback : types.CallbackQuery):
#     await callback.message.answer('Эмоция грусти подразумевает бессилие, неудовлетворенность и пассивное поведение. Как и любую другую эмоцию, грусть нужно отреагировать. Не уходи от этого состояния, а иди в него. Грусти. Плачь. Горюй. Опиши её. Почувствуй, где она в теле. Побудь с ней. Задай себе вопрос: что я могу для себя сделать? Каким образом? Помни, что музыка очень влияет на психо-эмоциональное состояние человека, по этому соответственно формируй свой плей-лист. Бывает грусть переходит в активную фазу, а затем в гнев. Будь к этому готов.')
#     await callback.answer('ГРУСТЬ')
#
# # чтобы поймать то что за злостью
# @dp.callback_query_handler(text='zlost')
# async def www_call(callback : types.CallbackQuery):
#     await callback.message.answer('Злость - естественная реакция, когда не удовлетворена потребность. Причем она может быть как топливом для достижения целей. Но так же она может "затмевать" разум переходить в ярость. Мышление сужается, становится ограниченным. Так же как и при страхе и при тревоге - необходимо приводить в активность голос и конечности. Уединись, встань и встряхнись всем телом несколько раз. Оскалься и порычи. Поработай кулаками. Попрыгай. Подыши глубоко. Если есть возможность пробежки на свежем в воздухе - прекрасно.')
#     await callback.answer('ЗЛОСТЬ')
#
# # чтобы поймать то что за апатией
# @dp.callback_query_handler(text='apat')
# async def www_call(callback : types.CallbackQuery):
#     await callback.message.answer('Безразличие и бессилие. Переутомление приводит к нехватке психической энергии, такое состояние называют "эмоциональное выгорание". Пропадает интерес к учебе, времяпрепровождению с друзьями и к удовольствиям. По этому очень важен режим учёбы/отдыха. Первым делом необходимо обеспечить себе достаточный сон, сбаласированный рацион питания для мозга и свежий воздух. И очень важно понимать, если подавлено настроение, потерян интерес к жизни, нарушен сон и аппетит и это состояние продолжительно, это возможно серьёзное органическое заболевание - депрессия. Депрессия - заболевание, при котором необходим врач!')
#     await callback.answer('АПАТИЯ')
#
#
#
#
#
#
#
#
# # регистрация хендлеров
# def register_handlers_client(dp: Dispatcher):
#     dp.register_message_handler(commands_start, commands=['start', 'help'])
#     dp.register_message_handler(otv_ok, commands=['Ok'])
#     dp.register_message_handler(otv_one_three, lambda message: '1-3' in message.text)
#     dp.register_message_handler(otv_four_six, lambda message: '4-6' in message.text)
#     dp.register_message_handler(otv_seven_ten, Text(equals='7-10', ignore_case=True))
#     dp.register_message_handler(dal_further, lambda message: 'Далее' in message.text)
#     dp.register_message_handler(link_expert, lambda message: 'Личная консультация' in message.text)
#     dp.register_message_handler(self_help, lambda message: 'Самопомощь' in message.text)
#     dp.register_message_handler(work_with_emotions, lambda message: 'РАБОТА С ЭМОЦИЯМИ' in message.text)