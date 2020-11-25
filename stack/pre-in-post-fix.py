def isOperator(s):
    if s in ['+','-','*','/']:
        return True
    else:
        return False

# ---------------------------------- prefix ---------------------------------- #

def prefix_to_infix(pre):
    st = []
    l = len(pre)

    for i in range(l-1,-1,-1):
        if isOperator(pre[i]):
            op1 = st.pop()
            op2 = st.pop()
            temp = "("+ op1 + pre[i] + op2 + ")"
            st.append(temp)
        else:
            st.append(pre[i])
    
    return st.pop()

def prefix_to_postfix(pre):
    st = []
    l = len(pre)

    for i in range(l-1,-1,-1):
        if isOperator(pre[i]):
            op1 = st.pop()
            op2 = st.pop()
            temp = op1+op2+pre[i]
            st.append(temp)
        else:
            st.append(pre[i])

    return st.pop()

# ----------------------------------- infix ---------------------------------- #

def infix_to_postfix(inf):
    st = []
    weight = {'+':1,'-':1,'*':2,'/':2,'^':3,'(':0}
    ans = ""

    for i in inf:
        if i.isalpha():
            ans += i
        elif i == "(":
            st.append(i)
        elif i == ")":
            while( len(st)!=0 and st[-1]!="("):
                ans += st.pop(-1)
            if len(st)!=0 and st[-1]!="(":
                return -1
            elif len(st)!=0 and st[-1]=="(":
                st.pop(-1)
        else:
            while(len(st)!=0 and weight[i]<=weight[st[-1]] ):
                if st[-1]=='(':
                    st.pop(-1)
                else:
                    ans += st.pop(-1)
            st.append(i)

    while len(st):
        ans += st.pop(-1)

    return ans
        
def infix_to_prefix(inf):
    r_inf = inf[::-1]
    for i in range(len(inf)):
        if r_inf[i]=='(':
            r_inf=r_inf[:i]+')'+r_inf[i+1:]
        elif r_inf[i]==')':
            r_inf=r_inf[:i]+'('+r_inf[i+1:]
    x = infix_to_postfix(r_inf)
    return x[::-1]

# ---------------------------------- postfix --------------------------------- #

def postfix_to_infix(pst):
    st = []
    l = len(pst)

    for i in range(l):
        if isOperator(pst[i]):
            op1 = st.pop()
            op2 = st.pop()
            temp = "("+op2+pst[i]+op1+")"
            st.append(temp)
        else:
            st.append(pst[i])

    return st.pop()

def postfix_to_prefix(pst):
    st = []
    l = len(pst)

    for i in range(l):
        if isOperator(pst[i]):
            op1 = st.pop()
            op2 = st.pop()
            temp = op2+op1+pst[i]
            st.append(temp)
        else:
            st.append(pst[i])

    return st.pop()

# ----------------------------------- main ----------------------------------- #

pre = "*-A/BC-/AKL"
inf = "a+b*(c^d-e)^(f+g*h)-i"
pst = "ABC/-AK/L-*"
print(prefix_to_infix(pre))
print(prefix_to_postfix(pre))
print(infix_to_postfix(inf))
print(infix_to_prefix(inf))
print(postfix_to_infix(pst))
print(postfix_to_prefix(pst))