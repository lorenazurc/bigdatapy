O objetivo deste projeto é entregar os relatórios mensais para a administração de um condomínio, para que tomem decisões com embasamento em dados que foram estudados e analisados periodicamente, além de possibilitar a melhoria nas atividades internas. As atividades foram divididas em etapas:

Ação 1: Coleta dos dados
import os

def coletar_dados(diretorio, nome_arquivo):
    caminho = os.path.join(diretorio, nome_arquivo)
    if os.path.exists(caminho):
        with open(caminho, 'r') as arquivo:
            dados = arquivo.readlines()
        return dados
    else:
        print("Arquivo não encontrado.")
        return None

# como utilizar:
diretorio = 'caminho/para/diretorio'
nome_arquivo = 'dados.txt'
dados = coletar_dados(diretorio, nome_arquivo)
Ação 2: Criar um script em Python que procure o que for produzido pelo txt
def procurar_dados(dados, termo):
    resultados = [linha for linha in dados if termo in linha]
    return resultados

# como utilizar:
termo = 'termo_de_busca'
resultados = procurar_dados(dados, termo)
print(resultados)
Ação 3: Analisar os dados utilizando a biblioteca pandas
import pandas as pd

def analisar_dados(dados):
    df = pd.DataFrame([linha.split() for linha in dados], columns=['Nome', 'Entrada', 'Saida', 'Acessos'])
    df['Tempo_Permanencia'] = pd.to_datetime(df['Saida']) - pd.to_datetime(df['Entrada'])
    return df

# como utilizar:
df = analisar_dados(dados)
print(df)
Ação 4: Criar uma planilha Excel com os dados padronizados
def criar_planilha_excel(df, nome_arquivo):
    df.to_excel(nome_arquivo, index=False)

# como utilizar:
nome_arquivo_excel = 'dados_padronizados.xlsx'
criar_planilha_excel(df, nome_arquivo_excel)
Ação 5: Gerar um PDF com os dados do Excel, incluindo gráficos e tabelas
import matplotlib.pyplot as plt
from fpdf import FPDF

def gerar_pdf(nome_arquivo_excel, nome_arquivo_pdf):
    df = pd.read_excel(nome_arquivo_excel)
    
    # Criando gráficos
    plt.figure()
    df['Acessos'].plot(kind='bar')
    plt.title('Número de Acessos por Mês')
    plt.savefig('grafico_acessos.png')
    
    # Criando o PDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    # Adicionar tabela
    pdf.cell(200, 10, txt="Relatório Mensal", ln=True, align='C')
    for i in range(len(df)):
        pdf.cell(200, 10, txt=str(df.iloc[i].to_dict()), ln=True, align='L')
    
    # Adicionar gráfico
    pdf.image('grafico_acessos.png', x=10, y=100, w=100)
    
    pdf.output(nome_arquivo_pdf)

# como utilizar:
nome_arquivo_pdf = 'relatorio_mensal.pdf'
gerar_pdf(nome_arquivo_excel, nome_arquivo_pdf)
Ação 6: Enviar o PDF por e-mail através de um servidor SMTP
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def enviar_email(destinatario, assunto, corpo, anexo):
    remetente = 'seu_email@example.com'
    senha = 'sua_senha'
    
    msg = MIMEMultipart()
    msg['From'] = remetente
    msg['To'] = destinatario
    msg['Subject'] = assunto
    
    msg.attach(MIMEText(corpo, 'plain'))
    
    with open(anexo, 'rb') as arquivo:
        parte = MIMEBase('application', 'octet-stream')
        parte.set_payload(arquivo.read())
        encoders.encode_base64(parte)
        parte.add_header('Content-Disposition', f'attachment; filename={os.path.basename(anexo)}')
        msg.attach(parte)
    
    with smtplib.SMTP('smtp.example.com', 587) as servidor:
        servidor.starttls()
        servidor.login(remetente, senha)
        servidor.sendmail(remetente, destinatario, msg.as_string())

# como utilizar e renomear as variáveis:
destinatario = 'admin@condominio.com'
assunto = 'Relatório Mensal'
corpo = 'Segue em anexo o relatório mensal.'
anexo = nome_arquivo_pdf
enviar_email(destinatario, assunto, corpo, anexo)
No final do projeto, o arquivo CSV será enviado para o Power BI, enviando um relatório para a administração e portaria com uma visualização mais robusta das atividades que ocorreram no mês.