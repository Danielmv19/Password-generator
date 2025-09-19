import random
import time
import string
import questionary
from rich.console import Console
from rich.markdown import Markdown
from rich import print
from rich.layout import Layout

console = Console()


digitos = string.digits
minusculas = string.ascii_lowercase
mayusculas = string.ascii_uppercase
simbolos = "#$%&?@^_!"


def pass_generator(longitud:int):
    caracteres = digitos + minusculas + mayusculas + simbolos

    password = []

    for i in range(longitud):
        char_random = random.choice(caracteres)
        password.append(char_random)

    password = "".join(password)

    return password

def long_validator(_):
    a = [str(i) for i in range(6, 22)]
    if _ in a: #['8','9','10','11','12','13','14','15','16','17','18','19','20','21','22']:
        return True
    else:
        return "Cantidad fuera del rango"

def long_q():
    longitud_contraseñas = questionary.text(
    "Longitud de contraseña", 
    validate=long_validator,
    instruction='6-22'
    ).ask()
    return int(longitud_contraseñas)

#command line interface
markdown = Markdown("# Password Generator")
console.print(markdown)
questionary.press_any_key_to_continue().ask()

Cantidad_contraseñas = questionary.select(
    "Cantidad de contraseñas",
    choices=[
        "Contraseña Multiple(5)",
        "Contraseña Unica (1)",
    ],
).ask()

def run():
    if Cantidad_contraseñas == "Contraseña Multiple(5)":
        l = long_q()
        for i in range(5):
            print(f'! Contraseña {i}: {pass_generator(l)}')
            time.sleep(1)
    else:
        l = long_q()
        time.sleep(1)
        print(f'! Contraseña: {pass_generator(l)}')


if __name__ == "__main__":
    run()
    while questionary.confirm("Continuar").ask():
        run()

