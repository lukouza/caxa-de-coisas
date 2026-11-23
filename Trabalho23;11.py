# Controle de estacionamento
# Estacionamento possui 50 vagas

import tkinter as tk
from tkinter import messagebox

# Vaga 0 não é usada; índices válidos vão de 1 a 50
vagas = ["LIVRE"] * 51
tempo_escolhido = 0
entrada_vaga = None
entrada_placa = None
janela_menu = None

#Calculo do valor escolhido
def calcular_valor(tempo):
    valores = {
        1: 10,
        2: 18,
        3: 30,
        4: 50,
    }
    return valores.get(tempo, 0)

#Mostra as vagas totais e ocupadas
def mostrar_vagas():
    janela_vagas = tk.Toplevel(janela_menu)
    janela_vagas.title("Vagas")
    janela_vagas.geometry("320x420")

    area_texto = tk.Text(janela_vagas, width=36, height=22, state="normal")
    area_texto.pack(padx=10, pady=10)

    for numero in range(1, 51):
        status = vagas[numero]
        linha = f"Vaga {numero:02d} - {status}\n"
        area_texto.insert(tk.END, linha)

    area_texto.config(state="disabled")

#funcao para escolher tempo
def escolher_tempo(opcao):
    global tempo_escolhido
    tempo_escolhido = opcao

#funcao para confirmar a vaga ocupada
def confirmar_ocupar():
    global tempo_escolhido

    texto_vaga = entrada_vaga.get().strip()
    placa = entrada_placa.get().strip().upper()

    if not texto_vaga.isdigit():
        messagebox.showwarning("Erro", "Digite um número de vaga válido.")
        return

    vaga = int(texto_vaga)

    if vaga < 1 or vaga > 50:
        messagebox.showwarning("Erro", "Vaga inválida! Escolha entre 1 e 50.")
    elif vagas[vaga] != "LIVRE":
        messagebox.showwarning("Erro", "Vaga já ocupada!")
    elif not placa:
        messagebox.showwarning("Erro", "Informe a placa do veículo.")
    elif tempo_escolhido == 0:
        messagebox.showwarning("Erro", "Escolha o tempo de permanência.")
    else:
        valor = calcular_valor(tempo_escolhido)
        vagas[vaga] = placa
        messagebox.showinfo(
            "OK",
            f"Vaga {vaga} ocupada!\nPlaca: {placa}\nValor: R$ {valor}",
        )
        tempo_escolhido = 0

# funcao para ocupar vaga 
def ocupar_vaga():
    global entrada_vaga, entrada_placa, tempo_escolhido
    tempo_escolhido = 0

    janela_ocupar = tk.Toplevel(janela_menu)
    janela_ocupar.title("Ocupar vaga")

    tk.Label(janela_ocupar, text="Número da vaga (1 a 50):").pack(pady=(10, 0))
    entrada_vaga = tk.Entry(janela_ocupar)
    entrada_vaga.pack()

    tk.Label(janela_ocupar, text="Placa do veículo:").pack(pady=(8, 0))
    entrada_placa = tk.Entry(janela_ocupar)
    entrada_placa.pack()

    tk.Label(janela_ocupar, text="Escolha o tempo:").pack(pady=(10, 2))
    tk.Button(janela_ocupar, text="1 hora - R$ 10", command=lambda: escolher_tempo(1)).pack(fill="x", padx=20, pady=1)
    tk.Button(janela_ocupar, text="2 horas - R$ 18", command=lambda: escolher_tempo(2)).pack(fill="x", padx=20, pady=1)
    tk.Button(janela_ocupar, text="4 horas - R$ 30", command=lambda: escolher_tempo(3)).pack(fill="x", padx=20, pady=1)
    tk.Button(janela_ocupar, text="12 horas - R$ 50", command=lambda: escolher_tempo(4)).pack(fill="x", padx=20, pady=1)

    tk.Button(janela_ocupar, text="Confirmar", command=confirmar_ocupar).pack(pady=10)

# funcao para confirmar a liberação da vaga
def confirmar_liberar():
    texto_vaga = entrada_vaga.get().strip()

    if not texto_vaga.isdigit():
        messagebox.showwarning("Erro", "Digite um número de vaga válido.")
        return

    vaga = int(texto_vaga)

    if vaga < 1 or vaga > 50:
        messagebox.showwarning("Erro", "Vaga inválida! Escolha entre 1 e 50.")
    elif vagas[vaga] == "LIVRE":
        messagebox.showwarning("Erro", "Vaga já está livre!")
    else:
        vagas[vaga] = "LIVRE"
        messagebox.showinfo("OK", f"Vaga {vaga} liberada!")

#funcao para liberar a vaga
def liberar_vaga():
    global entrada_vaga

    janela_liberar = tk.Toplevel(janela_menu)
    janela_liberar.title("Liberar vaga")

    tk.Label(janela_liberar, text="Número da vaga (1 a 50):").pack(pady=(10, 0))
    entrada_vaga = tk.Entry(janela_liberar)
    entrada_vaga.pack()

    tk.Button(janela_liberar, text="Liberar", command=confirmar_liberar).pack(pady=10)

#funcao para mostrar menu
def mostrar_menu():
    global janela_menu

    janela_menu = tk.Tk()
    janela_menu.title("Estacionamento")
    janela_menu.geometry("260x200")

    tk.Label(janela_menu, text="--- CONTROLE DE ESTACIONAMENTO ---").pack(pady=10)
    tk.Button(janela_menu, text="1 - Ver vagas", command=mostrar_vagas).pack(fill="x", padx=30, pady=2)
    tk.Button(janela_menu, text="2 - Ocupar vagas", command=ocupar_vaga).pack(fill="x", padx=30, pady=2)
    tk.Button(janela_menu, text="3 - Liberar vagas", command=liberar_vaga).pack(fill="x", padx=30, pady=2)
    tk.Button(janela_menu, text="4 - Sair", command=janela_menu.destroy).pack(fill="x", padx=30, pady=6)

    janela_menu.mainloop()


mostrar_menu()
