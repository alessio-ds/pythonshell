import subprocess
import os

class bcolors:
    cnick = '\033[92m' #GREEN
    cdir = '\033[94m' #BLUE
    reset = '\033[0m' #RESET COLOR

def decoder(inp):
    out=bytes.decode(inp)
    out=out.strip('\n')
    return out

def scrivi(testo):
    inp=subprocess.check_output(testo)
    print(decoder(inp))

def send(lolz):
    scrivi(lolz)

def creanome():
    pwd=subprocess.check_output('pwd')
    pwd=decoder(pwd)
    #if pwd=='/home/alessiosca':
    if pwd=='/':
        pwd2=bcolors.cdir+'~'+bcolors.reset
    else:
        pwd2=bcolors.cdir+pwd+bcolors.reset
    nick=subprocess.check_output('whoami')
    nick=decoder(nick)
    nick=nick
    nome=bcolors.cnick+nick+'@pythonshell'+bcolors.reset+':'+pwd2+'$ '
    return pwd, nick, nome

pwd, nick, nome = creanome()

while True:
    try:
        damandare=input(str(nome)).strip(' ')
        send(damandare)
    except KeyboardInterrupt:
        print('\nExiting from pythonshell')
        exit()
    except:
        if damandare=='cd' or damandare=='cd /':
            #os.chdir('/home/'+nick+'/')
            os.chdir('/')
            pwd, nick, nome = creanome()

        if damandare=='cd ..':
            cont=0
            s=''
            if pwd.count('/')==1:
                os.chdir('/')
                pwd, nick, nome = creanome()
            else:
                while s!='/':
                    cont-=1
                    s=pwd[cont]
                pwd=pwd[:cont]
                try:
                    os.chdir(pwd)
                    pwd, nick, nome = creanome()
                except FileNotFoundError:
                    print('No such file or directory.')
        if 'cd' in damandare and damandare!='cd' and damandare!='cd ..':
            damandare2=damandare.strip('cd ')
            damandare2=pwd+'/'+damandare2
            #print(damandare2)
            try:
                os.chdir(damandare2)
                pwd, nick, nome = creanome()
            except FileNotFoundError:
                print('No such file or directory.')

        try:
            if 'cd' in damandare:
                pass
            else:
                os.system(damandare)
        except:
            print('Wrong command.')
