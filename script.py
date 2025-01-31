import pyautogui
import pandas
import time

pyautogui.PAUSE = 0.5

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(3)

pyautogui.click(x=-1170, y=301)
pyautogui.hotkey("ctrl", "a")
pyautogui.write("devpython@gmail.com.br")
pyautogui.press("tab")
pyautogui.write("dfodmnjs85215")
pyautogui.click(x=-1155, y=453)
time.sleep(3)

tabela = pandas.read_csv("produtos.csv")
print(tabela)

for linha in tabela.index:  

    pyautogui.click(x=-1322, y=186)
    codigo = str(tabela.loc[linha, "codigo"]) #str trasnforma em texto
    pyautogui.write(codigo)

    marca = str(tabela.loc[linha, "marca"])
    pyautogui.press("tab")
    pyautogui.write(marca)

    tipo = str(tabela.loc[linha, "tipo"])
    pyautogui.press("tab")
    pyautogui.write(tipo)

    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.press("tab")
    pyautogui.write(categoria)

    preco_unitario = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.press("tab")
    pyautogui.write(preco_unitario)

    custo = str(tabela.loc[linha, "custo"])
    pyautogui.press("tab")
    pyautogui.write(custo)

    pyautogui.press("tab")
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)


    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(5000)

