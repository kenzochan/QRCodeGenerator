import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from qrcode_generator import gerar_qrcode
from utils import selecionar_local
from tkinter import Label

def criar_interface(diretorio_atual):
    root = tk.Tk()
    root.title("Gerador de QR Code")
    root.geometry("500x600")
    root.resizable(False, False)

    label_instrucoes = ttk.Label(root, text="Digite o link ou texto:")
    label_instrucoes.pack(pady=10)

    entrada = ttk.Entry(root, width=50)
    entrada.pack(pady=5)

    label_caminho = ttk.Label(root, text="Pasta para salvar o QR Code:")
    label_caminho.pack(pady=10)

    frame_caminho = ttk.Frame(root)
    frame_caminho.pack(pady=5)

    entrada_caminho = ttk.Entry(frame_caminho, width=40)
    entrada_caminho.pack(side=tk.LEFT, padx=5)
    entrada_caminho.insert(0, diretorio_atual)

    botao_caminho = ttk.Button(frame_caminho, text="Selecionar", command=lambda: selecionar_local(entrada_caminho))
    botao_caminho.pack(side=tk.LEFT)

    label_preview_texto = ttk.Label(root, text="Prévia do QR Code:")
    label_preview_texto.pack(pady=10)

    # Definindo o label_preview como Label
    label_preview = Label(root)
    label_preview.pack(pady=10)

    # Passando o label_preview para a função gerar_qrcode
    botao_gerar = ttk.Button(root, text="Gerar QR Code", command=lambda: gerar_qrcode(entrada, entrada_caminho, label_preview))
    botao_gerar.pack(pady=20)

    root.mainloop()
