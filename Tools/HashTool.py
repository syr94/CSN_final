
import zlib

class HashTool:

    def __init__(self):
        pass

    def crc32(input_data : str) -> int:
        return zlib.crc32(input_data)