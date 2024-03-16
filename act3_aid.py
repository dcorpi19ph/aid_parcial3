import platform
import sys
import subprocess
import json

file_name = "datos.json"
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
file = open(file_name, "w")
json.dump(diccionario, file, indent=4)
file.close()

#dictionaryToJson = json.dumps(diccionario)
#print(dictionaryToJson)