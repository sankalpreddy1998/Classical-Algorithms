# def construct(st,arr,l):
#     for i in range(l):
#         st[l+i] = arr[i]
#     for i in range(l-1,0,-1):
#         st[i] = st[i<<1]+st[i<<1|1]

# def query(st,i,j,l):
#     res = 0

#     i += l
#     j += l

#     while i<j:
#         if i % 2 == 0:
#             res += st[i]
#             i += 1
#         if j % 2 == 0:
#             j -= 1
#             res += st[j]

#         i >>= 1
#         j >>= 1

#     return res

# arr = [2, 6, 10, 4, 7, 28, 9, 11, 6, 33] 
# l = len(arr)
# st = [0 for i in range(2*l)]

# construct(st,arr,l)
# print(query(st,4,6,l))

def construct(st,arr,l):
    for i in range(l):
        st[l+i] = arr[i]
    for i in range(l-1,0,-1):
        st[i] = st[2*i]+st[2*i+1]

def query(st,i,j,l):
    i += l
    j += l
    s = 0
    while i<j:
        if i%2!=0:
            s += st[i]
            i += 1
        if j%2!=0:
            j -= 1
            s += st[j]
        i //= 2
        j //= 2
    return s

arr = [2, 6, 10, 4, 7, 28, 9, 11, 6, 33]
l = len(arr)
st = [0 for i in range(2*l)]

construct(st,arr,l)
print(query(st,1,5,l))