# Importa as bibliotecas OpenCV e pathlib
import cv2
from pathlib import Path

# Obtem o caminho completo para o diretório de cascata do OpenCV
caminhoHaarcascades = Path(cv2.data.haarcascades)

# Carrega os classificadores para detecção de rostos e sorrisos usando OpenCV
face_cascade=cv2.CascadeClassifier(str(caminhoHaarcascades / 'haarcascade_frontalface_default.xml'))
smile_cascade = cv2.CascadeClassifier(str(caminhoHaarcascades / 'haarcascade_smile.xml'))

# Inicializa o objeto VideoCapture para capturar o vídeo da webcam, geralmente a ID é 0.
cap = cv2.VideoCapture(0)

while cap.isOpened() and cv2.waitKey(1) == -1:
    # Captura um frame do vídeo
    ret, frame = cap.read()

    # Converte o frame para escala de cinza
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detecta faces no frame em escala de cinza
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    # Loop para processar cada face detectada
    for (x, y, w, h) in faces:
        # Desenha um retângulo ao redor da face detectada
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # Define a região de interesse (ROI) que contém a boca
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

        # Detecta sorrisos na ROI da boca
        #smile_cascade = cv2.CascadeClassifier('caminho_para_o_arquivo_xml_do_classificador_de_sorrisos')
        smiles = smile_cascade.detectMultiScale(roi_gray, scaleFactor=1.7, minNeighbors=22)

        # Verifica se há sorrisos na ROI da boca
        for (sx, sy, sw, sh) in smiles:
            cv2.rectangle(roi_color, (sx, sy), (sx+sw, sy+sh), (0, 0, 255), 1)

            # Se houver sorriso, exibe a mensagem "Sorriso detectado!"
            cv2.putText(frame, 'Sorriso detectado!', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    # Exibe o frame processado na janela
    cv2.imshow('Detector de sorrisos', frame)

# Libera os recursos
cap.release()
cv2.destroyAllWindows()
