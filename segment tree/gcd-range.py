# import math

# def construct(st,arr,l):
#     for i in range(l):
#         st[l+i] = arr[i]
#     for i in range(l-1,0,-1):
#         st[i] = math.gcd(st[i>>1],st[i>>1|1])

# def query(st,i,j,l):
#     res = 0

#     i += l
#     j += l

#     while i<j:
#         if i % 2 == 0:
#             res = math.gcd(res,st[i])
#             i += 1
#         if j % 2 == 0:
#             j -= 1
#             res = math.gcd(res,st[j])
#         i >>= 1
#         j >>= 1

#     return res


# arr = [2, 6, 10, 4, 7, 28, 9, 11, 6, 33] 
# l = len(arr)
# st = [0 for i in range(2*l)]

# construct(st,arr,l)
# print(query(st,4,7,l))

import math

def construct(st,arr,l):
    for i in range(l):
        st[l+i] = arr[i]
    for i in range(l-1,0,-1):
        st[i] = math.gcd(st[2*i],st[2*i+1])

def query(st,i,j,l):
    i += l
    j += l
    res = 0
    while i<j:
        if i%2!=0:
            res = math.gcd(res,st[i])
            i += 1
        if j%2!=0:
            j -= 1
            res = math.gcd(res,st[j])
        i //= 2
        j //= 2
    return res

arr = [2, 6, 10, 4, 7, 28, 9, 11, 6, 33]
l = len(arr)

st = [0 for i in range(2*l)]
construct(st,arr,l)

i,j = 4,6
print(arr)
print(arr[i:j])
print(query(st,i,j,l))