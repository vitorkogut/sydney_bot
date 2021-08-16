import pyautogui
from time import sleep
sleep(2)


while True :
    sleep(2)
    im = pyautogui.screenshot(region=(2174 , 792, 352 , 112)) # aqui definir a caixa onde
    #o prog procura o sydeney, (x,y,tamnho_x,tamanho_y)

    local = pyautogui.locate('foto.png', im) # foto da cara do sydney

    print( local)

    if(local != None):
        pyautogui.moveTo(2282, 866) # local da mensagem mais recente
        

        pyautogui.click()
        pyautogui.click()
        pyautogui.click()


        pyautogui.hotkey('ctrl','c')

        #2278 × 918

        pyautogui.moveTo(2278,918) # local da caixa de msg
        pyautogui.click()

        sleep(0.1)
        pyautogui.hotkey('ctrl','v')
        sleep(0.1)
        pyautogui.hotkey('enter')
    else:
        print("n tem sydeney aqui")
