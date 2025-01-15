import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter.ttk import Style
from qrcode_generator import gerar_qrcode
from utils import selecionar_local
from tkinter import Label

def criar_interface(diretorio_atual):
    root = tk.Tk()
    root.title("Gerador de QR Code")
    root.geometry("500x650")
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

    qrcode_preview_texto = ttk.Label(root, text="Prévia do QR Code:")
    qrcode_preview_texto.pack(pady=10)

    # Definindo o qrcode_preview como Label
    qrcode_preview = Label(root)
    qrcode_preview.pack(pady=5)

    style = ttk.Style()

    style.theme_use("clam")

    # Personalize o estilo do botão
    style.configure(
        "Custom.TButton",            # Nome do estilo
        font=("Arial", 14),          # Fonte e tamanho
        foreground="white",          # Cor do texto
        background="#1e90ff",        # Cor do fundo
        padding=10,                  # Espaçamento interno
        borderwidth=2,               # Largura da borda
        relief="raised"              # Estilo da borda
    )

    # Personalização do botão ao passar o mouse
    style.map(
        "Custom.TButton",
        foreground=[("active", "white")],  # Cor do texto ao passar o mouse
        background=[("active", "#4682b4")],  # Cor do fundo ao passar o mouse
        relief=[("pressed", "sunken")]  # Relevo ao pressionar
    )

    # Passando o qrcode_preview para a função gerar_qrcode
    botao_gerar = ttk.Button(root, text="Gerar QR Code", command=lambda: gerar_qrcode(entrada, entrada_caminho, qrcode_preview),style="Custom.TButton")
    botao_gerar.pack(side="bottom")
    botao_gerar.pack(pady=10)

    root.mainloop()
