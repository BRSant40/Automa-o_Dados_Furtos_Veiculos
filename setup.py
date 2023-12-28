import sys
import os
from cx_Freeze import setup, Executable

# Definir o que deve ser incluído na pasta final
arquivos = ['encontrar.py', 'transferir.py', 'ultimo_arquivo.py', 'conversor.py']

# Saída de arquivos
configuracao = Executable(
    script='main.py',
    icon='auto.jfif'
)

# Configurar o Executável
setup(
    name='Automatizador furto veiculos',
    version='1.0',
    description='Este programa tem a função de entrar no site: www.ssp, e extrair os dados de Furto de Veículos e converter os arquivos de xls para csv. Mante-lo na pasta do usuario & Deve-se ter o Chrome na maquina!!',
    author='Bruno Santana',
    options={'build_exe': {
        'include_files': arquivos,
        'include_msvcr': True # Permite que a aplicação rode em máquinas que não possuam o python
    }},
    executables=[configuracao]
)

