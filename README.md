# Automa-o_Dados_Furtos_Veiculos
Este projeto é uma automação desenvolvida para um freelancer. Consiste em entrar em um site do governo, fazer um scrapy de dados relacionados a "Furto de Veículos" de 2020 á 2022, e converter os arquivos baixados de xlsx para csv.

* main.py -> Arquivo principal do projeto. Consiste na manipulação das outras ferramentas e navegação do site.
* conversor.py -> Arquivo responsável pela ferramenta de conversão dos arquivos baixados em xls(arquivo antigo do excel) em xlsx(arquivo mais recente do excel). Ou seja, a ferramenta pega os arquivos de uma pasta chamada "Old Version" e transferi os arquivos, já convertidos, para a pasta "New Version".
* transferir.py -> Ferramenta responsável por transferir o arquivo baixado para a pasta "Old Version"(que consiste nos arquivos xls).
* ultimo_arquivo.py -> Ferramenta responsável por encontrar o arquivo baixado no pc.
* encontrar.py -> Ferramenta usada para encontrar a pasta "Automação Furto de Veículos" no computador. Usada quando o código é convertido em executável.

Tempo médio de execução do bot = Cada arquivo baixado demora 1 minuto e 40 segundos em média para ser liberado para download. Há 36 arquivos para serem baixados, 36 x 1.40 = 50 minutos.
