#!/usr/bin/python3
"""Fab file for generating arhived file of webstatic directory"""


from datetime import datetime
from fabric.api import local, env
from os import makedirs


def generate_archive_name():
    """
    Generates a unique name for the archive based on the current date and time.

    Returns:
        str: The name of the archive.
    """
    now = datetime.now()
    return f"web_static_{now.strftime('%Y%m%d%H%M%S')}.tgz"


def do_pack():
    """
    Creates a .tgz archive from the contents of the web_static directory.

    Returns:
        str: The name of the archive on success, None if failed.
    """
    file_name = generate_archive_name()
    makedirs("versions", exist_ok=True)
    status = local(f"tar -cvzf versions/{file_name} web_static")

    if status.failed:
        return None
    return file_name
