#!/usr/bin/python3
""" Compressing a fabric file"""


from fabric.api import local
from datetime import datetime


def do_pack():
    """ pack up out web_static directory """

try:
    now = datetime.now()
    tarArchiveName = "web_static_" + now.strftime("%Y%m%d%H%M%S") + ".tgz"
    tarArchivePath = "versions/" + tarArchiveName
    local("sudo mkdir -p versions")
    local("tar -czvf " + tarArchivePath + " web_static")
    return tarArchivePath
except:
    return None
