from nltk.tokenize import RegexpTokenizer
from nltk import pos_tag
from nltk import RegexpParser
from nltk.chat.util import Chat, reflections
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
import os

#Bot named after Marty McFly, change if necessary
bot = ChatBot("McFly")

#Training
trainer = ListTrainer(bot)
trainer.train("chatterbot.corpus.english")

for files in os.listdir("./english/"):
    data = open("./english/" + files, "r").readlines()
    trainer.train(data)

#Chat feature
while True:
    message = input("\t\t\tYou:")
    if message.strip()!= "Bye":
        reply = bot.get_response(message)
        print("McFly:", reply)
    if message.strip() == "Bye":
        print("McFly: Bye")
        break
