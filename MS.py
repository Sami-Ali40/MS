#coding=utf-8
import os, sys, platform
try:
    import requests
except:
    os.system('pip install requests')
os.system('xdg-open https://f//')
import requests
try:
    if sys.argv[1]=='update':
        os.system('rm -rf Sami.so Sami-Ali40.so')
except:
    pass
os.system('rm -rf Sami.so Sami-Ali40.so')
os.system('git pull')

bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('Sami.so'):
        os.system('curl -L https://github.com/Sami-Ali40/MS#3A00FF.git /executables/blob/main/Sami.cpython-311.so?raw=true -o Sami.so') 
        import Sami
    else:
        import Sami

elif bit == '32bit':
    if not os.path.isfile('Sarfraz32.so'):
        os.system('curl -L https://github.com/Sarfraz-XD/executables/blob/main/Sarfraz32.cpython-311.so?raw=true -o Sarfraz32.so') 
        import Sami-Ali40
    else:
        import Sami-Ali40
