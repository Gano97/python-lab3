from telegram.ext import Filters, CommandHandler, MessageHandler, Updater
from telegram import ChatAction
from gtts import gTTS

import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger= logging.getLogger(__name__)

def start(bot, update):
    update.message.reply_text("Bot started. The use of this bot is related to his physical machine.")
    from sys import argv
    fp = argv[1]
    txt = open(fp)
    for strng in txt.read().splitlines():
        task.append(strng)
    txt.close()

def echo(bot, update):
    update.message.reply_text("This bot accepts only commands. Messages will be ignored.")

def showTask(bot, update):
    if(len(task)<=0):
        update.message.reply_text("No tasks in memory. Nothing to do now.")
    else:
        l2= list(task)
        update.message.reply_text(sorted(l2))
        del l2[:]

def newTask(bot, update, args):
    strng= ""
    i= 0
    for s in args:
        strng= strng + s
        if i!= (len(args)-1):
            strng+= " "
        i+=1
    task.append(strng)

def removeTask(bot, update, args):
    if (len(task) <= 0):
        update.message.reply_text("No tasks in memory. Nothing to do now.")
    else:
        strng = ""
        i= 0
        for s in args:
            strng = strng + s
            if i!= (len(args)-1):
                strng+= " "
            i+=1
        task.remove(strng)

def removeAllTasks(bot, update, args):
    if (len(task) <= 0):
        update.message.reply_text("No tasks in memory. Nothing to do now.")
    else:
        ctrl = ""
        i= 0
        for s in args:
            ctrl = ctrl + s
            if i!= (len(args)-1):
                ctrl+= " "
            i+=1
        for strng in task:
            if ctrl in strng:
                task.remove(strng)

def main():
    bot_updater= Updater("633860381:AAE4lOKbl5w4JpUGeYW9WMMMM2vn2rZuyxM") #collegamento al bot
    bot_dispatcher= bot_updater.dispatcher #registro degli handler

    bot_dispatcher.add_handler(CommandHandler("start", start))
    bot_dispatcher.add_handler(MessageHandler(Filters.text, echo))
    bot_dispatcher.add_handler(CommandHandler("showTask", showTask))
    bot_dispatcher.add_handler(CommandHandler("newTask", newTask, pass_args=True))
    bot_dispatcher.add_handler(CommandHandler("removeTask", removeTask, pass_args=True))
    bot_dispatcher.add_handler(CommandHandler("removeAllTasks", removeAllTasks, pass_args=True))

    bot_updater.start_polling() #start the bot itself

    bot_updater.idle() #run the bot until the user press CTRL+C (sending a SIGINT, SIGABRT, ...) stopping the bot

if (__name__ == "__main__"):
    task = []
    main()