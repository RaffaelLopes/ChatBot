import openai

# Chave de API para autenticação no OpenAI API
chave_api = "chaveAcesso"

# Configurando a chave de API no OpenAI SDK
openai.api_key = chave_api

# Função para enviar uma mensagem ao chatbot e obter a resposta
def enviar_mensagem(mensagem, lista_mensagens=[]):
    # Adiciona a mensagem do usuário à lista de mensagens
    lista_mensagens.append(
        {"role": "user", "content": mensagem}
    )
    
    # Chama a API da OpenAI para obter a resposta do chatbot
    resposta = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=lista_mensagens,
    )

    # A resposta["choices"][0]["message"]["content"] é uma string, não um dicionário
    return resposta["choices"][0]["message"]["content"]

# Lista de mensagens, inicialmente vazia
lista_mensagens = []

# Loop principal para interagir com o chatbot
while True:
    # Solicita ao usuário para digitar uma mensagem
    texto = input("Escreva aqui sua mensagem:")

    # Verifica se o usuário deseja sair do chat
    if texto == "sair":
        break
    else:
        # Envia a mensagem do usuário e obtém a resposta do chatbot
        resposta = enviar_mensagem(texto, lista_mensagens)

        # Adiciona a resposta à lista de mensagens com o papel "assistant"
        lista_mensagens.append({"role": "assistant", "content": resposta})

        # Exibe a resposta do chatbot
        print("Chatbot:", resposta)
