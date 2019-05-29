def hex2int(xHex):

    xInteger = 0
    hexLen = len(xHex)
    for k in range(hexLen):
        c = xHex[hexLen-1-k]
        hexChar = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
        for j in range(len(hexChar)):
            if c == hexChar[j]:
                xInteger += j*(16**k)
    return int(xInteger)

def int2hex(xInteger):

    xHex = ""
    hexChar = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    while xInteger > 0:
        xHex = hexChar[xInteger%16] + xHex
        xInteger = xInteger // 16

    return xHex
    
