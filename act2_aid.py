import pywhatkit

try:
    #pywhatkit.sendwhatmsg_instantly("+524445859868", "Hola desde Python2")
    pywhatkit.sendwhatmsg_to_group_instantly("HMSd7sLfFPy4ivP0YtAqvE", "Enviado")
    print("Mensaje enviado")
except:
    print("ERROR 404 STIC-MÉXICO")