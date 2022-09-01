import ErrorFilter
import OnReady
from __module import *
from Admin_controls import AdminControls
from ExportPhotos import PostAndSaves
from Help import Help
from Info import Info
from ServerInfos import ServerInfo  # with a sub-command $channelinfo
from TrustIssues import TrustIssuesGame
from Extra import StupidExtraStuff

### MAIN CODE ------------------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    try:
        responder.add_cog(StupidExtraStuff(responder))
        responder.add_cog(PostAndSaves(responder))
        responder.add_cog(TrustIssuesGame(responder))
        responder.add_cog(AdminControls(responder))
        responder.add_cog(Info(responder))
        responder.add_cog(Help(responder))
        responder.add_cog(ServerInfo(responder))
        responder.run(RESPONDERTOKEN)
    except Exception as e:
        print(f"Error on boot: {e.__class__.__name__}: {e}")
        quit()
