import pywhatkit

try:
  #  pywhatkit.sendwhatmsg("+524443483559" , "hola", 18, 41)
  # pywhatkit.sendwhatmsg_instantly("+524443483559", "hola")
    pywhatkit.sendwhatmsg_to_group_instantly("HMSd7sLfFPy4ivP0YtAqvE", "hola", 10, True,3)
    print ("Mensaje enviado")
except:
    print("Error")