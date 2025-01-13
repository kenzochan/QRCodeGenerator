import tkinter as tk
from tkinter import ttk
from tkinter import messagebox, filedialog
import qrcode
from PIL import Image, ImageTk
from datetime import datetime
import os


# Função para gerar o QR Code
def gerar_qrcode():
    texto = entrada.get()
    caminho_salvar = entrada_caminho.get()
    
    if not texto.strip():
        messagebox.showwarning("Entrada inválida", "Por favor, insira um link ou texto para gerar o QR Code.")
        return

    if not caminho_salvar.strip():
        messagebox.showwarning("Caminho inválido", "Por favor, insira ou selecione uma pasta para salvar o QR Code.")
        return

    try:
        # Gerar o QR Code
        qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
        qr.add_data(texto)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white").convert("RGB")

        # Obter a data e hora atuais
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        # Criar o caminho completo do arquivo
        caminho_completo = f"{caminho_salvar}/qrcode_gerado_{timestamp}.png"
        img.save(caminho_completo)

        # Exibir a imagem no Tkinter
        img_tk = ImageTk.PhotoImage(img)
        label_preview.config(image=img_tk)
        label_preview.image = img_tk

        messagebox.showinfo("Sucesso", f"QR Code gerado e salvo em:\n{caminho_completo}")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro ao gerar o QR Code:\n{e}")

# Função para selecionar o diretório
def selecionar_local():
    caminho = filedialog.askdirectory(title="Selecione a pasta para salvar o QR Code")
    if caminho:
        entrada_caminho.delete(0, tk.END)
        entrada_caminho.insert(0, caminho)

# Configuração da janela principal
root = tk.Tk()
root.title("Gerador de QR Code")
root.geometry("500x600")
root.resizable(False, False)

# Label e entrada de texto para o link ou texto
label_instrucoes = ttk.Label(root, text="Digite o link ou texto:")
label_instrucoes.pack(pady=10)

entrada = ttk.Entry(root, width=50)
entrada.pack(pady=5)

# Label e entrada de texto para o local de salvamento
label_caminho = ttk.Label(root, text="Pasta para salvar o QR Code:")
label_caminho.pack(pady=10)

frame_caminho = ttk.Frame(root)
frame_caminho.pack(pady=5)

entrada_caminho = ttk.Entry(frame_caminho, width=40)
entrada_caminho.pack(side=tk.LEFT, padx=5)

# Diretório onde o script está sendo executado
diretorio_atual = os.getcwd()
entrada_caminho.insert(0, diretorio_atual)

botao_caminho = ttk.Button(frame_caminho, text="Selecionar", command=selecionar_local)
botao_caminho.pack(side=tk.LEFT)

# Botão para gerar QR Code
botao_gerar = ttk.Button(root, text="Gerar QR Code", command=gerar_qrcode)
botao_gerar.pack(pady=20)

# Label para exibir a prévia do QR Code
label_preview_texto = ttk.Label(root, text="Prévia do QR Code:")
label_preview_texto.pack(pady=10)

label_preview = ttk.Label(root)
label_preview.pack(pady=10)

# Iniciar o loop da interface gráfica
root.mainloop()
    