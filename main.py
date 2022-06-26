import subprocess, shutil

def git_updater():
    shutil.copyfile("me-pican-los-cocos/data/updater.py", "updater.py")
    subprocess.Popen("powershell python updater.py", creationflags=subprocess.CREATE_NEW_CONSOLE)

git_updater()