import pyautogui
import time
import pandas as pd

pyautogui.PAUSE = 0.5

linkSistema = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

# Abrir navegador
pyautogui.press('win')
pyautogui.write('Chrome')
pyautogui.press('Enter')

# Inserir URL
pyautogui.write(linkSistema)
pyautogui.press('Enter')
pyautogui.sleep(1)

# Fazer Login
#print(pyautogui.position()) - Pegar posição do mouse
pyautogui.click(x=987, y=512)
pyautogui.write('edu@gmail.com')
pyautogui.press('Tab')

pyautogui.write('AbCdEf')
pyautogui.press('Tab')
pyautogui.press('Enter')

# pip install pandas openpyxl - Instalar biblioteca para utilizar banco de dados
 
# Leitura da tabela atribuindo na variável 'tabela'
tabela = pd.read_csv("produtos.csv")
pyautogui.click(x=765, y=366)

#Preencher cadastro - Com interação para ler toda a tabela
for linha in tabela.index: 
    pyautogui.click(x=765, y=366)
    pyautogui.write(str(tabela.loc[linha, 'codigo']))
    pyautogui.press('Tab')

    pyautogui.write(str(tabela.loc[linha, 'marca']))
    pyautogui.press('Tab')

    pyautogui.write(str(tabela.loc[linha, 'tipo']))
    pyautogui.press('Tab')

    pyautogui.write(str(tabela.loc[linha, 'categoria']))
    pyautogui.press('Tab')

    pyautogui.write(str(tabela.loc[linha, 'preco_unitario']))
    pyautogui.press('Tab')

    pyautogui.write(str(tabela.loc[linha, 'custo']))
    pyautogui.press('Tab')

    obs = str(tabela.loc[linha, 'obs'])
    if obs != 'nan':
        pyautogui.write(obs)
    
    pyautogui.press('Tab')
    pyautogui.press('Enter')
    pyautogui.scroll(2000)
    pyautogui.sleep = 0.5

# Produto cadastrado


