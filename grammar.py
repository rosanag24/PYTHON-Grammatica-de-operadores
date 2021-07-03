import re


def init(entrada):
    pattern = '[A-Z]+$'
    if not(re.match(pattern, entrada)):
        print ("ERROR: \"%s\" no es un sı́mbolo no-terminal",entrada)

def rule(entrada):
    pattern = '([A-Z]*) ([^A-Z$]* [A-Z]*)*'
    if not(re.match(pattern, entrada)):
        print ("ERROR: Regla \"%s\" no corresponde a una gramática de operadores",entrada)  

def get_input():
    input_rule = input("$> ")
    return input_rule

def valid_command(grammar, input):
    if ():
        print ("valid")
    else:
        print("not valid")

#----------------------MAIN----------------------#        
def main():
    entrada = get_input()

    COMMANDS = ['RULE',"INIT","PREC","BUILD","PARSE","EXIT"]
    tokens = entrada.split(" ",2)
    print(tokens)

    if not(tokens[0] in COMMANDS):
        print ("Invalid command %s", tokens[0])

main()