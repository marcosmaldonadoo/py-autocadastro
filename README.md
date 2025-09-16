# Automação de Cadastro de Produtos 🖥️📋

[![Python](https://img.shields.io/badge/python-3.13-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

Este projeto é resultado da **primeira aula do Intensivão de Python** da [Hashtag Treinamentos](https://www.hashtagtreinamentos.com/).
Ele automatiza o cadastro de produtos em um sistema web utilizando Python, **pandas** e **pyautogui**.

---

## 🎯 Funcionalidades

- Leitura de uma tabela de produtos a partir de um CSV (`produtos.csv`) com **pandas**.
- Automação do navegador Microsoft Edge:
  - Acessa o site de login.
  - Preenche login e senha automaticamente.
  - Insere os dados dos produtos na plataforma.
- Ignora campos vazios (`NaN`) de forma automática.
- Facilita testes e aprendizado de automação web com Python.

---

## 🛠 Tecnologias utilizadas

- [Python 3](https://www.python.org/)
- [pandas](https://pandas.pydata.org/)
- [pyautogui](https://pyautogui.readthedocs.io/)
- Microsoft Edge (navegador para automação)

---

## 📁 Estrutura do projeto

pyautogui/
│ main.py # Script principal de automação
pyautogui/
│ produtos.csv # CSV com dados dos produtos
README.md # Documentação do projeto


---

## ⚡ Demonstração

> Você pode adicionar aqui um GIF mostrando a automação rodando ou prints da tela.

![Automação](docs/automacao.gif)

---

## 🚀 Como usar

### 1️⃣ Clonar o repositório
```bash
git clone [https://github.com/seu-usuario/nome-do-repositorio.git](https://github.com/seu-usuario/nome-do-repositorio.git)
cd nome-do-repositorio
2️⃣ Criar e ativar um ambiente virtual (recomendado)
Bash

python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate
3️⃣ Instalar dependências
Bash

pip install pandas pyautogui
4️⃣ Configurar o script
Abra automação/main.py e configure:

- Suas credenciais de login (login e password)
- Caminho do arquivo CSV (produtos.csv)
5️⃣ Executar
Bash

python automação/main.py
⚠️ Atenção: não use o computador para outras tarefas enquanto o script estiver rodando, pois o pyautogui controla teclado e mouse.

Campos vazios na tabela (NaN) são ignorados automaticamente.

O script é apenas para fins educacionais e práticos, seguindo o conteúdo da primeira aula do Intensivão de Python da Hashtag Treinamentos.

🤝 Contribuição
Contribuições são bem-vindas! Para isso:

Fork este repositório.

Crie uma branch (git checkout -b feature/nome-da-feature)

Faça suas alterações.

Commit (git commit -m "Descrição da alteração")

Push (git push origin feature/nome-da-feature)

Abra um Pull Request

📄 Licença
Este projeto está licenciado sob a MIT License.

👤 Autor
Marcos Maldonado

Email: marcosmaldonado0708@gmail.com

GitHub: marcosmaldonadoo

