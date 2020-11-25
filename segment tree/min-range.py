# def construct(st,arr,l):
#     for i in range(l):
#         st[l+i] = arr[i]
#     for i in range(l-1,0,-1):
#         st[i] = min(st[2*i],st[2*i+1])

# def min_query(st,i,j,l):
#     i += l
#     j += l
#     mi = 1e9
#     while i<j:
#         if i % 2 != 0:
#             mi = min(mi,st[i])
#             i += 1
#         if j % 2 != 0:
#             j -= 1
#             mi = min(mi,st[j])
#         i //= 2
#         j //= 2
#     return mi

# arr = [2, 6, 10, 4, 7, 28, 9, 11, 6, 33] 
# l = len(arr)
# st = [0 for i in range(2*l)]

# construct(st,arr,l)
# print(min_query(st,4,8,l))


def construct(at,arr,l):
    for i in range(l):
        st[l+i] = arr[i]
    for i in range(l):
        st[i] = min(st[2*i],st[2*i+1])

def min_query(st,i,j,l):
    i += l
    j += l
    mi = 1e9
    while i<j:
        if i%2!=0:
            mi = min(mi,st[i])
            i += 1
        if j%2!=0:
            j -= 1
            mi = min(mi,st[j])
        i //= 2
        j //= 2
    return mi

arr = [2, 6, 10, 4, 7, 28, 9, 11, 6, 33]
l = len(arr)

st = [0 for i in range(2*l)]
construct(st,arr,l)
print(min_query(st,4,8,l))