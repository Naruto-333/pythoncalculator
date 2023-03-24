from colorama import Fore, Back, Style
x = input(Fore.WHITE + 'Input first num')
y = input(Fore.WHITE + 'Input seccond num')
symbol = input(Fore.WHITE + 'Input the operation you want to do')
def calculate():
    if symbol == '+':
        print(Fore.WHITE + int(x) + int(y))
    elif symbol == '-':
        print(Fore.White + int(x) - int(y))
    elif symbol == 'x':
        print(Fore.WHITE + int(x) * int(y))
    elif symbol == '/':
        print(Fore.White + int(x) / int(y))
    elif symbol == '^':
        print(Fore.WHITE + int(x) ** int(y))
    else:
        print(Fore.RED + 'ERROR - DID NOT INPUT A VALID OPERATION')
calculate()
print(Fore.WHITE + 'Reload the program for more calculations')