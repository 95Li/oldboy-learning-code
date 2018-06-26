def isOneBitCharacter(bits):
    """
    :type bits: List[int]
    :rtype: bool
    """
    if bits == [0]:
        return True
    if not bits:
        return False
    st = str(bits[0])+str(bits[1])
    if st == '10' or st == '11':
        res = isOneBitCharacter(bits[2:len(bits)])
    else:
        res = isOneBitCharacter(bits[1:len(bits)])
    return res

# bits = [1, 0, 0]
bits = [1, 1, 1, 0]
print(isOneBitCharacter(bits))



