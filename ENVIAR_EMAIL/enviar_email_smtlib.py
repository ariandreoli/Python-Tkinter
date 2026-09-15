"""
SMTP
¿Qué es y para qué sirve SMTP?
SMTP, Simple Mail Transfer Protocol por sus siglas en inglés, es un protocolo o conjunto de reglas 
de comunicación que utilizan los servidores de correo electrónico para enviar y recibir e-mails.
"""
from email.message import EmailMessage  #estructura del email
import smtplib  # Conexión con el servidor y  para enviarlo
from tkinter import *
from tkinter import messagebox
# Python Image Library
from PIL import Image, ImageTk  

"------------INTERFAZ TKINTER------------"
ventana = Tk()
ventana.title("APLICACION DE MENSAJERIA")
ventana.geometry("380x480")
ventana.resizable(0, 0)
ventana.config(bd=10)

Label(
    ventana,
    text="ENVIAR CORREO VIA GMAIL",
    fg="black",
    font=("Arial", 15, "bold"),
    padx=5,
    pady=5,
).grid(row=0, column=0, columnspan=2)

# Imagen GMAIL
try:
    imagen_gmail = Image.open("logo_gmail.png")
    nueva_imagen = imagen_gmail.resize((125, 84))
    render = ImageTk.PhotoImage(nueva_imagen)
    label_imagen = Label(ventana, image=render)
    label_imagen.image = render
    label_imagen.grid(row=1, column=0, columnspan=2)
except Exception:
    Label(
        ventana, text="[Imagen no encontrada: ubica logo_gmail.png en la carpeta]", fg="red"
    ).grid(row=1, column=0, columnspan=2)

# Variables
destinatario_manual = StringVar(ventana)
asunto = StringVar(ventana)

REMITENTE = "especialidad246@gmail.com"

Label(
    ventana,
    text=f"Mi correo: {REMITENTE}",
    fg="white",
    bg="blue",
    font=("Arial", 10, "bold"),
    padx=5,
    pady=5,
).grid(row=2, column=0, columnspan=2, pady=5)

#OptionMenu
Label(
    ventana, text="Lista correos:", fg="black", font=("Arial", 10, "bold"), padx=5, pady=5
).grid(row=3, column=0)

opciones_emails = [
    "Seleccionar opción...",
    "fjcoronati@gmail.com",
    "mfedullo@gmail.com",
    "lafortaleza246@institucion.edu.ar",

]

email_seleccionado = StringVar(ventana)
email_seleccionado.set(opciones_emails[0])

menu_emails = OptionMenu(ventana, email_seleccionado, *opciones_emails)
menu_emails.config(width=22)
menu_emails.grid(row=3, column=1)

Label(
    ventana, text="Destinatario:", fg="black", font=("Arial", 10, "bold"), padx=5, pady=5
).grid(row=4, column=0)
Entry(ventana, textvariable=destinatario_manual, width=34).grid(row=4, column=1)

Label(
    ventana, text="Asunto:", fg="black", font=("Arial", 10, "bold"), padx=5, pady=5
).grid(row=5, column=0)
Entry(ventana, textvariable=asunto, width=34).grid(row=5, column=1)

Label(
    ventana, text="Mensaje:", fg="black", font=("Arial", 10, "bold"), padx=5, pady=5
).grid(row=6, column=0)
mensaje = Text(ventana, height=5, width=28, padx=5, pady=5)
mensaje.grid(row=6, column=1)
mensaje.config(font=("Arial", 9), padx=5, pady=5)


"------------ENVIO DE CORREO------------"
def enviar_email():
    remitente = REMITENTE

    # Determinar destinatario (Lista o manual)
    opcion = email_seleccionado.get()
    manual = destinatario_manual.get().strip()

    if manual:
        destinatario_final = manual
    elif opcion != "Seleccionar opción...":
        destinatario_final = opcion
    else:
        messagebox.showwarning(
            "MENSAJERIA", "Seleccione un correo de la lista o ingrese uno manualmente."
        )
        return

    try:
        # Estructura de email
        email = EmailMessage()
        email["From"] = remitente
        email["To"] = destinatario_final
        email["Subject"] = asunto.get()
        email.set_content(str(mensaje.get(1.0, "end")))

        # Envio de email
        smtp = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        smtp.login(remitente, "iyuxwojsfurpttau")
        smtp.sendmail(remitente, destinatario_final, email.as_string())
        messagebox.showinfo(
            "MENSAJERIA", f"Mensaje enviado correctamente a:\n{destinatario_final}"
        )
        smtp.quit()
    except Exception as e:
        messagebox.showerror("ERROR", f"No se pudo enviar el correo:\n{e}")


"------------BOTON------------"
Button(
    ventana,
    text="ENVIAR",
    command=enviar_email,
    height=2,
    width=10,
    bg="black",
    fg="white",
    font=("Arial", 10, "bold"),
).grid(row=7, column=0, columnspan=2, padx=5, pady=10)

ventana.mainloop()
