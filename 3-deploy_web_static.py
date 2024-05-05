#!/usr/bin/python3
"""Fab file for generating and distributing an archive to web servers """


from datetime import datetime
from fabric.api import local, put, sudo, sudo, env, settings
from os import makedirs, path


env.hosts = ["54.152.132.40", "34.204.81.107"]
env.user = "ubuntu"


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
    print(f"Packing web_static to versions/{file_name}")
    status = local(f"tar -cvzf versions/{file_name} web_static")

    if status.failed:
        return None
    print(f"web_static packed: {file_name} -> \
{path.getsize('versions/' + file_name)}Bytes")
    return file_name


def do_deploy(archive_path):
    """
    Deploys an archive to the web servers.

    Args:
        archive_path (str): Path to the archive to be deployed.

    Returns:
        bool: True if deployment is successful, False otherwise.
    """
    if not path.exists(archive_path):
        return False

    file_name = path.basename(archive_path)
    file = path.splitext(file_name)[0].strip()
    release_folder = f"/data/web_static/releases/{file}/"

    if put(archive_path, "/tmp/", use_sudo=True).failed:
        return False
    if sudo(f"mkdir -p {release_folder}").failed:
        return False
    if sudo(f"tar -xzf /tmp/{file_name} -C {release_folder}").failed:
        return False
    if sudo(f"rm -rf /tmp/{file_name}").failed:
        return False
    if sudo(f"mv  {release_folder}web_static/* {release_folder}").failed:
        return False
    if sudo(f"rm -rf {release_folder}web_static/").failed:
        return False
    if sudo(f"rm -rf /data/web_static/current").failed:
        return False
    if sudo(f"ln -s {release_folder} /data/web_static/current").failed:
        return False
    print("New version deployed!")
    return True


def deploy():
    # Local Stage: Run do_pack locally
    path_name = do_pack()
    if not path_name:
        return False

    # Remote Stage: Execute do_deploy on each server
    return do_deploy(path_name)


if __name__ == "__main__":

    do_deploy()