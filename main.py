from colorama import Fore, init
import subprocess
init()

def run(cmd):
    txt = f"powershell {cmd}"
    return subprocess.run(txt, capture_output=True)

def git_update():
    process = run("git reset --hard HEAD; git clean -d -f; git pull")
    print(str(process))

    if 'changed' in str(process): print(Fore.LIGHTGREEN_EX + f"[{Fore.LIGHTWHITE_EX}·{Fore.LIGHTGREEN_EX}] Updated" + Fore.RESET)
    elif "Already up to date" in str(process): print(Fore.LIGHTYELLOW_EX + f"[{Fore.LIGHTWHITE_EX}·{Fore.LIGHTYELLOW_EX}] Already up to date" + Fore.RESET)
    else: print(Fore.LIGHTRED_EX + f"[{Fore.LIGHTWHITE_EX}·{Fore.LIGHTRED_EX}] Not a git repository" + Fore.RESET)

def git_check():
    # process = run("git pull --rebase")
    # print(process.stderr)
    git_update()

git_check()
