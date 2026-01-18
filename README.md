# 📝 Cadastro de Pessoas

[![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=white)](https://www.python.org/) 
[![Status](https://img.shields.io/badge/Status-Concluído-brightgreen)](https://github.com/guilhermeemacedo/cadastro_de_pessoas)

Sistema CRUD em **Python** para gerenciamento de usuários via terminal.  
Permite **cadastrar, listar, buscar, atualizar e deletar** registros de pessoas.

---

## 🚀 Funcionalidades

- ✅ Cadastrar pessoas (nome, idade, email)  
- ✅ Listar todas as pessoas cadastradas  
- ✅ Buscar pessoas por **nome ou email**  
- ✅ Atualizar informações de pessoas (nome, idade, email)  
- ✅ Deletar pessoas com confirmação  
- ✅ Validações de entradas (nome com letras apenas, idade numérica, email único e não vazio)  
- ✅ Limpeza de tela para interface mais organizada no terminal  

---

## 🛠 Tecnologias

- **Python 3.11**  
- Bibliotecas utilizadas: `os` (para limpar a tela do terminal)  

---
## ⚡ Como executar


Clone o repositório para sua máquina:

git clone https://github.com/guilhermeemacedo/cadastro_de_pessoas.git


Entre na pasta do projeto:

cd cadastro_de_pessoas/sistema_cadastro_python


Execute o programa:

python cadastro_de_pessoas.py

----------

## 🎯 Uso / Exemplos
Após iniciar o programa, você verá o menu:

Copiar código
1 - Cadastrar pessoa
2 - Listar pessoas
3 - Buscar pessoa
4 - Atualizar pessoa
5 - Remover pessoa
0 - Sair
Para cadastrar, escolha 1, informe nome, idade e email.

Para listar, escolha 2 para ver todas as pessoas cadastradas.

Para buscar, escolha 3 e digite o nome ou email.

Para atualizar, escolha 4, selecione a pessoa e a informação que deseja alterar.

Para remover, escolha 5, confirme a exclusão.

Para sair, escolha 0.

## Nota do Desenvolvedor

Este é meu **primeiro projeto em Python**. Inicialmente, eu não conhecia o conceito de **CRUD** (Create, Read, Update, Delete), mas decidi criar este sistema de cadastro de pessoas para praticar tudo o que aprendi no curso **"Python: Crie a sua primeira aplicação" da Alura**.

### Meus principais aprendizados

- Eu entendi na prática como funciona um CRUD, manipulando dados de usuários: adicionei, listei, busquei, atualizei e removi registros.  
- Eu Aprendi a trabalhar com listas e dicionários, entendendo a diferença entre eles e como armazenar múltiplos registros de forma organizada.  
- Eu Aprendi a usar métodos importantes como .lower(), .strip() e .isdigit() para validar e tratar dados de entrada.  
- Eu Ganhei experiência em estruturar um menu interativo no terminal e controlar o fluxo do programa de forma lógica e segura.

### Minhas principais dificuldades

- Manipulação de listas e dicionários: no início, não sabia exatamente como adicionar, acessar ou remover dados corretamente.
- Validação de dados: garantir que nomes não aceitem números, que emails não sejam duplicados e que idades sejam números válidos.
- Controle do fluxo do programa, especialmente ao voltar ao menu ou repetir entradas inválidas sem quebrar a execução.

Este projeto me deu muita confiança para avançar em Python e me familiarizar com conceitos essenciais de programação.

