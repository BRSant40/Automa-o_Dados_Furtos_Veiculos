# Importar Ferramentas Necessárias
from selenium import webdriver # Permite Automações Web
from selenium.webdriver.common.by import By # Permite Encontrar Elementos na Página
from time import sleep # Ajuda em Esperar o Carregamento da Página
import pyautogui # Ferramenta de Automação
from transferir import transferir # Transferi o arquivo para a pasta old versions
from conversor import conversor_xls # Converte xls em xlsx
import pandas as pd
import os # Ajuda a acessar arquivos e diretórios no pc
import shutil # Ajuda a mover arquivos para outras pastas
#from encontrar import encontrar_pasta # Encontrar pasta da Automação no PC

# Entrar no site -> https://www.ssp.sp.gov.br/transparenciassp/Consulta2022.aspx
driver = webdriver.Chrome()
driver.get('https://www.ssp.sp.gov.br/transparenciassp/Consulta2022.aspx')
sleep(10)

# Clicar em "FURTO DE VEICULO"
furto_veiculo = driver.find_element(By.XPATH, '//*[@id="cphBody_btnFurtoVeiculo"]')
furto_veiculo.click()
sleep(10)

#Clicar nos anos: 2020, 2021 e 2022
for n in range(20, 23):
    pyautogui.scroll(-800)
    sleep(5)
    ano = driver.find_element(By.XPATH, f'//*[contains(@id,"cphBody_lkAno{n}")]')
    ano.click()
    sleep(35)
    # Tabela de Meses
    for n in range(1, 13):
        pyautogui.scroll(-800)
        sleep(5)
        tabela_mes = driver.find_element(By.XPATH, f'//*[@id="cphBody_lkMes{n}"]')
        tabela_mes.click()
        sleep(15)
        exportar = driver.find_element(By.XPATH, '//*[@id="cphBody_ExportarBOLink"]')
        exportar.click()
        sleep(100)
        transferir()

conversor_xls()

# Laço transformando em CSV - Último
#pasta = encontrar_pasta()
pasta = os.getcwd()
#sleep(15)
with os.scandir('new version') as novos:
    for n in novos:
        with open(f'{n.name}.csv', 'w') as novo_csv:
            n2 = pd.read_excel(n)
            novo_csv.writelines(n2.to_csv())
        novo_csv.close()

        if '2020' in novo_csv.name:
            p = pasta + '\\2020'
            if os.path.exists(p):  # SE A PASTA JÁ EXISTE, ENTÃO PASSAR OS ARQUIVOS...
                file_source = pasta + f'\{novo_csv.name}'
                file_destination = pasta + '\\2020'
            else:
                os.makedirs(p)
                file_source = pasta + f'\{novo_csv.name}'
                file_destination = pasta + '\\2020'

        elif '2021' in novo_csv.name:
            p = pasta + '\\2021'
            if os.path.exists(p):  # SE A PASTA JÁ EXISTE, ENTÃO PASSAR OS ARQUIVOS...
                file_source = pasta + f'\{novo_csv.name}'
                file_destination = pasta + '\\2021'
            else:
                os.makedirs(p)
                file_source = pasta + f'\{novo_csv.name}'
                file_destination = pasta + '\\2021'

        elif '2022' in novo_csv.name:
            p = pasta + '\\2022'
            if os.path.exists(p):  # SE A PASTA JÁ EXISTE, ENTÃO PASSAR OS ARQUIVOS...
                file_source = pasta + f'\{novo_csv.name}'
                file_destination = pasta + '\\2022'
            else:
                os.makedirs(p)
                file_source = pasta + f'\{novo_csv.name}'
                file_destination = pasta + '\\2022'

        shutil.move(file_source, file_destination)

novos.close()
