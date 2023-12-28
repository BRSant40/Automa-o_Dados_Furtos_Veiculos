import os
def encontrar_pasta():
    caminhos = list()
    for pasta, sub_pastas, arquivos in os.walk(os.environ['USERPROFILE']):
        if 'Automação_furto_veiculos' in pasta:
            caminhos.append(pasta)
            break
        if not sub_pastas:
            continue
        else:
            for sub in sub_pastas:
                if 'Automação_furto_veiculos' in sub:
                    caminhos.append(sub)
                    break

    #for c in caminhos:
        #if 'Automação_furto_veiculos' in c:
            #return c
    return caminhos[1]

#print(encontrar_pasta())