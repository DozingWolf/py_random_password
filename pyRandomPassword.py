from random import choice
from sys import argv,exit
from getopt import getopt,GetoptError
from pyperclip import copy

def showVersion():
    msg = 'Ver.0.0.3'
    print(msg)

def helpMsg():
    msg = '''
    ==============********===============
    ===========create by csy=============
    =============2022/10/8===============
    ==============********===============
    This cli tool is a password generator. When generator success it will automatic copy password to clipboard and show in cli window.
    parameter list:
    -h/--help ==> list help message
    -p/--length ==> input password length
    -l/--level ==> input password strength
    -v/--version ==> show version

    password strength level:
    l1:Level_1 , only number
    l2:Level_2 , number + letter
    l3:Level_3 , number + letter + capital letter
    l4:Level_4 , number + letter + capital letter + !$%&_=+
    l5:Level_5 , number + letter + capital letter + !$%&_=+ all object must exist 
    ===================================
    ======wish u have a good time======
    ===================================
    '''
    print(msg)

def randomPassword(plength:int,level:int):
    pwList = []
    # password letter length must in [4,18]
    # password level:
    # level 1 : 12345678 only number
    l1 = ['0','1','2','3','4','5','6','7','8','9']
    # level 2 : 123456+abcdef number and letter
    l2 = ['0','1','2','3','4','5','6','7','8','9',
          'a','b','c','d','e','f','g','h','i','j',
          'k','l','m','n','o','p','q','r','s','t',
          'u','v','w','x','y','z']
    # level 3 : 123+abc+ABC capital letter
    l3 = ['0','1','2','3','4','5','6','7','8','9',
          'a','b','c','d','e','f','g','h','i','j',
          'k','l','m','n','o','p','q','r','s','t',
          'u','v','w','x','y','z',
          'A','B','C','D','E','F','G','H','I','J',
          'K','L','M','N','O','P','Q','R','S','T',
          'U','V','W','X','Y','Z']
    # level 4 : 123+abc+ABC+!$%&_=+
    l4 = ['0','1','2','3','4','5','6','7','8','9',
          'a','b','c','d','e','f','g','h','i','j',
          'k','l','m','n','o','p','q','r','s','t',
          'u','v','w','x','y','z',
          'A','B','C','D','E','F','G','H','I','J',
          'K','L','M','N','O','P','Q','R','S','T',
          'U','V','W','X','Y','Z',
          '!','$','%','&','_','=','+']
    # level 5 charact set 
    l5_1 = ['!','$','%','&','_','=','+']
    l5_2 = ['a','b','c','d','e','f','g','h','i','j',
          'k','l','m','n','o','p','q','r','s','t',
          'u','v','w','x','y','z',
          'A','B','C','D','E','F','G','H','I','J',
          'K','L','M','N','O','P','Q','R','S','T',
          'U','V','W','X','Y','Z']
    l5_3 = ['0','1','2','3','4','5','6','7','8','9']
    try:
        if level not in ['l1','l2','l3','l4','l5']:
            raise Exception(0,'incorrect input')
        if plength < 4:
            raise Exception(0,'password is too short')
        elif plength > 19:
            raise Exception(0,'password is too long')
        else:
            for letnum in range(0,plength):
                if level == 'l1':
                    pwList.append(choice(l1))
                elif level == 'l2':
                    pwList.append(choice(l2))
                elif level == 'l3':
                    pwList.append(choice(l3))
                elif level == 'l4':
                    pwList.append(choice(l4))
                elif level == 'l5':
                    if letnum%3 == 0:
                        pwList.append(choice(l5_2))
                    if letnum%3 == 1:
                        pwList.append(choice(l5_3))
                    if letnum%3 == 2:
                        pwList.append(choice(l5_1))
            pwString = ''.join(pwList)
            return pwString
    except Exception as err:
        return err
            
if __name__ == '__main__':
    argv = argv[1:]
    opts, args = getopt(argv, "l:p:hv",['level=','plength=','help','version'])
    for opt,arg in opts:
        if opt in ['-h','--help']:
            helpMsg()
            exit()
        elif opt in ['-v','--version']:
            showVersion()
            exit()
    try:
        for opt, arg in opts:
            if opt in ['-l', '--level']:
                passwordLevel = arg
            elif opt in ['-p', '--plength']:
                passwordLength = int(arg)
            else:
                raise Exception('-1','Error in arguments!')
        rtnData = randomPassword(plength=passwordLength,level=passwordLevel)
        print(rtnData)
        copy(rtnData)
    except GetoptError:
        print(0,'input arguments error')
        print(opts)
    except Exception as err:
        print(err)