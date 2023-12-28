import os
from ultimo_arquivo import ult_arq
import pandas as pd
from transferir import transferir
#from conversor import conversor_xls
# with os.scandir('new version') as novos:
#     for n in novos:
#         print(n)
#arquivo = ult_arq()
#n = open(f"C://Users/brsan/Downloads/{arquivo}", 'r')
#with open(f'{n.name}.csv', 'w') as novo_csv:
    #pass


#print('2020' in n.name)

#with open(os.path.join(arquivo), 'r') as arq:
    #for c in arq:
        #print(c)


#home = os.environ['HOMEPATH']
# downloads = home + '\Downloads'
# print(os.listdir(downloads))


# for p in os.environ:
#     if 'Automação_furto_veiculos' in os.environ[p]:
#         print(os.environ[p])

# local = 'C:\\'
# with os.scandir(local) as arqs:
#     for arq in arqs:
#         if arq.is_file():
#             if arq == 'Automação_furto_veiculos':
#                 print('arquivo:', arq.name)
#
#         elif arq.is_dir():
#             #print('pasta:  ', arq.name)
#             for a in os.listdir(arq):
#                 print(a)


transferir()



#conversor_xls()

# import PyInstaller.__main__
#
# PyInstaller.__main__.run([
#     'main.py',
#     '--onefile',
#     '--windowed'
# ])

# from encontrar import encontrar_pasta
# pasta = encontrar_pasta()
# print(pasta + '\old version')

