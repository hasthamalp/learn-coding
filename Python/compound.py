
def ci(p, r, t):

    Amount = p * (pow((1 + r / 100), t))
    CI = Amount - p
    print("Compound interest is", CI)

ci(50000, 11.25, 4)
