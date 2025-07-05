def main() :
    n = takeInput();
    meow(n);

def takeInput() :
    while(True) :
        n = int(input("Enter a number: "));
        if n > 0 :
            return n;

def meow(n) :
    for i in range(n) :
        print("Meow!");


main();