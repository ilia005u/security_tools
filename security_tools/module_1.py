import random
import re
import math

def generate_password(lenght: int):
    """
    Напишите функцию, которая генерирует пароль заданной длины (буквы, цифры,
    символы). Вторая функция вычисляет энтропию пароля и оценивает его
    стойкость (слабый/средний/сильный).
    :param lenght:
    :return:
    """
    password = ""
    for i in range(lenght):
        password += random.choice("qwertyuiopasdfghjklzxcvbnm12345678!@#$%^&*()_-?/.<:;")

    return password


def calculate_entropy(password):
    """Расчет практической энтропии на основе используемых символов"""
    char_sets = {
        'lowercase': 26,
        'uppercase': 26,
        'digits': 10,
        'special': 32
    }

    used_sets = []

    if re.search(r'[a-z]', password):
        used_sets.append('lowercase')
    if re.search(r'[A-Z]', password):
        used_sets.append('uppercase')
    if re.search(r'\d', password):
        used_sets.append('digits')
    if re.search(r'[^a-zA-Z0-9]', password):
        used_sets.append('special')

    char_space = sum(char_sets[s] for s in used_sets)

    if char_space == 0:
        return 0

    entropy = len(password) * math.log2(char_space)

    return entropy


def xor_encrypt(text, key):
    """
    XOR шифрование
    """
    text_bytes = text.encode('utf-8')

    key_bytes = key.encode('utf-8')

    key_repeated = (key_bytes * (len(text_bytes) // len(key_bytes) + 1))[:len(text_bytes)]

    encrypted_bytes = bytes(a ^ b for a, b in zip(text_bytes, key_repeated))

    return encrypted_bytes


def xor_decrypt(encrypted_bytes, key):
    """
    Дешифрование XOR
    """
    key_bytes = key.encode('utf-8')
    key_repeated = (key_bytes * (len(encrypted_bytes) // len(key_bytes) + 1))[:len(encrypted_bytes)]

    decrypted_bytes = bytes(a ^ b for a, b in zip(encrypted_bytes, key_repeated))

    return decrypted_bytes.decode('utf-8')