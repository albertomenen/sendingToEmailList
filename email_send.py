import smtplib
import requests


your_name = "Manuel Menendez"
your_email = 'manuelmenendezmicrosoft@gmail.com'
sender_pass = 'ogxuuijylvcpttyw'
receiver_address = 'creatumoneda@gmail.com'


server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server.ehlo()
server.login("manuelmenendezmicrosoft@gmail.com", "ogxuuijylvcpttyw")

r = requests.get("https://api.apispreadsheets.com/data/Td4KGcddGrkTdHWU/")

if r.status_code == 200:
    #Exito
    data = r.json() ["data"]
    print("Exito")
else:
    #Error
    data = None
    print("Fail")

for idx in range(len(data)):
    #Obtener cada dato de la lista
    name = data[idx]["Name"].strip()
    email = data[idx]["email"].strip()
    subject = data[idx]["Subject"].strip()
    message = data[idx]["Message"].strip()

    full_email = ("From: {0}< {1}> \n"
                "To: {2} < {3} > \n"
                "Subject: {4} \n\n"
                " {5}"
                .format(your_name, your_email, name, email, subject, message))


    try:
        server.sendemail(your_email, [email], full_email)
        print (" El email se envió a {} satisfactoriamente!\n\n ".format(email))
    except Exception as e:
        print("El email a  {} no se pudo mandar debido a {} \n\n".format(email, str(e)))


## Cerrar el servidor

server.close()
