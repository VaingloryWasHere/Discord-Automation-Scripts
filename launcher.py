import easygui as easy
import os
import subprocess

DATA = {
    'TOKEN': None,
    'PRIMARY ID':'0', #usually the user/server ID
    'CONTENT':'0',
    'REPEAT':'0'
}

#key: script. value: req args.
#current args: Token, Target ID(user/group/guild), Message, Repeat Times. IN THAT ORDER.
choices = {
    'Group Chat Spammer':['Token','Target ID','Message','Repeat Times'],
    'Server Leaver':['Token'],
    'Unfriender':['Token'],
    'User Spammer':['Token','Target ID','Message','Repeat Times']
}

def token_prompt():
    if os.path.exists('default_info.txt') and open('default_info.txt','r').readline() != None:
        if easy.choicebox("Use default token?",choices=["Yes","No"]) == 'Yes':
            DATA['TOKEN'] = open("default_info.txt", 'r').readline()
            return

    token_prompt = easy.enterbox("Please enter your account token.",'Token needed.')
    if len(token_prompt) < 10:
        easy.msgbox("That appears to be an invalid token. Consult youtube if you do not know to extract your token properly.")
    else:
        DATA['TOKEN'] = token_prompt

def select_script_and_data():
    script = easy.choicebox("Which script would you like to activate?", choices=choices)
    print(script)
    script_requirements = choices[script]
    print(script_requirements)
    for requirement in script_requirements:
            match requirement:
                case 'Token':
                    pass
                case 'Target ID':
                    DATA['PRIMARY ID'] = str(easy.enterbox("Please fill requirement: Target ID"))
                case 'Message':
                    DATA['CONTENT'] = str(easy.enterbox(r"What message should I send? Note: You can use special character \n to denote new lines.")) 
                case 'Repeat Times':
                    DATA['REPEAT'] = str(easy.enterbox(r"How many times should the message be send?"))
                case _:
                    pass
            
    return script

def exec_script(script):
    file_path = f"{script}/main.py"
    creationflags = subprocess.CREATE_NEW_CONSOLE
    subprocess.Popen(["python", file_path, DATA['TOKEN'], DATA['PRIMARY ID'], DATA['CONTENT'], DATA['REPEAT']], creationflags=creationflags)
def launcher():
    while DATA['TOKEN'] == None:
        token_prompt()  
    script = select_script_and_data()
    exec_script(script)

running = True
while running == True:
    launcher()
    running = False if easy.buttonbox("Script has been launched in a new shell window, and will work in the background. Exit Launcher, or continue to menu?",choices=['Exit','Continue']) == 'Exit' else True 