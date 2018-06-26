def backspaceCompare(S, T):
    """
    :type S: str
    :type T: str
    :rtype: bool
    """
    if S or T:
        if S == T:
            return True

    sindex = len(S)
    new_S = list(S)
    for i in range(sindex):
        if S[i] == '#':
            index = new_S.index(S[i])
            if not (index == 0):
                new_S.pop(index - 1)
            new_S.remove(S[i])

    tindex = len(T)
    new_T = list(T)
    for i in range(tindex):
        if T[i] == '#':
            index = new_T.index(T[i])
            if not (index == 0):
                new_T.pop(index- 1)
            new_T.remove(T[i])

    return new_T == new_S


if __name__ == '__main__':
    # S = "ab#c"
    # T = "ad#c"

    # S = "ab##"
    # T = "c#d#"

    # S = "a##c"
    # T = "#a#c"

    S = "a#c"
    T = "b"
    res = backspaceCompare(S, T)
    print(res)
