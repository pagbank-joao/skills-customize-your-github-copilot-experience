# 📘 Assignment: Construindo APIs REST com FastAPI

## 🎯 Objetivo

Aprender a criar uma API REST simples utilizando o framework FastAPI em Python. O estudante irá desenvolver endpoints para manipular dados de usuários, praticando conceitos de rotas, métodos HTTP e respostas JSON.

## 📝 Tarefas

### 🛠️ Task 1: Criar estrutura básica da API

#### Description
Inicialize um projeto FastAPI e crie o endpoint raiz (`/`) que retorna uma mensagem de boas-vindas.

#### Requirements
Completed program should:
- Inicializar um app FastAPI
- Criar endpoint GET `/` que retorna `{ "message": "Bem-vindo à API FastAPI!" }`

### 🛠️ Task 2: CRUD de Usuários

#### Description
Implemente endpoints para criar, listar, buscar e deletar usuários em memória (lista Python).

#### Requirements
Completed program should:
- Endpoint POST `/users` para adicionar usuário (nome, email)
- Endpoint GET `/users` para listar todos os usuários
- Endpoint GET `/users/{id}` para buscar usuário por id
- Endpoint DELETE `/users/{id}` para remover usuário

### 🛠️ Task 3: Documentação automática

#### Description
Explorar a documentação interativa gerada pelo FastAPI em `/docs`.

#### Requirements
Completed program should:
- Permitir acesso à documentação automática
- Todos endpoints devem aparecer corretamente documentados

## 💡 Dicas
- Consulte a documentação oficial do FastAPI: https://fastapi.tiangolo.com/
- Use o comando `uvicorn main:app --reload` para rodar o servidor localmente

## 📦 Starter Code
Veja o arquivo `starter-code.py` para começar seu projeto.
