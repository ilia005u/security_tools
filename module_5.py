from PIL import Image
import numpy as np
import os


class LSBSteganography:
    """Класс для сокрытия и извлечения данных методом LSB"""

    @staticmethod
    def text_to_bits(text: str) -> str:
        """Преобразование текста в битовую строку (исправлено)"""
        text_bytes = text.encode('utf-8')

        msg_length = len(text_bytes)
        length_bytes = msg_length.to_bytes(4, byteorder='big')

        full_data = length_bytes + text_bytes

        bits = ''
        for byte in full_data:
            bits += format(byte, '08b')

        return bits

    @staticmethod
    def bits_to_text(bits: str) -> str:
        """Преобразование битовой строки обратно в текст (исправлено)"""

        if len(bits) < 32:
            return ""

        length_bits = bits[:32]
        msg_length = int(length_bits, 2)

        total_needed = 32 + msg_length * 8
        if len(bits) < total_needed:
            return ""

        message_bits = bits[32:32 + msg_length * 8]

        message_bytes = bytearray()
        for i in range(0, len(message_bits), 8):
            byte_bits = message_bits[i:i + 8]
            if len(byte_bits) == 8:
                message_bytes.append(int(byte_bits, 2))

        try:
            return message_bytes.decode('utf-8')
        except:
            return ""

    @staticmethod
    def hide_message(image_path: str, message: str, output_path: str):
        """Сокрытие сообщения в изображении методом LSB"""
        # Проверяем существование файла
        if not os.path.exists(image_path):
            raise FileNotFoundError(f"Файл {image_path} не найден!")

        img = Image.open(image_path)
        img = img.convert('RGB')
        pixels = np.array(img)

        bits = LSBSteganography.text_to_bits(message)

        height, width, channels = pixels.shape

        max_bits = height * width * channels
        if len(bits) > max_bits:
            raise ValueError(f"Сообщение слишком большое! Нужно {len(bits)} бит, доступно {max_bits}")

        bit_index = 0
        for i in range(height):
            for j in range(width):
                for k in range(channels):
                    if bit_index < len(bits):
                        pixel_value = pixels[i, j, k]
                        if bits[bit_index] == '1':
                            pixels[i, j, k] = pixel_value | 1
                        else:
                            pixels[i, j, k] = pixel_value & ~1
                        bit_index += 1

        result_img = Image.fromarray(pixels)
        result_img.save(output_path)

        return pixels

    @staticmethod
    def extract_message(image_path: str) -> str:
        """Извлечение сообщения из изображения методом LSB"""
        if not os.path.exists(image_path):
            raise FileNotFoundError(f"Файл {image_path} не найден!")

        img = Image.open(image_path)
        img = img.convert('RGB')
        pixels = np.array(img)

        height, width, channels = pixels.shape

        max_bits_to_extract = height * width * channels

        bits = ''
        for i in range(height):
            for j in range(width):
                for k in range(channels):
                    bits += str(pixels[i, j, k] & 1)

                    if len(bits) >= 32:
                        temp_text = LSBSteganography.bits_to_text(bits)
                        if temp_text and len(temp_text) > 0:
                            if len(bits) >= 32:
                                length_bits = bits[:32]
                                msg_length = int(length_bits, 2)
                                needed_bits = 32 + msg_length * 8
                                if len(bits) >= needed_bits:
                                    return temp_text

        return LSBSteganography.bits_to_text(bits)

