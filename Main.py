import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import requests
import random
import bs4

def sendMessage(mText):
    vk.messages.send(
        random_id=random.randint(0, 1000),
        peer_id=event.message.peer_id,
        message= mText)

# def getShedule():

sess = requests.Session()
vk_sess = vk_api.VkApi(token = 'a8abcdbcdc7d89e63874f81fc073ad056032136abd04998072dbe145bc9033aac43bcd5b0435a53179128')
longpoll = VkBotLongPoll(vk_sess,group_id='192697690')
vk = vk_sess.get_api()
while True:
    try:
        for event in longpoll.listen():
            if event.type == VkBotEventType.MESSAGE_NEW:
                if 'олег' in event.message.text.lower():
                    mText = 'Олег? Это который лох?'
                    sendMessage(mText)
                elif 'понедельник' in event.message.text.lower():
                    mText = ('И до понедельника в коридоре под плинтусами вычистить всю грязь, отодрать краску от пола, вымыть все двери, в сан узле отодрать краску от пола и стен, вымыть пол и стены, чтоб точек не было, вымыть подставки различные , зеркало и за ним, вентиляцию, с/у, раковину, трубы, вычистить грязь за чёрной трубой, починить кран и свет. В воскресенье вечером все вещи из с/у и коридора занести в комнату')
                    sendMessage(mText)
                elif 'коменды' in event.message.text.lower():
                    mText = '89676656512'
                    sendMessage(mText)
                elif 'когда' in event.message.text.lower():
                    mText = 'Через пол часа'
                    sendMessage(mText)
                # elif 'ит1721' in event.message.text.lower():

            # elif event.type == VkBotEventType.MESSAGE_TYPING_STATE:
            #     mText = 'тест'
            #     sendMessage(mText)
    except requests.exceptions.ReadTimeout as timeout:
        continue

