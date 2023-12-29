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

     # Muda a cor do texto em result_cotacoes
    result_cotacoes.config(text=texto, fg="green")  # Por exemplo, verde
 
janela = Tk()
janela.title("Cotação Moedas")
janela.geometry("250x200")

texto= Label(janela, text="Buscar Cotações Dollar/Euro/ BTC")
texto.grid(column=1, row=0, padx=15, pady=5)

texto2 = Label(janela, text="Clique para buscar!")
texto2.grid(column=1, row=1, padx=5, pady=5)

botao = Button(janela, text="Atualizar", command=cotacoes)
botao.grid(column=1, row=2)

# Trazer o texto com as cotações na janela
result_cotacoes = Label(janela, text="")
result_cotacoes.grid(column=1, row=3, padx=5, pady=5)

# Inicializa a função de cotações
janela.mainloop()