import pyautogui
import keyboard
import time

def main():
    print("Lütfen F10 tuşuna basarak işlemi başlatın...")
    while True:
        # F10'a basılması bekleniyor
        if keyboard.is_pressed("f10"):
            print("İşlem başlatılıyor...")
            time.sleep(0.5)  # Yanlışlıkla birden fazla algılamayı önlemek için bekleme
            break

    running = True
    while running:
        # F10 tekrar basıldığında işlemi durdurur
        if keyboard.is_pressed("f10"):
            print("İşlem durduruluyor...")
            time.sleep(0.5)  # Yanlış algılamayı önlemek için bekleme
            running = False
            break

        # Belirtilen işlemler
        pyautogui.click()  # Sol fare tuşuna tıkla
        time.sleep(3)  # 3 saniye bekleme
        pyautogui.press("a")  # "a" tuşuna bas
        pyautogui.press("d")  # "d" tuşuna bas

if __name__ == "__main__":
    main()
