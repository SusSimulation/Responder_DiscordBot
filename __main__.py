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
import Survey
import PenisMeasurement


### MAIN CODE ------------------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    try:
        responder.run(RESPONDERTOKEN)
    except Exception as e:
        print(f"Error: {e}")
        quit()
