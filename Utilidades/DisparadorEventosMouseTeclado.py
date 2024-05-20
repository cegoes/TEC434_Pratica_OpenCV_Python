#pip install pyautogui

import pyautogui

# Mover o mouse para as coordenadas (100, 200)
pyautogui.moveTo(100, 200)

# Clicar com o botão esquerdo do mouse
pyautogui.click()

# Clicar com o botão direito do mouse
pyautogui.click(button='right')

# Pressionar uma tecla
pyautogui.press('enter')

# Digitar um texto
pyautogui.typewrite('Hello, World!')

# Pressionar uma combinação de teclas
pyautogui.hotkey('ctrl', 'c')