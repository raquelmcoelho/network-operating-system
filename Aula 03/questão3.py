print(r"3.Tente decodificar a nova sequência:b'\xff\xfeA\x00p\x00r\x00e\x00n\x00d\x00e\x00n\x00d\x00o\x00 "
      r"\x00p\x00r\x00o\x00g\x00r\x00a\x00m\x00a\x00\xe7\x00\xe3\x00o\x00 \x00e\x00m\x00 \x00P\x00y\x00t\x00h"
      r"\x00o\x00n\x00'")

print("decodificado:", b'\xff\xfeA\x00p\x00r\x00e\x00n\x00d\x00e\x00n\x00d\x00o\x00 \x00p\x00r\x00o\x00g\x00r\x00a\x00m'
                       b'\x00a\x00\xe7\x00\xe3\x00o\x00 \x00e\x00m\x00 \x00P\x00y\x00t\x00h\x00o'
                       b'\x00n\x00'.decode("utf-16"))

