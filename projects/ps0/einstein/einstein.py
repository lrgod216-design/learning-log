
def main():
    m = int(input("Input a mass as an integer (in kg): "))
    print(energy(m))

# Caculate Energy
def energy(m):
    c = 300000000
    E = m * c ** 2
    return E

main()