import subprocess as sp
import re

# list of pkg managers for each terminal ({os:{pkgm:{"search":"search_cmd", "install":"install_cmd", "uninstall":"uninstall_cmd"}})
PKGMS = {
    "windows":
        {
        "winget":
        {
            "installer": "winget install {}",
            "search": "winget search {}",
            "is_there": "winget",
            "end": ""
        },
        "choco":
        {
            "installer": "choco install {}",
            "search": "choco search {}",
            "is_there": "choco",
            "end": ""
        },
        "scoop":
        {
            "installer": "scoop install {}",
            "search": "scoop search {}",
            "is_there": "scoop",
            "end": ""

        },
        "oneget":
        {
            "installer": "Install-Package {} -ProviderName Chocolatey",
            "search": "Find-Package {}",
            "is_there": "",
            "end": ""

        },
        "npackd":
        {
            "installer": "npacked-cli install {}",
            "search": "npackd-cli search {}",
            "is_there": "npacked-cli",
            "end": ""

        },
        "----":
        {
            "installer": "...",
            "search": "...",
            "is_there": "...",
            "end": "",

        }
    },
    "lin-x":{}
}

##########################
LOG = True
FALLI = ["no"]
PATT = r"\b(" + "|".join(FALLI) + r")\b"
##########################
def red(str_): return f"\033[31m{str_}\033[0m"
def green(str_): return f"\033[32m{str_}\033[0m"
def yellow(str_): return f"\033[33m{str_}\033[0m"
def blue(str_): return f"\033[34m{str_}\033[0m"
#########################

def log_(logg, is_err=True):
    if LOG:
        if is_err:
            print(f"[{yellow('log')}]({error_(logg)})")
        else:
            print(f"[{yellow('log')}]({logg})")

def error_(err):
    tmpl = f"[{red('error')}]: "
    tmpl += "{}"
    if err:
        tmpl = tmpl.format(err)
    else:
        tmpl = tmpl.format("err not found")

    return tmpl

def oll(os_, pkg):
    if os_ not in PKGMS:
        log_("os not found/implemented")
        # err
        return 1
    aval_pkgms = []
    for n,i in PKGMS[os_].items():
        # check if the pkgm is installed
        resp = sp.run(
            [i["is_there"]],
            capture_output=True,
            text=True,
            shell=True
        )
        if resp.stderr:
            log_(f"{n} not found")
            continue
        aval_pkgms.append(n)
    print(f"{blue('available pkgms')}: {green(aval_pkgms)}")
    aval_in = []
    for i in aval_pkgms:
        resp = sp.run(
            (PKGMS[os_][i]["search"].format(pkg)).split(' '),
            shell=True,
            capture_output=True,
            text=True,
            encoding="utf-8"
        )
        out_ = resp.stdout
        end_ = 40
        # find the first \n or none
        I_out_ = out_.find('\n')
        if I_out_ != -1:
            end_ = I_out_
        if re.search(PATT, out_[:end_], re.IGNORECASE):
            print(f"[{i}]: \U0000274C")
            continue
        aval_in.append(i)
    if len(aval_in) < 1:
        print(error_("Package Not found"))
        return 1
    print(f"[------{green('found')}------]")
    for i in aval_in:
        print(f"[{i}]: \u2705")



oss = "windows" #input("enter os name: ")
pkgg = input("enter pkg name: ")
oll(oss, pkgg)
