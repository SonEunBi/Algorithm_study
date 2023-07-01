import sys
import operator
from collections import defaultdict
read = sys.stdin.readline

book = defaultdict(int)
n = int(read().strip())
arr =[]
for i in range(n):
    k = input().rstrip()
    book[k] +=1

# book = sorted(book.items()) #오름차순으로 정렬
print(sorted(book.items(), key=lambda x : x[1], reverse=True)[0][0])


# maxkey = max(book.values())
# for k, v in book.items():
#     if v == maxkey:
#        arr.append(k)
# arr.sort()
# print(arr[0]) 