# Chiffrage XOR
def c_xor (m , k):
    '''
    Chiffrement
    '''
    etendre =''
    compteur = 0
    while len(etendre)!=len(m):
        etendre += k[compteur]
        compteur += 1
        if compteur == 3:
            compteur = 0
    a=[]
    b=[]
    s=''
    for k in range(len(m)):
        a.append(ord(etendre[k]))
        b.append(ord(m[k]))
        s+=chr(a[k] ^ b[k])
    return s

def d_xor(s,k):
    return c_xor(s,k)

def c_xor (m , k):
    etendre =''
    compteur = 0
    while len(etendre)!=len(m):
        etendre += k[compteur]
        compteur += 1
        if compteur == 3:
            compteur = 0
    a=[]
    b=[]
    s=''
    for k in range(len(m)):
        a.append(ord(etendre[k]))
        b.append(ord(m[k]))
        s+=chr(a[k] ^ b[k])
    return s

def d_xor(s,k):
    '''
    Déchiffrement
    '''
    return c_xor(s,k)

cle='testnumeroun'
a="CECI EST UN TEST"
print(c_xor(a,cle))
b=c_xor(a,cle)
print(d_xor(b,cle))
