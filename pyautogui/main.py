import pyautogui
import pandas as pd
import time

# Credenciais
login = "marcosdeveloper@tester.com"
password = "9090190"

# Carregar tabela de produtos
tabela = pd.read_csv("pyautogui/produtos.csv")

# Abrir Edge e acessar o site
pyautogui.press("win")
pyautogui.write("edge")
pyautogui.press("enter")
time.sleep(1)
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(2)

# Login
pyautogui.click(x=823, y=361)
pyautogui.write(login)
pyautogui.press("tab")
pyautogui.write(password)
pyautogui.press("enter")
time.sleep(2)

# Preenchimento dos produtos
for linha in tabela.index:
    pyautogui.click(x=781, y=251)
    
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)
    pyautogui.press("tab")
    
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(marca)
    pyautogui.press("tab")
    
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(tipo)
    pyautogui.press("tab")
    
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")
    
    preco_unitario = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco_unitario)
    pyautogui.press("tab")
    
    preco_custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(preco_custo)
    pyautogui.press("tab")
    
    observacao = tabela.loc[linha, "obs"]
    # Verifica se observação não é NaN
    if pd.notna(observacao):
        pyautogui.write(str(observacao))
    pyautogui.press("tab")
    pyautogui.press("enter")

    