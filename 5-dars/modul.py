def Summa (n):
    s = 0
    for i in range(n+1):
        s += i
    return s

def Foktaril(n):
    if n == 1 or n == 0:
        return 1
    return n * Foktaril(n-1)
def Main():
    n = 4
    s = Summa(n)
    f = Foktaril(n)
    print("Summa: ", s)
    print("Foktarial: ", f)
if __name__ == "__main__":
    Main()