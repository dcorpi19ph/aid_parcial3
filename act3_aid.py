import platform
import sys
import subprocess
import json

sistemaos = sys.platform
sistema = platform.system()
version = platform.win32_ver()
procesador = platform.processor()
hostname = platform.node()

if sistema == 'Windows':
    local = subprocess.getoutput("""for /f "tokens=2 delims=[]" %a in ('ping -n 1 -4 "%computername%"') do @echo %a""")
else:
    local = subprocess.getoutput("ifconfig | grep 'inet ' | grep -Fv 127.0.0.1 | awk '{print $2}'")
print(local)

diccionario = {'ip':local, 'so':sistemaos, 'version':version, 'hostname':hostname, 'cpu':procesador}
dictionaryToJson = json.dumps(diccionario)
print(dictionaryToJson)