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

def adicionar_locais():
    local = local_var.get()
    condi = condi_entry.get()
    detalhes = detalhes_entry.get()
    especie = especie_entry.get()
    quantidade = quantidade_entry.get()
    detalhese = detalhese_entry.get()

    if local == "outros":
        
        local = outros_entry.get()
        if 'outros' not in dados_coletados:
            dados_coletados['outros'] = []
        dados_coletados['outros'].append({'condições ambientais': condi, 'Detalhes das condições ambientais': detalhes, 'Espécie': especie, 'Quantidade': quantidade, 'Detalhes da espécie': detalhese, 'Local': local})
    else:
        dados_coletados[local.lower().replace(" ", "_")].append({'condições ambientais': condi, 'Detalhes das condições ambientais': detalhes, 'Espécie': especie, 'Quantidade': quantidade, 'Detalhes da espécie': detalhese})
    salvar_dados(dados_coletados)

def selecionar_local(local):
    if local == "outros":
        outros_label.grid()
        outros_entry.grid()
    else:
        outros_label.grid_remove()
        outros_entry.grid_remove()

def visualizar_dados():
    dados_text.delete(1.0, tk.END)
    for local, dados in dados_coletados.items():
        dados_text.insert(tk.END, f'{local.capitalize()}:\n')
        for d in dados:
            dados_text.insert(tk.END, f'{d}\n')

dados_coletados = carregar_dados()


root = tk.Tk()
root.title("MonoBio")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

expli_label = tk.Label(frame, text="Use os espaços abaixo para adicionar os dados.\n")
expli_label.grid(row=0, column=0, columnspan=2)

local_label = tk.Label(frame, text="Local:")
local_label.grid(row=1, column=0, sticky="w")
local_var = tk.StringVar(root)
local_var.set("UFRPE")
local_dropdown = tk.OptionMenu(frame, local_var, "UFRPE", "UFPE", "Marco Zero", "Parque da Jaqueira", "outros", command=selecionar_local)
local_dropdown.grid(row=1, column=1, pady=5)

condi_label = tk.Label(frame, text="condições ambientais:")
condi_label.grid(row=2, column=0, sticky="w")
condi_entry = tk.Entry(frame)
condi_entry.grid(row=2, column=1, pady=5)

detalhes_label = tk.Label(frame, text="Detalhes das condições ambientais:")
detalhes_label.grid(row=3, column=0, sticky="w")
detalhes_entry = tk.Entry(frame)
detalhes_entry.grid(row=3, column=1, pady=5)

especie_label = tk.Label(frame, text="Espécie:")
especie_label.grid(row=4, column=0, sticky="w")
especie_entry = tk.Entry(frame)
especie_entry.grid(row=4, column=1, pady=5)

quantidade_label = tk.Label(frame, text="Quantidade da espécie:")
quantidade_label.grid(row=5, column=0, sticky="w")
quantidade_entry = tk.Entry(frame)
quantidade_entry.grid(row=5, column=1, pady=5)

detalhese_label = tk.Label(frame, text="Detalhes da espécie:")
detalhese_label.grid(row=6, column=0, sticky="w")
detalhese_entry = tk.Entry(frame)
detalhese_entry.grid(row=6, column=1, pady=5)


outros_label = tk.Label(frame, text="Informe o local:")
outros_label.grid(row=7, column=0, sticky="w")
outros_label.grid_remove() 
outros_entry = tk.Entry(frame)
outros_entry.grid(row=7, column=1, pady=5)
outros_entry.grid_remove()  

adicionar_especies_button = tk.Button(frame, text="Adicionar Dados", command=adicionar_locais)
adicionar_especies_button.grid(row=8, columnspan=2, pady=10)

visualizar_button = tk.Button(frame, text="Visualizar Dados", command=visualizar_dados)
visualizar_button.grid(row=9, columnspan=2, pady=10)

dados_text = tk.Text(root, height=10, width=60)
dados_text.pack(padx=10, pady=10)


root.mainloop()