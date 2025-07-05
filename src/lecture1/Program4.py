def main():
    name = input("What's your name: ");
    hello(name);
    fun();

def fun():
    hello();

def hello(name = "Tom"):
    print("Hello....", name);

main();