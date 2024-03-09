import platform
import sys
import subprocess

sistemaos = sys.platform
sistema = platform.system()
version = platform.win32_ver()
procesador = platform.processor()

print("Estamos en {}".format(sistema), " en version: {}".format(version))
print("Procesador: {}".format(procesador))
print ("Tipo SO: {}".format(sistemaos))
if sistema == 'Windows':
    local = subprocess.getoutput("""for /f "tokens=2 delims=[]" %a in ('ping -n 1 -4 "%computername%"') do @echo %a""")
else:
    local = subprocess.getoutput("ifconfig | grep 'inet ' | grep -Fv 127.0.0.1 | awk '{print $2}'")
print(local)