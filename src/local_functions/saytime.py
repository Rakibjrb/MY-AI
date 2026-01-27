import time
import datetime
import random
from speak_and_listen.speak import speak

def saytime():
    current_time = time.localtime() # get current time
    formatted_time = time.strftime('%I:%M %p', current_time)
    return formatted_time

def wish_me():
    hour = int(datetime.datetime.now().hour) # get current hour
    
    morning_options = [
        "Good morning Rakibul! I hope you have a productive morning.",
        "Morning Rakibul! The system is fully operational and ready for your commands.",
        "Good morning! A fresh start to a new day. How can I help you, Rakibul?",
        "Rise and shine Rakibul! I am online and waiting for your instructions."
    ]

    afternoon_options = [
        "Good afternoon Rakibul! Have you had your lunch yet?",
        "Good afternoon! I hope your day is going well so far.",
        "Afternoon Rakibul! I'm here if you need any assistance with your tasks.",
        "Hello Rakibul! It's a bright afternoon. What's on your mind?"
    ]

    evening_options = [
        "Good evening Rakibul! How can I assist you this evening?",
        "Evening Rakibul! The weather seems nice. Ready to wrap up some work?",
        "Good evening! I am at your service. What do you need, Rakibul?",
        "Hello Rakibul! Hope you're having a relaxing evening."
    ]

    night_options = [
        "Good night Rakibul! It's getting late, you should get some rest soon.",
        "Night Rakibul! Don't work too hard, remember to sleep well.",
        "Good night! I'll be here if you need anything before you go to bed.",
        "It's late, Rakibul. System is in standby mode, but I am still listening for you."
    ]

    night_options = [
        "Good night Rakibul! It's getting late, you should get some rest soon.",
        "Night Rakibul! Don't work too hard, remember to sleep well.",
        "Good night! I'll be here if you need anything before you go to bed.",
        "It's late, Rakibul. System is in standby mode, but I am still listening for you."
    ]

    wish_text = "Nothing for wish"

    if hour >= 5 and hour < 12:
        wish_text = random.choice(morning_options)
    elif hour >= 12 and hour < 17:
        wish_text = random.choice(afternoon_options)
    elif hour >= 17 and hour < 21:
        wish_text = random.choice(evening_options)
    else:
        wish_text = random.choice(night_options)
    
    speak(wish_text)