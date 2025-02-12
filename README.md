#Portfólio Framework para Web
## Instalação 
1. Faça um clone do repositorio atual
2. Após feito o clone abra a pasta clonada "Portfolio-FrameworkWeb" no CMD
3. Com a pasta aberta crie um ven com o seguinte comando

```bash
python -m venv venv
```

Caso não dé certo utilize o seguinte comando

```bash
python3 -m venv venv
```

4. Com o venv criado podemos executa-lo utilizando o seguinte comando caso esteja no Windows:

```bash
venv/Scripts/activate
```

Ou no Linux:

```bash
source venv/bin/activate
```

5. Com o ambiente virtual ativado podemos seguir com as instalações das dependencias com o seguinte comando

```bash
pip install -r requirements.txt
```

6. Após instalar as dependencias podemos executar o projeto

## Execução

1. Com as dependecias instaladas e o venv criado podemos executar o projeto, para isso primeiros podemos abrir o VsCode utilizando o seguinte comando

```bash
code .
```

2. Com o VsCode aberto, podemos instalar a extensão do python na loja - Extensão: Python / Microsoft

3. Com a extensão instalada podemos voltar a pasta e abrir o script app.py

## Gerando uma API GOOGLE

1. Entre no site da Google Studio API pelo link: https://aistudio.google.com/app/apikey

2. Realize o login com sua conta google

3. Caso apareça "It's Time to Build", aperte no GET API KEY

4. Aceite os termos de uso

5. Aperte Criar Chave de API

6. Aperte em copiar

7. Entre no arquivo pdf.py

8. Insira Cole a chave da API nos parenteses na linha 21, onde está escrito chave_aqui genai.configure(api_key="chave_aqui")

## Continuando a Execução 

5. Com o Script aberto podemos abertar o atalho F5 e então executar o arquivo app.py

6. Caso seja a primeira vez executando um arquivo com a extensão ele exibira algumas opções podemos escolher a primeira opção - Arquivo Python - e ele será executado
