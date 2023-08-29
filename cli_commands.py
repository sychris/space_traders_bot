def menu():
    run = True
    while run:
        my_input = input("please enter a command")

        match my_input:
            case "hi":
                print("hello")
            case "view_contracts":
                view_contracts()
            case "view_location":
                view_location("X1-QB20-61050B")
            case "exit":
                run = False

            case _:
                print("unknown command")
