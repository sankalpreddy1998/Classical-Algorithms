# def construct(st,arr,l):
#     for i in range(l):
#         st[l+i] = arr[i]
#     for i in range(l-1,0,-1):
#         st[i] = max(st[2*i],st[2*i+1])

# def max_query(st,i,j,l):
#     i += l
#     j += l
#     m = -999999
#     while i<j:
#         if i%2!=0:
#             m = max(m,st[i])
#             i += 1
#         if j%2!=0:
#             j -= 1
#             m = max(m,st[j]) 
#         i //= 2
#         j //= 2
#     return m

# arr = [2, 6, 10, 4, 7, 28, 9, 11, 6, 33] 
# l = len(arr)
# st = [0 for i in range(2*l)]

# construct(st,arr,l)
# print(max_query(st,6,9,l))

def construct(st,arr,l):
    for i in range(l):
        st[l+i] = arr[i]
    for i in range(l):
        st[i] = max(st[2*i],st[2*i+1])

def max_query(st,i,j,l):
    i += l
    j += l
    mx = -999999
    while i<j:
        if i%2!=0:
            mx = max(mx,st[i])
            i += 1
        if j%2!=0:
            j -= 1
            mx = max(mx,st[j])
        i //= 2
        j //= 2
    return mx

arr = [2, 6, 10, 4, 7, 28, 9, 11, 6, 33]
l = len(arr)

st = [0 for i in range(2*l)]

construct(st,arr,l)
print(max_query(st,6,9,l))