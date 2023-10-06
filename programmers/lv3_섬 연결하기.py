def solution(n, costs):
    answer =0
    parent =[i for i in range(n)]
    costs.sort(key = lambda x:x[2])
    
    def sameParent(parent, a,b):
        return getParent(parent, a) == getParent(parent, b)

    def getParent(parent, x):
        if parent[x] == x:
            return x
        return getParent(parent, parent[x])

    def unionParent(parent, a,b):
        a=getParent(parent, a)
        b = getParent(parent, b)
        if a<b:
            parent[b] =a
        else:
            parent[a]=b
            
    for a,b,cost in costs:
        if sameParent(parent, a,b) == False:
            unionParent(parent, a,b)
            answer += cost
    
    return answer

