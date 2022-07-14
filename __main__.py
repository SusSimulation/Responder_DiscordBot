from __module import *
import AddAdmin
import OnReady
import ErrorFilter
import Help
import Reboot
import Quit
import Files
import Servers
import Info
import TrustIssues
import Photo_and_Add
import BlackJack
import Quote
import EightBall
import RPS
import PenisMeasurement
import Zelda
import Hen
import Survey

### MAIN CODE ------------------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    try:
        responder.run(RESPONDERTOKEN)
    except Exception as e:
        print(f"Error on boot: {e.__class__.__name__}: {e}")
        quit()
