import hexahack as hexa
import cmd
import os
from termcolor import colored

def icon():
    print(colored("""
 __    __                                __    __                      __       
/  |  /  |                              /  |  /  |                    /  |      
$$ |  $$ |  ______   __    __   ______  $$ |  $$ |  ______    _______ $$ |   __ 
$$ |__$$ | /      \ /  \  /  | /      \ $$ |__$$ | /      \  /       |$$ |  /  |
$$    $$ |/$$$$$$  |$$  \/$$/  $$$$$$  |$$    $$ | $$$$$$  |/$$$$$$$/ $$ |_/$$/ 
$$$$$$$$ |$$    $$ | $$  $$<   /    $$ |$$$$$$$$ | /    $$ |$$ |      $$   $$<  
$$ |  $$ |$$$$$$$$/  /$$$$  \ /$$$$$$$ |$$ |  $$ |/$$$$$$$ |$$ \_____ $$$$$$  \ 
$$ |  $$ |$$       |/$$/ $$  |$$    $$ |$$ |  $$ |$$    $$ |$$       |$$ | $$  |
$$/   $$/  $$$$$$$/ $$/   $$/  $$$$$$$/ $$/   $$/  $$$$$$$/  $$$$$$$/ $$/   $$/ 
""", 'cyan'))  

class HexaHackCMD(cmd.Cmd):
    intro = colored('Welcome to the HexaHack command line interface. Type help or ? to list commands.\n', 'green')
    prompt = colored('(hexahack) ', 'yellow')

    def __init__(self):
        icon()  # Print the icon on start
        super().__init__()
        self.username = input(colored("Enter your username: ", 'blue'))
        self.user_id = int(input(colored("Enter your user ID: ", 'blue')))

    def preloop(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        super().preloop()

    def precmd(self, line):
        os.system('cls' if os.name == 'nt' else 'clear')
        icon()  # Print the icon on every command
        return line

    def parse_args(self, arg, expected_args):
        args = arg.split()
        if len(args) != expected_args:
            print(colored(f"Invalid number of arguments. Usage required: {expected_args} arguments.", 'red'))
            return None
        return args
                                                                     
                                                                                
                                                                                
    def do_create_account(self, arg):
        'Create a new user account: create_account fullname referer_id'
        args = self.parse_args(arg, 2)
        if args:
            fullname, referer_id = args[0], int(args[1])
            success = hexa.create_account(self.user_id, fullname, self.username, referer_id)
            print(colored("Account creation successful", 'green') if success else colored("Account creation failed", 'red'))

    def do_available_taps(self, arg):
        'Check available taps for a user: available_taps'
        taps = hexa.available_taps(self.username, self.user_id)
        print(colored(f"Available taps: {taps}", 'blue'))

    def do_mine_all(self, arg):
        'Execute mining for all available taps: mine_all'
        success = hexa.mineall(self.username, self.user_id)
        print(colored("Mining successful", 'green') if success else colored("Mining failed", 'red'))

    def do_get_balance(self, arg):
        'Get the balance of a user: get_balance'
        balance = hexa.get_balance(self.username, self.user_id)
        print(colored(f"Balance: {balance}", 'blue'))

    def do_exit(self, arg):
        'Exit the command line interface'
        print(colored("Exiting HexaHack CLI", 'yellow'))
        return True

if __name__ == '__main__':
    HexaHackCMD().cmdloop()
