myStr = input("Enter a string: ");

match myStr :
    case "A":
            print("str is A");
    case "B":
            print("str is B");
    case "C":
            print("str is C");
    case _:
            print("What is this str????")