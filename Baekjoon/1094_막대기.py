import sys
X = int(sys.stdin.readline())
print(bin(X))
if X == 64:
    print(1)
else:
    b = list(map(int, str(bin(X))))
    print(9 - len(str(bin(X))))
