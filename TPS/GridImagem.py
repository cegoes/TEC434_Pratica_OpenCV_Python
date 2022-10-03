import cv2 as cv
from pathlib import Path

class GridImagem:
    # Mostra os 16 pontos distribuidos na imagem
    def mostraPontosImagem(self, imagem, listaPontos):
        for pontos in listaPontos:
            cv.circle(imagem,pontos,1,(0,255,255),-1)
        return imagem

    # Distribui 16 pontos homogeneos na imagem e retorna a lista dos pontos
    def calculaPontosImagem(self, imagem):
        rows, cols, _ = imagem.shape
        stepL = int((rows)/3)
        stepC = int((cols)/3)
        #print (stepL, stepC)
        source = list()
        passoLinhas = -1
        while(passoLinhas<rows):
            passoColunas = -1
            while(passoColunas<cols):
                gLinhas = passoLinhas
                gColunas = passoColunas
                if (passoLinhas==-1):
                    gLinhas = 0
                if (passoColunas==-1):
                    gColunas = 0
                source.append((gLinhas,gColunas))        
                #cv.circle(newMat_3ch,(gLinhas,gColunas),1,(255,0,255),-1)
                passoColunas = passoColunas + stepC
            passoLinhas = passoLinhas + stepL
        #print (source)
        return source

if __name__ == '__main__':
    caminho = Path('TPS/len_std.png')
    imagem = cv.imread(str(caminho),cv.IMREAD_ANYCOLOR)

    gImagem = GridImagem()
    pontos = gImagem.calculaPontosImagem(imagem)
    imagem = gImagem.mostraPontosImagem(imagem,pontos)

    cv.namedWindow('Imagem Pontos', 0)
    cv.imshow('Imagem Pontos', imagem)
    cv.waitKey()