import time
import random
import datetime
import RPi.GPIO as GPIO
import telepot
from telepot.loop import MessageLoop

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

led = 16

GPIO.setup(led, GPIO.OUT)

def LedOn(val):
    GPIO.output(led,1)
    time.sleep(val)
    GPIO.output(led,0)

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    print 'Got command: %s' % command

    if command == '/On':
        #bot.sendMessage(chat_id, random.randint(1,6))
        #LedOn(5)
        GPIO.output(led,1)
    elif command == '/Off':
        #bot.sendMessage(chat_id, str(datetime.datetime.now()))
        GPIO.output(led,0)

bot = telepot.Bot('token')

MessageLoop(bot, handle).run_as_thread()
print 'I am listening ...'

while 1:
    time.sleep(10)
