from PIL import ImageFilter, ImageOps

class Filtro:
    def aplicar(self, imagem):
        pass

class EscalaCinza(Filtro):
    def aplicar(self, imagem):
        return imagem.convert("L")

class PretoBranco(Filtro):
    def aplicar(self, imagem):
        return imagem.convert("1")

class Cartoon(Filtro):
    def aplicar(self, imagem):
        return imagem.filter(ImageFilter.FIND_EDGES)

class FotoNegativa(Filtro):
    def aplicar(self, imagem):
        return ImageOps.invert(imagem)

class Contorno(Filtro):
    def aplicar(self, imagem):
        return imagem.filter(ImageFilter.CONTOUR)

class Blurred(Filtro):
    def aplicar(self, imagem):
        return imagem.filter(ImageFilter.BLUR)