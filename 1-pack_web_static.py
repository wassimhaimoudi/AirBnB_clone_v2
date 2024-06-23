#!/usr/bin/python3
"""This script generates .tgz archive from the content of web_static
"""
from fabric.api import *
from datetime import datetime as dt
from os import path


def do_pack():
    """Creates and packs web_static
       content to a tarball in the versions folder
    """
    local("mkdir -p versions")
    dt_now = dt.now()
    dt_frmt = "%Y%m%d%H%M%S"
    dt_str = dt_now.strftime(dt_frmt)
    tarball_path = f"versions/web_static_{dt_str}.tgz"
    result = local(f"tar -cvzf {tarball_path} web_static", capture=True)

    if result.failed:
        return
    if path.exists(tarball_path):
        return tarball_path
    return
