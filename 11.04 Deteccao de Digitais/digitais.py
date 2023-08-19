import cv2
from pathlib import Path

def find_best_match(imagemEntrada, pathComparacaoC):
    # Cria o detector SIFT
    #sift = cv2.xfea.SIFT_create()
    sift = cv2.SIFT_create()
    # Encontra os pontos-chave e descritores com SIFT
    kp1, des1 = sift.detectAndCompute(imagemEntrada,None)

    # Configuração do índice FLANN
    FLANN_INDEX_KDTREE = 0
    index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
    search_params = dict(checks=50)

    flann = cv2.FlannBasedMatcher(index_params, search_params)

    best_match_count = 0
    best_match_image_path = None
    match_points = []
    for file in (Path().glob(pathComparacaoC)):
        image_path = file
        caminhoImagem = Path(image_path)
        img2 = cv2.imread(str(caminhoImagem), cv2.IMREAD_GRAYSCALE)
        kp2, des2 = sift.detectAndCompute(img2,None)

        matches = flann.knnMatch(des1,des2,k=2)

        good_matches_count = 0
        for m,n in matches:
            if m.distance < 0.8*n.distance:
                good_matches_count += 1
                match_points.append(m)
        
        if good_matches_count > best_match_count:
            best_match_count = good_matches_count
            best_match_image_path = image_path

    return kp1,kp2,match_points,best_match_image_path

# Exemplo de uso da função find_best_match()
pathImagemEntrada = str(Path('11.04 Deteccao de Digitais/Finger-Print.tif'))
imagemEntradaC = cv2.imread(pathImagemEntrada,cv2.IMREAD_GRAYSCALE)
cv2.imshow('Imagem de Busca',imagemEntradaC)

pathComparacaoC = str(Path('11.04 Deteccao de Digitais/database/*.tif'))
match_points =[]
keypoints_1,keypoints_2,match_points,best_match_image_path = find_best_match(imagemEntradaC, pathComparacaoC)

if best_match_image_path != None:
    imgCorrespondente = cv2.imread(str(Path(best_match_image_path)))
    print(f'A imagem mais correspondente é: {best_match_image_path}')
    cv2.imshow('Imagem Correspondente',imgCorrespondente)
    result = cv2.drawMatches(imagemEntradaC, keypoints_1, imgCorrespondente, 
                        keypoints_2, match_points, None)     
    cv2.namedWindow("Resultado", cv2.WINDOW_NORMAL)
    cv2.imshow("Resultado", result)    
else:
    print('Nenhuma imagem correspondente detectada.')

cv2.waitKey(0)
cv2.destroyAllWindows()