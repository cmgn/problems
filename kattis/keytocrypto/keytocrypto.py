A = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

cipher = input()
key = input()
out = ""

for i in range(len(cipher)):
    c = A.find(cipher[i])
    k = A.find(key[i])
    j = c - k % 26
    out += A[j]
    key += A[j]

print(out)