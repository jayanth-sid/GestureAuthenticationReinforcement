from cryptography.fernet import Fernet
from os import listdir

def create_user(id,pwd,gpwd):
    filekey = open('usrs/filekey.key', 'r')
    key = filekey.read()
    key = Fernet(key)
    s = pwd+gpwd.lower()
    encoded = key.encrypt(s.encode())
    f = open('usrs/'+id+'.txt','ab')
    f.write(encoded)
    f.close()
    return 1

def login_user(id,pwd,gpwd):
    filekey = open('usrs/filekey.key', 'rb')
    key = filekey.read()
    key = Fernet(key)
    fid = id+'.txt'
    if fid in listdir('usrs/'):
        f = open('usrs/'+fid,'rb')
        dec = key.decrypt(f.read()).decode()
        print(dec)
        pre = list(gpwd.keys())[0]
        print(pre)
        # authentication succesful
        if gpwd[pre] > 0.6 and dec [:len(dec)-1:] == pwd and pre.lower() == dec[-1]:
            return 2
        # authentication failed
        else:
            return 3
     # user not found
    else:
        return 1
