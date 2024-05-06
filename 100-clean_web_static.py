#!/usr/bin/python3
"""Fab file for generating and distributing an archive to web servers """


from datetime import datetime
from fabric.api import local, put, sudo, sudo, env, task, runs_once, lcd, cd
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


@task
@runs_once
def do_pack():
    """
    Creates a .tgz archive from the contents of the web_static directory.

    Returns:
        str: The name of the archive on success, None if failed.
    """
    file_name = generate_archive_name()
    makedirs("versions", exist_ok=True)
    print(f"Packing web_static to versions/{file_name}")
    status = local(f"tar -czvf versions/{file_name} web_static")

    if status.failed:
        return None
    print(f"web_static packed: versions/{file_name} -> \
{path.getsize('versions/' + file_name)}Bytes")
    return f"versions/{file_name}"


@task
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


@task
def deploy():
    """
    Deploys the archive to the specified web servers.

    Returns:
        bool: True if deployment is successful to all servers, False otherwise.
    """
    # Local Stage: Run do_pack locally
    archive_path = do_pack()
    if not archive_path:
        return False

    # Remote Stage: Execute do_deploy on each server
    return do_deploy(archive_path)


@task
@runs_once
def do_clean_local(number=0):
    """
    Cleans up local versions directory by deleting old archives except
    the latest ones.

    Args:
        number (int or str, optional): Number of latest archives to keep.
        Defaults to 0, meaning only the latest archive is kept.

    Returns:
        None
    """
    # Determine the number of archives to keep
    keep = int(number) + 1
    if number == "0" or number == "1":
        keep = 2

    # Change directory to versions/
    with lcd("versions/"):
        # List files sorted by modification time and delete old
        # archives except the latest ones
        local(f"ls -1t | tail -n +{keep} | xargs rm -rf")


@task
def do_clean_server(number=0):
    """
    Cleans up server releases directory by deleting old releases
    except the latest ones.

    Args:
        number (int or str, optional): Number of latest releases
        to keep. Defaults to 0, meaning only the latest release is kept.

    Returns:
        None
    """
    # Determine the number of releases to keep
    keep = int(number) + 1
    if number == "0" or number == "1":
        keep = 2

    # Change directory to /data/web_static/releases/
    with cd("/data/web_static/releases/"):
        # List directories sorted by modification time and delete
        # old releases except the latest ones
        sudo(f"ls -1t | tail -n +{keep} | xargs rm -rf")


@task
def do_clean(number=0):
    """
    Cleans up local and server directories by deleting old
    archives/releases except the latest ones.

    Args:
        number (int or str, optional): Number of latest archives/releases
        to keep. Defaults to 0, meaning only the latest archive/release
        is kept.

    Returns:
        None
    """
    # Perform cleanup on both local and server directories
    do_clean_local(number)
    do_clean_server(number)


if __name__ == "__main__":

    do_clean()
