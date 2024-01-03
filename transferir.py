from ultimo_arquivo import ult_arq
from encontrar import encontrar_pasta
from time import sleep
import shutil
import os

def transferir():
    arquivo = ult_arq()
    #pasta = encontrar_pasta()
    pasta = os.getcwd()
    sleep(25)

    home = os.environ['HOMEPATH']
    downloads = home + '\Downloads'

    p = pasta + '\old version'
    if os.path.exists(p) == False:
        os.mkdir(p)

    file_source = downloads + f'\{arquivo}'
    file_destination = pasta + '\old version'

    shutil.move(file_source, file_destination)
