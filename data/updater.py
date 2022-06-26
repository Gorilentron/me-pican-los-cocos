from colorama import Fore, init
import subprocess, time, os
init()

def run(cmd):
    return subprocess.run(["powershell", *cmd.split(' ')], capture_output=True).stdout

process = run("cd me-pican-los-cocos; git pull")

if 'changed' in str(process): print(Fore.LIGHTGREEN_EX + f"[{Fore.LIGHTWHITE_EX}·{Fore.LIGHTGREEN_EX}] Updated" + Fore.RESET)
elif "Already up to date" in str(process): print(Fore.LIGHTYELLOW_EX + f"[{Fore.LIGHTWHITE_EX}·{Fore.LIGHTYELLOW_EX}] Already up to date" + Fore.RESET)
else: print(Fore.LIGHTRED_EX + f"[{Fore.LIGHTWHITE_EX}·{Fore.LIGHTRED_EX}] Not a git repository" + Fore.RESET)
time.sleep(2)

if os.path.isfile("updater.py"):
    os.remove("updater.py")