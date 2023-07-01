import sys
input = sys.stdin.readline

n = int(input())
nlist = list(map(int, input()))
nlist.sort()
print(round(sum(nlist)/n)) #1.산술평균
print(nlist[n//2]) #2.중앙값

ndict =dict()
for i in nlist:
    for i in ndict:
        ndict[i]+=1
maxi = max(ndict.values()) #빈도값 중 최대값
maxi_ndict =[]
for i in ndict:
    if maxi == ndict[i]:
        maxi_ndict.append(i)
        
    

print(nlist[n]-nlist[0])