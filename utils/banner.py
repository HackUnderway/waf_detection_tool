import random

colores = ["red", "green", "yellow", "blue", "magenta", "cyan", "white", "orange"]

def obtener_color_aleatorio():
    color = random.choice(colores)
    if color == "orange":
        return "\033[1;38;5;208m"
    return color

def generar_banner():
    color = obtener_color_aleatorio()
    banner_text = r"""
                   (                   
 (  (       (      )\ )    (        )  
 )\))(   '  )\    (()/(    )\ )  ( /(  
((_)()\ )((((_)(   /(_))  (()/(  )\()) 
_(())\_)())\ _ )\ (_))_|   ((_))(_))/  
\ \((_)/ /(_)_\(_)| |_     _| | | |_   
 \ \/\/ /  / _ \  | __|  / _` | |  _|  
  \_/\_/  /_/ \_\ |_|    \__,_|  \__|  
    """
    if color.startswith("\033"):
        return f"{color}{banner_text}\033[0m"
    else:
        from termcolor import colored
        return colored(banner_text, color, attrs=["bold"])

uso = "\033[1;36mUso:\033[0m\n  python3 waf_detection_tool.py [opción]"

opciones = """
\033[1;35m🔥 l      \033[0m\033[1;37mMuestra la lista de WAFs soportados.\033[0m
\033[1;35m🔥 h      \033[0m\033[1;37mMuestra esta ayuda.\033[0m
\033[1;35m🔥 v      \033[0m\033[1;37mMuestra la versión de la herramienta.\033[0m
\033[1;35m🔥 [URL]  \033[0m\033[1;37mAnaliza la URL proporcionada para detectar un WAF.\033[0m
"""

ejemplo = "\033[1;36mEjemplo:\033[0m\n  python3 waf_detection_tool.py https://hackerone.com"

def mostrar_ayuda_completa():
    print(generar_banner())  
    print(uso)
    print(opciones)
    print(ejemplo)
