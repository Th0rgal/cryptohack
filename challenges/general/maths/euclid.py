def gcd(a, b):
    if a == b:
        return a
    return gcd(a, b-a) if (b > a) else gcd(b, a)


def gcdb(a,b):            # maybe will be useful later
     if a<b:             # check and inevert a b, if a<b
          a,b = b,a
     while b!=0:
          a,b = b,a%b
     return a
print(gcd(66528,52920))

def inv_multiplication(a, b, k=1):
    return k if k*a % b == 1 else inv_multiplication(a, b, k+1)

inv_multiplication(26513, 32321)