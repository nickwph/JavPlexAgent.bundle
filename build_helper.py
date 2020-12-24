import os

import psutil

PROCNAME = "Plex Media Server"

for proc in psutil.process_iter():
    # print proc.name()
    # check whether the process name matches
    if proc.name() == "Plex Media Server":
        print "kililing now"
        proc.kill()
        print "done"

print "starting"
os.system("open  /Applications/Plex\ Media\ Server.app")

print "started"