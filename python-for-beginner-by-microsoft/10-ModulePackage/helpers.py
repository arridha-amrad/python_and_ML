from pip._vendor.colorama import init, Fore
init()


def display(message, warning=False):
    if warning:
        print(Fore.RED + "waning : " + message)
    else:
        print(Fore.GREEN + "Not a warning message : " + message)
