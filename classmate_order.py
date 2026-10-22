
def c(p):
    x = p * 0.05
    y = p + x
    return y


def o(n):
    if n < 40:
        return True
    else:
        return False


def d(p):
    if p > 300:
        p = p * 0.90
    x = p * 0.05
    y = p + x
    return y


def pay(a):
    print("Payment amount:", a)
    return True
