import json
import tkinter as tk

def salvar_dados(dados):
    with open('dados_coletados.json', 'w') as file:
        json.dump(dados, file)

def carregar_dados():
    try:
        with open('dados_coletados.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {'ufrpe': [], 'ufpe': [], 'marco_zero': [], 'parque': [], 'outros': []}
