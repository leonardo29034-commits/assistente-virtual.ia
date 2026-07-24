import os
import google.generativeai as genai

# Configura a chave de API
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))

def carregar_arquivos():
    base_path = os.path.dirname(os.path.abspath(__file__))
    
    caminho_conhecimento = os.path.join(base_path, '..', 'data', 'conhecimento.txt')
    caminho_prompt = os.path.join(base_path, '..', 'docs', 'prompt_system.txt')

    with open(caminho_conhecimento, 'r', encoding='utf-8') as f:
        conhecimento = f.read()

    with open(caminho_prompt, 'r', encoding='utf-8') as f:
        prompt_sistema = f.read()

    return conhecimento, prompt_sistema

def main():
    conhecimento, prompt_sistema = carregar_arquivos()
    contexto = f"{prompt_sistema}\n\n[BASE DE CONHECIMENTO]:\n{conhecimento}"

    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        system_instruction=contexto
    )

    chat = model.start_chat()
    print("--- Assistente de Segurança Bancária Iniciado (digite 'sair' para encerrar) ---")

    while True:
        pergunta = input("\nVocê: ")
        if pergunta.lower() == 'sair':
            break

        resposta = chat.send_message(pergunta)
        print(f"\nAssistente: {resposta.text}")

if __name__ == "__main__":
    main()
