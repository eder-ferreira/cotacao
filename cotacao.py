import requests
from tkinter import*
from datetime import datetime

def cotacoes():
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

    requisicao_dic = requisicao.json()

    cotacao_dolar = requisicao_dic['USDBRL']['bid']
    cotacao_euro = requisicao_dic['EURBRL']['bid']
    cotacao_btc = requisicao_dic['BTCBRL']['bid']

    agora = datetime.now()
    formato_dt = agora.strftime("%d-%m-%y %H:%M:%S")
    
    texto = f'''
    Dólar: {cotacao_dolar}
    Euro : {cotacao_euro}
    BTC  : {cotacao_btc}
    Data : {formato_dt}'''
    print(texto)
    

cotacoes()

