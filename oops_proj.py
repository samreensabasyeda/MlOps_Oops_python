class ChatBook:
    def __init__(self):
        self.username = ".."
        self.password = ".."
        self.loggedin = False
        self.menu()


    def menu(self):
        user_input = input("""Welcome to chatbook... Please tell m e how can i help you...!
                        1. Press 1 to signup
                        2. press 2 to signin
                        3. press 3 to write a post
                        4. press 4 to meaasage ur friend
                        5. press any key to exit""")
        if user_input == "1":
                        self.signup()
        elif user_input == "2":
                        pass
        elif user_input == "3":
                        pass
        elif user_input == "4":
                        pass
        else:
            exit()
    def signup(self):
        email = input("enter your email here -> ")
        pwd = input("setup your password here -> ")
        self.username = email
        self.password = pwd
        print("You have signed up successfully !!")
        print("\n")
        self.menu()

obj = ChatBook()