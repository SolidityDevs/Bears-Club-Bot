from telegram.ext.dispatcher import run_async
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext, Filters
from pricebot.ads import get_current_add as myads


import json
import random

def quote_message(update, context):
    # content by https://www.daniel-wong.com/2015/10/05/study-motivation-quotes/
    quotes = ["Believe you can and you’re halfway there.", "You have to expect things of yourself before you can do them.",
              "It always seems impossible until it’s done.", "Don’t let what you cannot do interfere with what you can do. – John Wooden",
              "Start where you are. Use what you have. Do what you can. – Arthur Ashe", "Successful and unsuccessful people do not vary greatly in their abilities.",
              "They vary in their desires to reach their potential. – John Maxwell", "The secret of success is to do the common things uncommonly well. – John D. Rockefeller",
              "Good things come to people who wait, but better things come to those who go out and get them.", "Strive for progress, not perfection.",
              "I find that the harder I work, the more luck I seem to have. – Thomas Jefferson", "Success is the sum of small efforts, repeated day in and day out. – Robert Collier",
              "Don’t wish it were easier; wish you were better. – Jim Rohn",
              "I don’t regret the things I’ve done. I regret the things I didn’t do when I had the chance.",
              "There are two kinds of people in this world: those who want to get things done and those who don’t want to make mistakes. – John Maxwell",
              "The secret to getting ahead is getting started.", "You don’t have to be great to start, but you have to start to be great.",
              "The expert in everything was once a beginner.", "There are no shortcuts to any place worth going. – Beverly Sills",
              "Push yourself, because no one else is going to do it for you.", "Some people dream of accomplishing great things. Others stay awake and make it happen.",
              "There is no substitute for hard work. – Thomas Edison", "The difference between ordinary and extraordinary is that little “extra.”",
              "You don’t always get what you wish for; you get what you work for.", "It’s not about how bad you want it. It’s about how hard you’re willing to work for it.",
              "The only place where success comes before work is in the dictionary. – Vidal Sassoon", "There are no traffic jams on the extra mile. – Zig Ziglar",
              "If people only knew how hard I’ve worked to gain my mastery, it wouldn’t seem so wonderful at all. – Michelangelo",
              "“All our dreams can come true, if we have the courage to pursue them.” – Walt Disney.",
              "Success is not final, failure is not fatal: it is the courage to continue that counts.",
              "If it’s important to you, you’ll find a way. If not, you’ll find an excuse.", "Don’t say you don’t have enough time. You have exactly the same number of hours per day that were given to Helen Keller, Pasteur, Michelangelo, Mother Teresea, Leonardo da Vinci, Thomas Jefferson, and Albert Einstein. – H. Jackson Brown Jr.",
              "Challenges are what make life interesting. Overcoming them is what makes life meaningful. – Joshua J. Marine",
              "Life has two rules: 1) Never quit. 2) Always remember Rule #1.", "I’ve failed over and over and over again in my life. And that is why I succeed. – Michael Jordan",
              "I don’t measure a man’s success by how high he climbs, but how high he bounces when he hits the bottom. – George S. Patton",
              "If you’re going through hell, keep going. – Winston Churchill", "Don’t let your victories go to your head, or your failures go to your heart.",
              "Failure is the opportunity to begin again more intelligently. – Henry Ford",
              "Believe you can and you're halfway there.",
              "Strive for progress, not perfection",
              "Dream don't work unless you do",
              "Never let your fear decide your future.",
              "You don’t drown by falling in the water; you drown by staying there. – Ed Cole", "The difference between a stumbling block and a stepping-stone is how high you raise your foot.",
              "The pain you feel today is the strength you will feel tomorrow. For every challenge encountered there is opportunity for growth.",
              "“Be like a diamond, precious and rare, not like a stone, found everywhere.” Anonymous",
              "It’s not going to be easy, but it’s going to be worth it."]
    length = len(quotes)
    randomIndex = random.randint(0, length - 1)
    update.message.reply_text('`'+ quotes[randomIndex] +'`\n' + myads(),parse_mode='markdown', disable_web_page_preview=True)
