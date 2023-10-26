def solution(wallpaper):
    minx, miny, maxx, maxy = 51,51,0,0
    #가장 왼쪽, 가장 오른쪽, 가장 위쪽, 가장 아래쪽
    for i in range(0, len(wallpaper)):
        for j in range(0, len(wallpaper[0])):
            if wallpaper[i][j] == '#':
                miny = min(miny, i)
                minx = min(minx, j)
                maxy = max(maxy, i+1)
                maxx= max(maxx, j+1)
    
    return [miny, minx, maxy, maxx]