from tkinter import messagebox
from PIL import Image
from datetime import datetime
import os


class Imagem:
    def __init__(self, caminho):
        """
        Inicializa a imagem a partir do caminho fornecido.
        """
        try:
            self.caminho = caminho
            self.imagem_original = Image.open(caminho).convert("RGB")
        except Exception as e:
            messagebox.showerror("Erro", f"Não foi possível abrir a imagem: {e}")
            self.imagem_original = None

    def aplicar_filtros(self, filtros):
        """
        Aplica uma lista de filtros à imagem original e retorna a imagem filtrada.
        """
        if not self.imagem_original:
            messagebox.showerror("Erro", "Imagem não carregada corretamente.")
            return None
        imagem = self.imagem_original
        for filtro in filtros:
            imagem = filtro.aplicar(imagem)
        return imagem

    def salvar_imagem(self, imagem, prefixo="imagem_filtrada"):
        """
        Salva a imagem filtrada em um arquivo com um prefixo e um timestamp.
        """
        if not imagem:
            return None
        pasta = "imagens modificadas"
        os.makedirs(pasta, exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        caminho = os.path.join(pasta, f"{prefixo}_{timestamp}.png")
        imagem.save(caminho)
        return caminho

    def resetar_imagem(self):
        """
        Retorna uma cópia da imagem original.
        """
        if not self.imagem_original:
            return None
        return self.imagem_original.copy()
