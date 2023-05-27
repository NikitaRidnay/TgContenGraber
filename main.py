from telethon import TelegramClient
import time, telethon
import sys
import pytz
from getpass import getpass
from time import sleep
from telethon.errors import SessionPasswordNeededError
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import InputPeerChat, InputPeerChannel
from telethon.tl.functions.contacts import ResolveUsernameRequest
from telethon.tl.types import ChannelParticipantsSearch, InputChannel
from telethon.tl.types import PeerUser, PeerChat, PeerChannel
import configparser
import json
from telethon.tl.functions.messages import GetHistoryRequest
from telethon.tl.types import Channel, InputChannel
from random import randrange

from telethon.sync import TelegramClient
from telethon import connection

# для корректного переноса времени сообщений в json
from datetime import  datetime


# класс для работы с сообщениями
from telethon.tl.functions.messages import GetHistoryRequest

from colorama import init, Fore, Back, Style

# Написал @antiniks


# Присваиваем значения внутренним переменным
api_id =20581589
api_hash = 'ecbdbafc89f87c4d5e41b164cac7583d'

timezone = pytz.timezone('Europe/Moscow')
start_date = datetime(year=2023, month=4, day=14, hour=0, minute=0, second=0, tzinfo=timezone)  #настройка времени с которого будут браться сообщения
total_count = 0
delay = 5  # задержка в 5 сек перед отравкой след сообщения
client = TelegramClient('resend', api_id, api_hash)
client.start()










async def check(amount):

    me = await client.get_me()

    i = 1
    print("\n\n\nСписок диалогов:\n")
    async for dialog in client.iter_dialogs():
        print('Диалог', dialog.name, 'имеет айди', dialog.id)
        i += 1
        if i > amount and amount != int('0'):
            break


while True:
    print('''


Выберите действие:

1)Список чатов
2)Начать спам рассылку по группам
3)Выйти


''')
    change = input()
    if change.isdigit() == False:
        print('''Ошибка? Пиши нормально.
1)Список чатов
2)Начать спам рассылку по группам
3)Выйти

''')

    elif int(change) == 1:
        new_change = input("Введите сколько последних диалогов отобразить (введите 0, если отобразить все): ")
        if new_change.isdigit() == False:
            print('''

1)Список чатов
2)Начать спам рассылку по группам
3)Выйти

''')
        else:
            with client:
                client.loop.run_until_complete(check(int(new_change)))
    elif int(change) == 3:
        print("Пока...\nСозданно @antiniks")
        exit(':)')

    if int(change) == 2:

        print('Если имеются проблемы с софтом пишите прогеру: @antiniks')



        from_channels = [-1001976831202, -1001642191306]#каналы доноры
        target_channels=[-1001604710589, -1001903515753]#отправка в эти каналы
        target_entities = [client.get_entity(channel) for channel in target_channels if client.get_entity(channel)]

        Sent_count = 0#не меняем

        max_messages = 10  #максимальное кол-во сообщений



        while Sent_count < max_messages:

            for from_channel in from_channels:

                messages = client.iter_messages(from_channel)

                total_count = len(list(messages)) * len(target_entities)

                for message in messages:

                    if message.date >= start_date:

                        for entity in target_entities:

                            if Sent_count < max_messages:

                                try:
                                    client.send_message(entity,message)#без пометки
                                    #client.forward_messages(entity, message)#с пометкой о пересылке

                                    Sent_count += 1

                                except Exception as e:

                                    print(f"Ошибка отправки: {e}")

                            else:

                                print(Fore.CYAN, 'все сообщения отправлены')

                                exit()
                        print('Ограничения установленные в скрипте:',max_messages)
                        print('Всего сообщений в каналах:', total_count)
                        print(Fore.BLUE, f"Успешно отправленных: {Sent_count}")

                        time.sleep(delay)

        print(Fore.CYAN, 'Достигнут лимит сообщений')
        time.sleep(delay)


