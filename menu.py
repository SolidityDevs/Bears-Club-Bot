from telegram.ext import *
from telegram import *
import random
from pricebot.ads import get_current_add as myads

HELLO = [
    "`Hi !`",
    "`‘Ello, gov'nor!`",
    "`What’s crackin’?`",
    "`‘Sup, homeslice?`",
    "`Howdy, howdy ,howdy!`",
    "`Hello, who's there, I'm talking.`",
    "`You know who this is.`",
    "`Yo!`",
    "`Whaddup.`",
    "`Greetings and salutations!`",
    "`Hello, sunshine!`",
    "`Hey, howdy, hi!`",
    "`What’s kickin’, little chicken?`",
    "`Peek-a-boo!`",
    "`Howdy-doody!`",
    "`Hey there, freshman!`",
    "`I come in peace!`",
    "`Ahoy, matey!`",
    "`Hiya!`",
    "`Oh gey! Well Hello`",
    "`Hello please add me to your group`",
    "`Hey hope you okay`",
    "`Am active!`",
    "`Hello.`",
    "`God was searching for you. You should leave to meet him.`",
    "`You should Volunteer for target in an firing range.`",
    "`Try playing catch and throw with RDX its fun.`",
    "`What language are you speaking? Cause it sounds like ....`",
    "`You are proof that evolution CAN go in reverse.`",
    "`I would ask you how old you are but I know you can't count that high.`",
    "`As an outsider, what do you think of the human race?`",
    "`Ordinarily people live and learn.`",
    "`Keep talking, someday you'll say something intelligent!.......`"
]
def menu(update,context):
    length = len(HELLO)
    randomIndex = random.randint(0, length - 1)
    update.message.reply_text('`'+ HELLO[randomIndex] +'`\n'+ myads(),parse_mode='markdown', disable_web_page_preview=True)
    
