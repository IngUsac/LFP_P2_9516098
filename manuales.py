# en el modulo principal agregar este import "import manuales as MTU"
# import manuales as MTU # importar funciones del Manual Tecnico y Usuario

# **************** Para llamar desde el boton del menu principal MTU.AbrirManualUsuario
# **************** Para llamar desde el boton del menu principal MTU.AbrirManualTecnico 


import webbrowser
import markdown2

def manual_tecnico():

    markdown_file = 'manual_tecnico.md'

    with open(markdown_file, 'r', encoding='utf-8') as file:
        markdown_content = file.read()

    html_content = markdown2.markdown(markdown_content)

    temp_file = 'temp.html'

    with open(temp_file, 'w', encoding='utf-8') as file:
        file.write(html_content)

    webbrowser.open_new_tab(temp_file)

 
def manual_usuario():
    # Ruta del archivo Markdown
    markdown_file = 'manual_usuario.md'

    with open(markdown_file, 'r', encoding='utf-8') as file:
        markdown_content = file.read()

    html_content = markdown2.markdown(markdown_content)

    temp_file = 'temp.html'

    with open(temp_file, 'w', encoding='utf-8') as file:
        file.write(html_content)

    webbrowser.open_new_tab(temp_file)

# Función para llamar a la acción de abrir el documento Markdown desde el menu principal


def AbrirManualUsuario():
    manual_usuario()

def AbrirManualTecnico():
    manual_tecnico()
