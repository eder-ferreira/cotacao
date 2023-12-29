ESTUDO CONFORME VIDEO: 
Como Criar uma Tela em Python Para Seus Códigos - [Interface Gráfica Intuitiva com Tkinter]
https://www.youtube.com/watch?v=AiBC01p58oI


Criação de uma venv no VS Code

Passo 1:Abrindo um projeto no VS Code:
Após a instalação, abra o VS Code e crie ou abra um projeto existente.

Passo 2:Abrindo o terminal integrado:

Passo 3: Instalação da biblioteca `venv` e criação de uma venv:
Antes de criar uma venv, você precisa garantir que a biblioteca `venv` 
esteja instalada em seu sistema. No terminal do VS Code, digite o seguinte comando:

    pip3 install venv

Após a instalação da biblioteca `venv`, você pode prosseguir com a criação da venv. 
No terminal do VS Code, digite o seguinte comando:

    python -m venv nome_da_venv

Passo 4: Ativação da venv:
    source nome_da_venv/bin/activate

Passo 5: Desativação da venv:
Quando você terminar de trabalhar em seu projeto e desejar desativar a venv, 
basta digitar o seguinte comando no terminal:

    deactivate

Passo 6: Instalando pacotes e bibliotecas:

pip3 install numpy
pip3 install pandas

Passo 7: Freeze dos requirements:

Para facilitar a reprodução do ambiente virtual em outro local, é útil ter um 
arquivo com uma lista de todos os pacotes e versões instalados. No terminal do VS Code, 
com a venv ativada, digite o seguinte comando:

    pip3 freeze > requirements.txt

Isso criará um arquivo chamado "requirements.txt" no diretório do seu projeto, 
contendo uma lista de todas as bibliotecas e suas versões.