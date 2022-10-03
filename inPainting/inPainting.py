import cv2 as cv
from pathlib import Path

caminhoImagem = Path('Anexos, Imagens e Videos')

src = cv.imread(str(caminhoImagem / 'ex1.jpg'))
mask = cv.imread(str(caminhoImagem / 'ex1mask.png'))
mask = cv.cvtColor(mask, cv.COLOR_BGR2GRAY)

# Apply the inpainting algorithms
dst = cv.inpaint(src, mask, 5, cv.INPAINT_TELEA)
dst2 = cv.inpaint(src, mask, 5, cv.INPAINT_NS)

# Show the results
cv.namedWindow( " ORIGINAL ", cv.WINDOW_AUTOSIZE )
cv.imshow( " ORIGINAL ", src )
cv.namedWindow( " MASK ", cv.WINDOW_AUTOSIZE )
cv.imshow( " MASK ", mask )
cv.namedWindow(" INPAINT_TELEA ", cv.WINDOW_AUTOSIZE )
cv.imshow( " INPAINT_TELEA ", dst );
cv.namedWindow(" INPAINT_NS ", cv.WINDOW_AUTOSIZE )
cv.imshow( " INPAINT_NS ", dst2 )

cv.waitKey()


