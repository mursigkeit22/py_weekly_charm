import struct
import ctypes
import sys
# Use sys.byteorder to check the endianness of your system.
print(sys.byteorder)
# Встроенная функция id() возвращает адрес памяти,
# где хранится объект (сам объект является C структурой)
# Чтобы считать данные по адресу памяти, нужно воспользоваться функцией string_at из модуля ctypes.
# ctypes.string_at(address, size=-1)
# This function returns the C string starting at memory address "address" as a bytes object.
# If size is specified, it is used as size, otherwise the string is assumed to be zero-terminated.

# Теперь попробуем считать данные по адресу, который вернул нам id():
obj = 2
print(id(2))
# print(id(500))
print(id(int))
print('======')
print(ctypes.string_at(id(obj), 28))
obj = 1
print(ctypes.string_at(id(obj), 28))
obj = 1152921504606846976  # 2**60
print(ctypes.string_at(id(obj), 36))
