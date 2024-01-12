import os
import requests
import sys
import subprocess
import tkinter as tk
from tkinter import filedialog
from tkinter import simpledialog
from tkinter import messagebox

def select_folder():
    root = tk.Tk()
    root.withdraw()  # Oculta a janela principal

    folder_selected = filedialog.askdirectory(title="Selecione uma pasta para salvar as imagens")

    if folder_selected:
        print(f"Pasta selecionada: {folder_selected}")
        return folder_selected	
    else:
        print("Nenhuma pasta selecionada.")
        return False

def download_image(number, save_folder):
    url = f'http://cdn.stardoll.com/itemimages/76/0/98/{number}.png'
    response = requests.get(url)

    if response.status_code == 200:
        image_content = response.content
        save_path = os.path.join(save_folder, f'{number}.jpg')

        with open(save_path, 'wb') as file:
            file.write(image_content)

        print(f'Imagem {number}.png baixada e salva em {save_path}')
        return True
    elif response.status_code == 404:
        print(f'Imagem {number}.png não encontrada (Erro 404)')
        return False
    else:
        print(f'Falha ao baixar imagem {number}.jpg (Código de status: {response.status_code})')
        return False

def get_user_input():
    root = tk.Tk()
    root.withdraw()  # Oculta a janela principal

    user_input = simpledialog.askstring("Stardoll Scrapper", "Digite o número da última imagem da última coleção:")

    if user_input is not None:
        print(f"Último: {user_input}")
        return user_input
    else:
        print("Nenhum valor foi inserido.")
        return False	

if __name__ == "__main__":
	number = int(get_user_input())
	if(number == False):
		sys.exit()	
	begin_number = number
	number += 1 # Próxima imagem, a primeira da nova coleção
	folder = select_folder()
	if(folder == False):
		sys.exit()
	count = 0
	while True:
		if (not download_image(number, folder)):
			break
		number += 1
		download_image(number, folder)
		count = number - 1 - begin_number
	messagebox.showinfo('Stardoll Scrapper',f'Foram baixadas {count} imagens.')




