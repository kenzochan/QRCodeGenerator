import qrcode
from PIL import Image, ImageTk
from tkinter import messagebox
from datetime import datetime

def gerar_qrcode(entrada, entrada_caminho, qrcode_preview):
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
        qrcode_preview.config(image=img_tk)
        qrcode_preview.image = img_tk        

        messagebox.showinfo("Sucesso", f"QR Code gerado e salvo em:\n{caminho_completo}")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro ao gerar o QR Code:\n{e}")