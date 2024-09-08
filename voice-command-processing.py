print("Inicializando...")

import speech_recognition as sr
import os

# Função para ouvir e reconhecer a fala
def ouvir_microfone():
    # Habilita o microfone do usuário
    microfone = sr.Recognizer()

    # Usando o microfone
    with sr.Microphone() as source:

        # Chama um algoritmo de redução de ruídos do som
        microfone.adjust_for_ambient_noise(source)

        # Frase para o usuário dizer algo
        print("Diga alguma coisa:")

        # Armazena o que foi dito numa variável
        audio = microfone.listen(source)

    try:
        # Passa a variável para o algoritmo reconhecedor de padrões
        frase = microfone.recognize_google(audio, language='pt-BR')

        if "navegador" in frase:
            os.system("start Chrome.exe")
            return False
        
        elif "Excel" in frase:
            os.system("start Excel.exe")
            return False
        
        elif "PowerPoint" in frase:
            os.system("start POWERPNT.exe")
            return False
        
        elif "Edge" in frase:
            os.system("start msedge.exe")
            return False
        
        elif "Fechar" in frase:
            os.system("exit")
            return False

        # Retorna a frase pronunciada
        print("Você disse: " + frase)

    # Se não reconheceu o padrão de fala, exibe a mensagem
    except sr.UnknownValueError:
        print("Não entendi")

    return frase

# Loop para continuar ouvindo até que uma ação seja realizada
while True:
    if ouvir_microfone() == False:
        break
