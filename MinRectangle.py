def solution(sizes):
    answer = 0
    tag0 =0
    tag1 =0
    for nametag in sizes:
        if nametag[0] < nametag[1]:
            pass
        else:
            nametag[0], nametag[1] = nametag[1], nametag[0]
        if nametag[0] > tag0:
            tag0 = nametag[0]
        if nametag[1] > tag1:
            tag1 = nametag[1]
    answer = tag1 * tag0
    return answer