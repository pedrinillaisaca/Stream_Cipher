y_i="bsaspp kkuosp"
k_i="rsidpy dkawoy"
abecedario=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
salida=""
cont=0
for i in y_i:
    if i !=" ":        
        x_i= (abecedario.index(i)) - (abecedario.index(k_i[cont])  % 26)
        salida+=abecedario[x_i]
    elif i ==" ":
        salida+=" "
    cont+=1
print("==>",salida,"<==")




