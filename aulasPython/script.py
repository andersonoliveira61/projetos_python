import pywhatkit as kit
import time

contatos = [] #Lista de contatos aqui
mensagem = 'Você acaba de receber uma mensagem do novo programa de envios automáticos do Anderson, feito com Python'

for numero in contatos:
    try:
        hora = time.localtime().tm_hour
        minuto = time.localtime().tm_min + 1  # Define 1 minuto no futuro
        kit.sendwhatmsg(numero, mensagem, hora, minuto)
        print(f"Mensagem enviada para {numero}")
        time.sleep(60)  # Aguarda para evitar bloqueio
    except Exception as e:
        print(f"Erro ao enviar mensagem para {numero}: {e}")
