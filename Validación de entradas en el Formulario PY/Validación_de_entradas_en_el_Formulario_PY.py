## 3MLIDTS-EmmanuelSalinas-05Python
## Validación de entradas en Formulario

## Almacenamiento en TXT
import re
import tkinter as tk
from tkinter import messagebox

##Definición de función
def limpiar_campos():
    tbNombre.delete(0, tk.END)
    tbApellidos.delete(0, tk.END)
    tbEdad.delete(0, tk.END)
    tbEstatura.delete(0, tk.END)
    tbTelefono.delete(0, tk.END)
    var_genero.set(0)
    
def borrar():
    limpiar_campos()    
    
def guardar_valores():
    ##Obtener valores desde los entrys
    nombres = tbNombre.get().strip()
    apellidos = tbApellidos.get().strip()
    edad_str = tbEdad.get().strip()
    estatura_str = tbEstatura.get().strip()
    telefono = tbTelefono.get().strip()
    
    ##Validación de datos
    if not nombres or not apellidos or not edad_str or not estatura_str or not telefono:
        messagebox.showerror("Error", "Todos los campos deben ser completados.")
        return

    if not re.match("^[A-Za-z\s]+$", nombres):
        messagebox.showerror("Error", "El campo 'Nombres' debe contener solo letras y espacios.")
        return
    
    if not re.match("^[A-Za-z\s]+$", apellidos):
        messagebox.showerror("Error", "El campo 'Apellidos' debe contener solo letras y espacios.")
        return
    
    if not telefono.isdigit() or len(telefono) != 10:
        messagebox.showerror("Error", "El campo 'Telefono' debe contener exactamente 10 digitos y debe de contener solo numeros.")
        return

    try:
        edad = int(edad_str)
    except ValueError:
        messagebox.showerror("Error", "La edad debe ser un numero entero.")
        return
    
    try:
        estatura = float(estatura_str)
    except ValueError:
        messagebox.showerror("Error", "La estatura debe ser un numero decimal.")
        return

    genero = ""
    if var_genero.get() == 1:
        genero = "Hombre"
    elif var_genero.get() == 2:
        genero = "Mujer"
    else:
        messagebox.showerror("Error", "Debe seleccionar un genero.")
        return
    
    ##Generar la cadena de caracteres
    datos = ("Nombres: " + nombres + "\n" +
             "Apellidos: " + apellidos + "\n" +
             "Edad: " + str(edad) + " anios\n" +
             "Estatura: " + str(estatura) + "\n" +
             "Telefono: " + telefono + "\n" +
             "Genero: " + genero + "\n")
    
    ##Guardar los datos en el archivo TXT
    with open("312034Datos.txt", "a") as archivo:
        archivo.write(datos + "\n\n")
        
    ##Mostrar mensaje de confirmación
    messagebox.showinfo("Informacion", "Datos guardados con exito:\n\n" + datos)
    
    ##Limpiar los campos después de guardar
    limpiar_campos()

##Creación de Ventana
ventana = tk.Tk()
ventana.geometry("520x500")
ventana.title("Formulario Vr.01")

##Variable Genero para RadioButton
var_genero = tk.IntVar()

##Creación de etiquetas y campos
lbNombre = tk.Label(ventana, text="Nombres:")
lbNombre.pack()
tbNombre = tk.Entry()
tbNombre.pack()

lbApellidos = tk.Label(ventana, text="Apellidos:")
lbApellidos.pack()
tbApellidos = tk.Entry()
tbApellidos.pack()

lbTelefono = tk.Label(ventana, text="Telefono:")
lbTelefono.pack()
tbTelefono = tk.Entry()
tbTelefono.pack()

lbEdad = tk.Label(ventana, text="Edad:")
lbEdad.pack()
tbEdad = tk.Entry()
tbEdad.pack()

lbEstatura = tk.Label(ventana, text="Estatura:")
lbEstatura.pack()
tbEstatura = tk.Entry()
tbEstatura.pack()

lbGenero = tk.Label(ventana, text="Genero:")
lbGenero.pack()
rbMasculino = tk.Radiobutton(ventana, text="Hombre", variable=var_genero, value=1)
rbMasculino.pack()
rbFemenino = tk.Radiobutton(ventana, text="Mujer", variable=var_genero, value=2)
rbFemenino.pack()

##Creación de botones
btnBorrar = tk.Button(ventana, text="Borrar datos", command=borrar)
btnBorrar.pack()
btnGuardar = tk.Button(ventana, text="Guardar datos", command=guardar_valores)
btnGuardar.pack()

##Ejecución de ventana
ventana.mainloop()

