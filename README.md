# Cryptographie-Symetrique
Si l'on parle ici de cryptographie symétrique, c'est que la même clé k est utilisée pour le chiffrement et le déchiffrement.

**Chiffrement de César :**

• Vous pouvez ajouter des caractères à la variable "alphabet", cela ne modifiera pas l'efficacité du code.

• Les messages m et s seront des chaînes de caractères n'utilisant que des majuscules sans accents.

• Chiffre de César. Il s'agit de décaler de k rangs les lettres du message dans l'alphabet (avec reprise à A si on dépasse Z, bien sûr). La clé de chiffrement et de déchiffrement est le nombre de rangs de décalage k.

**Chiffrage XOR :**

• L'opérateur XOR ("ou exclusif") a la particularité d'être réversible, et d'être une des briques de base de l'Unité Arithmétique et Logique d'un ordinateur, ce qui lui donne une pertinence certaine dans le cadre qui nous occupe.

• Le chiffrage XOR consiste à choisir une clé k. On reproduit la clé autant de fois que nécessaire pour arriver à la même longueur que le message à chiffrer. Ensuite, on convertit chaque caractère du message et de la clé étendue en nombre (par exemple via son code Unicode). On effectue ensuite l'opération XOR entre chaque nombre du message et le nombre correspondant de la clé étendue (bit à bit). Pour rappel, l'opérateur XOR renvoie 0 si les deux bits sont identiques, 1 s'ils sont différents.

• Si M est le bit du message, K le bit correspondant de la clé étendue, et que M XOR K = S, alors la réversibilité de l'opérateur XOR nous assure que K XOR S = M, ce qui permettra de décoder le message avec la même clé étendue.
