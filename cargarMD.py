
import tkinter as tk
import webbrowser
import markdown2


#epsilon = '\u03B5'
#print(epsilon)

def abrir_manual_tecnico():

    markdown_file = 'manual_tecnico.md'


    with open(markdown_file, 'r', encoding='utf-8') as file:
        markdown_content = file.read()

    html_content = markdown2.markdown(markdown_content)

    temp_file = 'temp.html'

    with open(temp_file, 'w', encoding='utf-8') as file:
        file.write(html_content)

    webbrowser.open_new_tab(temp_file)

 

def abrir_manual_usuario():
    # Ruta del archivo Markdown
    markdown_file = 'manual_usuario.md'

    with open(markdown_file, 'r', encoding='utf-8') as file:
        markdown_content = file.read()

    html_content = markdown2.markdown(markdown_content)

    temp_file = 'temp.html'

    with open(temp_file, 'w', encoding='utf-8') as file:
        file.write(html_content)

    webbrowser.open_new_tab(temp_file)




# Función para llamar a la acción de abrir el documento Markdown


def manualUsuariomd():
    abrir_manual_usuario()

def manualTecnico():
    abrir_manual_tecnico()
