def valid_binary(value):
    if len(value) != 8:
        return False
    else:
        value = str(value)
        for num in range(len(str(value))):
            if value[num] != "0" and value[num] != "1":
                return False
        else:
            return True

def hamming_distance(bin1, bin2):
    if not valid_binary(bin1) or not valid_binary(bin2):
        print("Invalid input")
        return
    else:
        hamming = []
        for i in range(8):
            if bin1[i] != bin2[i]:
                hamming.append("1")
            else:
                hamming.append("0")
        new = "".join(hamming)
        final = int(new)
        return final
