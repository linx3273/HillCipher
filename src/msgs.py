import colorama
from colorama import Fore


colorama.init(autoreset=True) # autoreset so that the color remains green only for that print line

# when an error has occured
def errmsg(val,e='\n',s=' '):
    print("[" + Fore.RED + "ERR" + Fore.RESET + "]",end=' ')
    print(val,end=e,sep=s)

# when input is required in the current line
def inpmsg(val):
    print("[" + Fore.YELLOW + "INP" + Fore.RESET + "]",end=' ')
    return input(val)

# default info message
def msg(val,e='\n',s=' '):
    print("[" + Fore.GREEN + "INF" + Fore.RESET + "]",end=' ')
    print(val,end=e,sep=s)