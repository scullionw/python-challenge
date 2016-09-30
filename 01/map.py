__author__ = 'williamscullion'

a = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
c = "map"
b = []
for i, j in enumerate(a):
    if 97 <= ord(j) <= 120:
        z = ord(j) + 2
    elif ord(j) == 122:
        z = 98
    elif ord(j) == 121:
        z = 97
    else:
        z = ord(j)

    b.append(chr(z))

print("".join(b))
print(a)

print(ord("z"))
