
def hash_encrypt(hash_value: int):
    """
    Перебор всех 4-значных паролей (0000-9999) для восстановления пароля по хешу
    """
    found_passwords = []

    for num in range(10000):
        password = f"{num:04d}"

        if sum(ord(c) for c in password) % 10000 == hash_value:
            found_passwords.append(password)

    return found_passwords

