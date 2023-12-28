import os
import win32com.client as client
from encontrar import encontrar_pasta
from time import sleep
def conversor_xls():
    excel = client.Dispatch("excel.application")
    pasta = encontrar_pasta()
    sleep(15)

    for file in os.listdir(pasta + "/old version/"):
        filename, fileextension = os.path.splitext(file)
        wb = excel.Workbooks.open(pasta + "/old version/" + file)
        output_path = pasta + "/new version/" + filename
        wb.SaveAs(output_path,51)
        wb.Close()

    excel.Quit()