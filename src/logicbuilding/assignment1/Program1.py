print("Dividing two user inputted numbers...")

def main() :
     n1 = int(input("Enter first number: "));
     n2 = int(input("Enter second number: "));

     res = solve(n1, n2);
     print("Quotient is", res);

def solve(n1, n2) :
    return n1 / n2;

main();