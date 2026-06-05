from security_tools.module_1 import *


password = generate_password(10)
print(password)

entropy = calculate_entropy(password)
print(entropy)

