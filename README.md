
# Лабораторная работа: Методы сокрытия и анализа информации

## Описание

В рамках данного проекта реализованы три ключевых подхода к работе с информацией:

- Генерация паролей и оценка их устойчивости
- Восстановление паролей по хеш-значениям
- Встраивание данных в графические изображения с использованием метода LSB

## Структура проекта

- `module_1.py` – создание паролей, расчёт энтропии, шифрование с помощью XOR
- `module_2.py` – подбор 4-значных паролей на основе хеша
- `module_5.py` – LSB-стеганография (скрытие и извлечение текста из изображений)
- `main.py` – демонстрационный пример работы с `module_1`

## Модуль 1 (`module_1.py`)

**Предоставляемые функции:**

- `generate_password(length)` – создаёт случайный пароль указанной длины, используя буквы, цифры и специальные символы
- `calculate_entropy(password)` – оценивает энтропию пароля, исходя из набора использованных символов
- `xor_encrypt(text, key)` – выполняет XOR-шифрование переданного текста
- `xor_decrypt(encrypted_bytes, key)` – выполняет XOR-расшифрование данных

## Модуль 2 (`module_2.py`)

**Предоставляемые функции:**

- `hash_encrypt(hash_value)` – осуществляет перебор всех возможных 4-значных паролей (от `0000` до `9999`) и возвращает те, хеш которых (вычисленный как сумма ASCII-кодов по модулю 10000) совпадает с заданным значением

## Модуль 5 (`module_5.py`)

**Класс `LSBSteganography`:**

- `text_to_bits(text)` – преобразует текстовое сообщение в битовую строку с предварительным добавлением информации о длине сообщения
- `bits_to_text(bits)` – выполняет обратное преобразование битовой строки в текст
- `hide_message(image_path, message, output_path)` – скрывает сообщение в изображении путём замены младших битов пикселей
- `extract_message(image_path)` – извлекает скрытое сообщение из изображения

## `main.py`

Демонстрирует процесс генерации пароля и расчёт его энтропии.

## Зависимости

- Python 3.x
- Pillow (PIL)
- NumPy

## Установка

```bash
pip install -r requarements.txt
```

# Использование

## Генерация пароля и вычисление энтропии
``` python
from security_tools.module_1 import generate_password, calculate_entropy

password = generate_password(10)
entropy = calculate_entropy(password)
```
## XOR-шифрование
``` python

from security_tools.module_1 import xor_encrypt, xor_decrypt

encrypted = xor_encrypt("текст", "ключ")
decrypted = xor_decrypt(encrypted, "ключ")
```
## Восстановление пароля по хешу
``` python

from security_tools.module_2 import hash_encrypt

passwords = hash_encrypt(202)  # возвращает список найденных паролей
```
## Сокрытие сообщения в изображении
``` python
from security_tools.module_5 import LSBSteganography
```

# Сокрытие данных
``` python
LSBSteganography.hide_message("input.png", "секретное сообщение", "output.png")
```
# Извлечение данных
``` python
message = LSBSteganography.extract_message("output.png")
```
### Запуск main.py
```bash
python main.py
```
