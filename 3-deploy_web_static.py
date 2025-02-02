#!/usr/bin/python3
""" Compressing a fabric file"""

from fabric.api import *
from datetime import datetime
import os.path

env.hosts = ['35.231.1.112', '54.167.91.234']


def deploy():
    """ deploys dopack to archive"""
    archive = do_pack()
    if archive is None:
        return False

    status = do_deploy(archive)

    return status


def do_deploy(archive_path):
    """deploy to web-server"""

    if not os.path.exists(archive_path):
        return False

    try:
        archiveName = archive_path[9:]
        archiveNameWithoutExtension = archiveName[:-4]
        put(archive_path, '/tmp/' + archiveName)
        run("mkdir -p /data/web_static/releases/" +
            archiveNameWithoutExtension)
        # no space after /tmp/ add a space before -c
        run('tar -xzvf /tmp/' + archiveName +
            " -C /data/web_static/releases/" +
            archiveNameWithoutExtension + " --strip-components=1")
        run("rm -rf /tmp/" + archiveName)
        run("rm -rf /data/web_static/current")
        run("sudo ln -sf /data/web_static/releases/" +
            archiveNameWithoutExtension + " /data/web_static/current")

        return True
    except:
        return False


def do_pack():
    """ Pack up our web_static """

    try:
        now = datetime.now()

        tarArchiveName = "web_static_" + now.strftime("%Y%m%d%H%M%S") + ".tgz"
        tarArchivePath = "versions/" + tarArchiveName

        local("mkdir -p versions")

        local("tar -czvf " + tarArchivePath + " web_static")

        return tarArchivePath
    except:
        return None
