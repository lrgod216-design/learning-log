
def main():
    print(energy())

# Caculate Energy
def energy():
    m = int(input("Input a mass as an integer (in kg): "))
    c = 300000000
    E = m * c ** 2
    return E

main()