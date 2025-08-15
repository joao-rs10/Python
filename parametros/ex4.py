#Crie uma função chamada enviar_email que aceite os parâmetros destinatario,
#assunto e corpo. O parâmetro assunto deve ter um valor padrão de "Sem assunto".
#O parâmetro corpo deve ter um valor padrão de uma string vazia. A função deve
#imprimir as informações formatadas. Inclua uma docstring que explique brevemente
#o propósito da função.


def enviar_email(destinatario: str = "", assunto: str = "Sem assunto", corpo: str = ""):
    """
    Envia um email formatado com as informações fornecidas.
    Parâmetros:
    destinatario (str): O endereço de email do destinatário.
    assunto (str): O assunto do email (padrão é "Sem assunto").
    corpo (str): O corpo do email (padrão é uma string vazia).
    """
    print(f"Para: {destinatario}")
    print(f"Assunto: {assunto}")
    print(f"Corpo: {corpo}")

enviar_email()