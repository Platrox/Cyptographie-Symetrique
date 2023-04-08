alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" 

def indice(ch,txt):
    for k in range(len(txt)):
        if txt[k]==ch:
            return k

def c(m,k):
    '''
    La fonction de chiffrement, qui reçoit un message en clair m (une chaîne de caratères par exemple) et une clé de chiffrement k (qui peut être une chaîne de caractères, un nombre, etc.). Elle produit en sortie un message chiffré s.
    '''
    s=''
    for c in m:
        if c in alphabet:
            i=indice(c,alphabet)
            s+=alphabet[(i+k)%len(alphabet)]
        else:
            s+=c
    return s

def d(s,k):
    '''
    La fonction de déchiffrement, qui reçoit le message chiffré s, une clé de déchiffrement k, et qui renvoie le message en clair m.
    '''
    return c(s,-k)
