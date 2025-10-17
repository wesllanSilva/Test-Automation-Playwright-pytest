# 🧠 Automação de Testes com Playwright + Pytest

Este repositório contém **anotações e códigos do projeto prático** desenvolvidos ao longo do estudo sobre **“Automação de Testes com Playwright usando Python”**, estudo para entender os testes web modernos e profissionais.

![Python](https://img.shields.io/badge/Python-3.11%2B-blue?logo=python)
![Pytest](https://img.shields.io/badge/Pytest-Framework-brightgreen?logo=pytest)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)
![Build](https://img.shields.io/badge/Build-Passing-success)
---

## 📘 Projeto

O **Playwright**, é uma das ferramentas mais modernas e completas para **automação de testes web**. Ele suporta múltiplos navegadores — **Chromium, Firefox e WebKit** — e oferece recursos poderosos como:

- Esperas automáticas (_auto-wait_);
- Gravação de scripts;
- Depuração integrada;
- Suporte nativo a paralelismo e relatórios.


---

## 🚀 Conteúdo e Evolução

 Etapa da evolução no estudo, com **anotações**, **exercícios** e **implementações práticas**.

### 🔹Fundamentos
- Instalação do Python e configuração do ambiente virtual  
- Instalação e setup do Playwright  
- Criação e execução do primeiro teste automatizado  

### 🔹Explorando o Playwright
- Navegação e interações básicas  
- Seletores e boas práticas  
- Inspeção de elementos e debugging  

### 🔹Estruturando o Projeto com POM
- Introdução ao **Page Object Model (POM)**  
- Organização de diretórios e classes de página  
- Reutilização de componentes e manutenção de código  

### 🔹Pytest e Fixtures
- Criação e uso de **fixtures**  
- Escopos e estratégias de reaproveitamento  
- Execução de testes em múltiplos contextos  

### 🔹Recursos Avançados
- Upload e download de arquivos  
- Execução em paralelo  
- Relatórios HTML personalizados  
- Autenticação com **storage state**  

### 🔹Integração e Deploy
- Integração com **CI/CD** usando Jenkins  
- Boas práticas para pipelines de automação  
- Geração de artefatos e logs automatizados  

---

## 📚 Tecnologias Utilizadas &  Referências Oficiais

- **Python** 🐍
- Documentação Oficial: https://docs.python.org/3/


- **Playwright** 🌐  
Documentação Oficial: [https://playwright.dev/python/docs/intro](https://playwright.dev/python/docs/intro)  
Repositório GitHub: [https://github.com/microsoft/playwright-python](https://github.com/microsoft/playwright-python)


- **Pytest** ⚙️  
Documentação Oficial: [https://docs.pytest.org/en/stable/](https://docs.pytest.org/en/stable/)  
Repositório GitHub: [https://github.com/pytest-dev/pytest](https://github.com/pytest-dev/pytest)


- **Jenkins** 🧱 (CI/CD) 
Documentação Oficial: https://www.jenkins.io/doc/
Repositório GitHub: https://github.com/jenkinsci/jenkins


- **HTML Reports** 📊  
Documentação Oficial: https://pytest-html.readthedocs.io/en/latest/
Repositório GitHub: https://github.com/pytest-dev/pytest-html
## 📚 Referências Oficiais

🔗 **Playwright (Python)**  

🔗 **Pytest**  

---

## 🎯 Objetivos de Aprendizado

- Criar **testes rápidos, confiáveis e eficientes** para qualquer aplicação web.  
- Estruturar suítes de teste escaláveis com **Page Object Model** e **Fixtures do Pytest**.  
- Dominar os **fundamentos do Playwright**: navegação, interações, seletores e manuseio de arquivos.  
- Integrar testes automatizados em pipelines **CI/CD**.  

---

## 🧪 Como Executar o Projeto Localmente

```bash
# Clone o repositório
git clone https://github.com/wesllanSilva/python_automation_postgresql.git
cd Test-Automation-Playwright-pytest

# Crie e ative um ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Instale as dependências
pip install -r requirements.txt

# Execute os testes
pytest
