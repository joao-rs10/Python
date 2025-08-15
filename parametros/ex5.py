#Defina uma função chamada concatenar_strings que aceite duas strings e um
#parâmetro nomeado separador com um valor padrão de espaço. A função deve
#retornar as duas strings concatenadas com o separador entre elas

def concatenar_strings(string1: str, string2: str, separador: str = ""):
    print(f"{string1}{separador}{string2}")
concatenar_strings("Olá", "Mundo", " ")


