from tkinter import filedialog

def selecionar_local(entrada_caminho):
    caminho = filedialog.askdirectory(title="Selecione a pasta para salvar o QR Code")
    if caminho:
        entrada_caminho.delete(0, tk.END)
        entrada_caminho.insert(0, caminho)
