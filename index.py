from colorama import init, Fore, Style

from src.application import Application
from src.log import Log
from src.multi_account import MultiAccount

from src.services.telegram import Telegram

import sys

init()

banner = """
*******************************************************************************
** BOMBCRYPTO - BOT
**
** Please consider buying me a coffee :)
** BCOIN: 0x318863E8f42F4471C1c3FEc59DF2Dd9447F39241
** PIX: 08912d17-47a6-411e-b7ec-ef793203f836
*******************************************************************************
** Press CTRL + C to kill the bot.
** Some configs can be found in the https://github.com/newerton/bombcrypto-bot
*******************************************************************************"""

print(Fore.GREEN + banner + Style.RESET_ALL)

application = Application()
log = Log()
multi_account = MultiAccount()
telegram = Telegram()


def main():  
    application.start()
    telegram.start()
    multi_account.start()


def onlyMap():
    application.start()
    telegram.start()
    multi_account.startOnlyMapAction()


if __name__ == '__main__':
    try:
        print("PLATAFORMAAA" + sys.platform)
        if 'only-map' in sys.argv:
            onlyMap()
        else:
            main()
    except KeyboardInterrupt:
        log.console('Shutting down the bot',
                    services=True, emoji='😓', color='red')
        telegram.stop()
        exit()
