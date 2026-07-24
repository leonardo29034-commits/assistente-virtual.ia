# Assistente Virtual de Segurança Bancária e Análise de Transações

> Projeto desenvolvido para o Lab de Inteligência Artificial da DIO.

## 📌 Pitch do Projeto
- **O Problema:** Clientes frequentemente têm dúvidas sobre bloqueios preventivos de transações e limites de segurança, gerando alto volume de chamados de suporte.
- **A Solução:** Um assistente virtual baseado em IA Generativa que responde dúvidas usando estritamente uma base de conhecimento oficial.
- **O Impacto:** Atendimento imediato, redução de ruído no suporte e garantia de respostas alinhadas às políticas de segurança bancária.

## 📁 Estrutura do Repositório
- `data/`: Base de dados e regras de negócio (`conhecimento.txt`).
- `docs/`: Documentação e diretrizes do agente (`documentacao.md` e `prompt_system.txt`).
- `src/`: Código-fonte do protótipo em Python (`app.py`).

## 🚀 Como Executar
1. Instale a biblioteca do Google Gemini:
   ```bash
   pip install google-generativeai
