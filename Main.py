import tkinter as tk
import funciones as fc
import cargarMD as MD

def ventana_bienvenida():
    # Crear la ventana de bienvenida
    Info = tk.Tk()
    Info.title("Bienvenida")  
    Info.geometry("600x200")
    Info.title("Proyecto 2 - Lenguajes Formales y de Programacion")

    label = tk.Label(Info,text ="Información del Desarrollador",foreground="blue").place(x=150, y=10)
    label = tk.Label(Info,text ="Lenguajes Formales y de Programación",foreground="green").place(x=150, y=50)
    label = tk.Label(Info,text ="Vacaciones - Junio - Sección: 'P'",foreground="green").place(x=150, y=70)
    label = tk.Label(Info,text ="Carnet: 9516098",foreground="green").place(x=150, y=90)
    label = tk.Label(Info,text ="Gustavo Adolfo Lorenzana Ecuté",foreground="green").place(x=150, y=110)
    label = tk.Label(Info, text="¡Bienvenido a la aplicación Spark Stack !",foreground="blue",font=("Arial", 15)).place(x=100, y=150)

    # Cerrar la ventana de bienvenida después de 5 segundos
    Info.after(500, Info.destroy)

    # Mostrar la ventana de bienvenida
    Info.mainloop()


def ventana_principal():
    # Crear la ventana principal
    ventana = tk.Tk()
    ventana.title("Sistema de validación de autómatas Spark Stack")
    ventana.geometry("550x200")

    # Definir la función para cerrar la ventana principal y mostrar la ventana de despedida
    def cerrar_ventana():
        ventana.destroy()

        despedida = tk.Tk()
        despedida.title("Despedida")
        despedida.geometry("600x200")
        label = tk.Label(despedida, text="Gracias por utilizar el Sistema Spark Stack",foreground="blue",font=("Arial", 20))
        label.grid(sticky="nsew")

        # Configurar el tamaño de la celda del Label para que se expanda
        despedida.grid_rowconfigure(0, weight=1)
        despedida.grid_columnconfigure(0, weight=1)

        despedida.after(500, despedida.destroy)

        despedida.mainloop()
  
   
    label = tk.Label(ventana, text="Sistema Spark Stack",foreground="blue",font=("Arial", 20))
    label.grid(sticky="nsew")

    # Configurar el tamaño de la celda del Label para que se expanda
    ventana.grid_rowconfigure(0, weight=1)
    ventana.grid_columnconfigure(0, weight=1)

     # Crear un menú con la opción "Salir" que llame a la función cerrar_ventana
    menu_principal = tk.Menu(ventana)
    menu_archivo = tk.Menu(menu_principal, tearoff=0)
    ventana.config(menu=menu_principal)
    # Opción "Archivo"
    
    menu_principal.add_cascade(label="Archivo", menu=menu_archivo)

    # crear un submenu
    sub_menu1 = tk.Menu(menu_archivo, tearoff=0)
    menu_archivo.add_cascade(label="Módulo Gramática libre de contexto", menu=sub_menu1)
    sub_menu2 = tk.Menu(menu_archivo, tearoff=0)
    menu_archivo.add_cascade(label="Módulo autómatas de pila", menu=sub_menu2)

    # submenu de Modulo Gramatica libre de contexto
    sub_menu1.add_command(label="Cargar archivo",command=fc.cargar_archivo_glc)
    sub_menu1.add_command(label="Mostrar información general",command=fc.informacion_glc)
    sub_menu1.add_command(label="Arbol de derivación",command=fc.arbol_derivacion)

    # submenu de Modulo autómatas de pila
    sub_menu2.add_command(label="Cargar archivo",command=fc.cargar_archivo_pila)
    sub_menu2.add_command(label="Mostrar información del autómata",command=fc.informacion_pila)
    sub_menu2.add_command(label="Validar cadena",command=fc.validar_cadena_pila)
    sub_menu2.add_command(label="Ruta de validación",command=fc.ruta_validacion_cadena)
    sub_menu2.add_command(label="Recorrido paso a paso",command=fc.recorido_paso_paso)
    menu_archivo.add_separator()
    menu_archivo.add_command(label="Salir", command=cerrar_ventana)


    # Opción "Ayuda"
    menu_ayuda = tk.Menu(menu_principal, tearoff=False)
    menu_principal.add_cascade(label="Ayuda", menu=menu_ayuda)
    menu_ayuda.add_command(label="Manual Técnico", command=MD.manualTecnico)
    menu_ayuda.add_command(label="Manual de Usuario", command=MD.manualUsuariomd)
 

    # Mostrar la ventana principal
    ventana.mainloop()


# Llamar a las funciones para mostrar las ventanas
ventana_bienvenida()
ventana_principal()