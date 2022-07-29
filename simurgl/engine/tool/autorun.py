from winreg import *

sub_key = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Run'
# Путь в реестре
key_my = OpenKey(HKEY_CURRENT_USER,
                 sub_key,
                 0, KEY_ALL_ACCESS)


def ar_add(path):
    try:
        SetValueEx(key_my, "Simurgl", 0, REG_SZ, f'{path}\\test.py')
    except OSError:
        print("Запись уже есть")


def ar_remove(path):
    # Удалить из автозагрузки
    try:
        DeleteValue(key_my, "Simurgl")
    except FileNotFoundError:
        print("В реестре нет такой записи")
