#!bin/python3

import os

class KillerTool:
    commands_dir = "./commands"
    commands = []


    def __init__(self):
        self.commands = os.listdir(self.commands_dir)
        self.commands.insert(0, "exit")
        self.os_name = os.name
        if not os.path.exists(".history_ip"):
            with open(".history_ip", "w") as f:
                f.write("")

    def displayMenu(self):
        os.system("clear")
        print("Welcome to Killer Tool")
        for id, command in enumerate(self.commands):
            print(f"{id} - {command}")

    def run(self):
        self.displayMenu()
        id_command = int(input("Enter the command number: "))
        if id_command == 0:
            os.system("clear")
            exit(0)
        os.system(f"python3 {self.commands_dir}/{self.commands[id_command]}")
        print("Press enter to continue...")
        input()
        self.run()


if __name__ == "__main__":
    killerTool = KillerTool()
    killerTool.run()

    


