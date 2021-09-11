import subprocess
import os

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
    nick=subprocess.check_output('whoami')
    nick=decoder(nick)
    nome=nick+':'+pwd+'~$ '
    return pwd, nick, nome

pwd, nick, nome = creanome()

while True:
    try:
        damandare=input(str(nome)).strip(' ')
        send(damandare)
    except:
        if damandare=='cd':
            os.chdir('/home/'+nick+'/')
            pwd, nick, nome = creanome()

        if damandare=='cd ..':
            cont=0
            s=''
            while s!='/':
                cont-=1
                s=pwd[cont]
            pwd=pwd[:cont]
            try:
                os.chdir(pwd)
                pwd, nick, nome = creanome()
            except FileNotFoundError:
                print('No such file or directory.')
        try:
            os.system(damandare)
        except:
            print('Wrong command.')
