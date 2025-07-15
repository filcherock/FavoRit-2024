import requests
import os
from tkinter import messagebox
import time
import sys
import ctypes
import elevate
def check_for_updates(current_version):
    # URL для проверки наличия обновлений
    update_url = "http://favorite.v96209al.beget.tech/data.php?key=version"

    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(update_url, headers=headers)
        latest_version = response.text.strip()

        if latest_version != current_version:
            print("Доступна новая версия:", latest_version)
            return True

    except requests.exceptions.RequestException as e:
        print("Ошибка при проверке обновлений:", e)

    return False


def download_update():
    result = messagebox.askyesno("Обновление", "Доступна новая версия. Скачать обновление?")
    if result:
        update_url = "http://favorite.v96209al.beget.tech/frsetup.exe"

        # Путь к исходной папке
        source_folder = "./"  # Укажите путь к исходной папке здесь

        try:
            headers = {'User-Agent': 'Mozilla/5.0'}
            response = requests.get(update_url, headers=headers)

            # Проверяем статус ответа
            if response.status_code == 200:
                # Имя файла
                file_name = "frsetup.exe"

                # Полный путь к файлу в исходной папке
                file_path = os.path.join(source_folder, file_name)

                # Сохраняем файл
                try:
                    with open(file_path, 'wb') as file:
                        file.write(response.content)
                except PermissionError:
                    messagebox.showerror("Ошибка", "Не удалось сохранить файл. Откройте файл от имени администратора.")

                return True
            else:
                print("Ошибка при загрузке обновления:", response.status_code)

        except requests.exceptions.RequestException as e:
            print("Ошибка при загрузке обновления:", e)

        return False
    else:
        os.system("start fr24.exe")
        sys.exit(0)

def apply_update():
    # Распаковка и установка обновления
    # Ваш код для распаковки и установки обновления

    # Пример:
    try:
        os.system("start frsetup.exe")
        os.remove("frsetup.exe")
    except PermissionError:
        messagebox.showerror("Ошибка", "Не удалось обновить программу. Откройте файл от имени администратора.")
        os.remove("frsetup.exe")



def main():

    current_version = "1.2"

    if check_for_updates(current_version):
        if download_update():
            apply_update()
    else:
        os.system("start fr24.exe")


if __name__ == "__main__":
    main()
