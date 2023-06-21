# os.listdir para navegar em caminhos
# /Users/luizotavio/Desktop/EXEMPLO
# C:\Users\luizotavio\Desktop\EXEMPLO
# caminho = r'C:\\Users\\luizotavio\\Desktop\\EXEMPLO'
# print(caminho)

import os

caminho = os.path.join('C:\\Users', 'dai_v', 'Python', 'aulas')
# print(caminho)

for folder in os.listdir(caminho):
    caminho_completo_folder = os.path.join(caminho, folder)
    print(folder)

    if not os.path.isdir(caminho_completo_folder):
        continue

    for txt in os.listdir(caminho_completo_folder):
        print('  ', txt)
