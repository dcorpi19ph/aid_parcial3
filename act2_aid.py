import pywhatkit

try:
    #pywhatkit.sendwhatmsg("+524445859868", "Hola desde Python", 18, 10)
    pywhatkit.sendwhatmsg_instantly("+524445859868", "Hola desde Python", 18, 10)
    print("Mensaje enviado")
except:
    print("ERROR 404 STIC-MÉXICO")