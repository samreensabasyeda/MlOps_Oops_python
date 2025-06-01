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
                      pass
        elif user_input == "2":
                      pass
        elif user_input == "3":
                      pass
        elif user_input == "4":
                      pass
        else:
            exit()

obj = ChatBook()