import struct

raw = b"\x00\x00\x00\x2A"

big    = struct.unpack("!I", raw)[0]
little = struct.unpack("<I", raw)[0]
inversé = struct.unpack(">I", raw[::-1])[0]

print(f"big-endian                : {big}")
print(f"little-endian             : {little}")
print(f"inversé puis big-endian   : {inversé}")
print(f"little == inversé         : {little == inversé}")


#### réponse au bonus ####

'''
Lire en little-endian, c'est par définition lire les octets dans l'ordre inversé par rapport au big-endian. Inverser les octets manuellement puis lire en big-endian produit exactement la même opération, vu que les deux chemins aboutissent au même ordre d'octets avant interprétation le résultat est nécessairement identique.


'''

