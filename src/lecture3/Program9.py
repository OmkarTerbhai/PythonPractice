print("Printing box...")

def main() :
    n = int(input("Enter rows: "));
    m = int(input("Enter columns..."));
    solve(n, m);

def solve(n, m) :
    for i in range(n) :
        for j in range(m) :
            print("* ", end="");
        print();

main();