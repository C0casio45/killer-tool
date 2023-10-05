import os

os.system("clear")

match os.name:
    case "nt":
        os.system("ipconfig")
    case "posix":
        os.system("ip a")
    case _:
        print("Your OS is not supported")
        exit(1)

