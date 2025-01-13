from gui import criar_interface
from qrcode_generator import gerar_qrcode
import os

def main():
    # Diretório onde o script está sendo executado
    diretorio_atual = os.getcwd()
    
    # Inicializar a interface gráfica
    criar_interface(diretorio_atual)

if __name__ == "__main__":
    main()
