class account:
    def __init__(self,firstname,lastname,userid,password):
        self.firstname = firstname
        self.lastname = lastname
        self.userid = userid
        self.password = password
    def acsess():
            print("Hi do you have an account enter yes or no")
            awnser = input("?")
            while True:
                if awnser == "yes":
                    userin = input("What is your user name?")
                    passwordin = input("what is your password?")
                elif awnser == "no":

                    account.firstname = input("what is your first name?")
                    account.lastname = input("what is your last name?")
                    account.userid = input("give us a user id:")
                    while True:
                        account.password = input("give us a password:")
                        verify = input("verify your pass word:")
                        if account.password == verify:
                            with open("catering.txt","a") as file:
                                file.write("\n")
                                file.write("First name:")
                                file.write(account.firstname)
                                file.write("\n")
                                file.write("Last name:")
                                file.write(account.lastname)
                                file.write("\n")
                                file.write("User ID:")
                                file.write(account.userid)
                                file.write("\n")
                                file.write("Password:")
                                file.write(account.password)
                                file.write("\n")
                                file.write(" ` "*10)
                                file.write("\n")
                                print(">"*40)
                                break
                                    

                break
class recipe(account):
    def __init__(self,owner,foodname,category,preptime,servings,ingredients,moreinfo):
        self.owner = owner
        self.foodname = foodname
        self.category = category
        self.preptime = preptime
        self.servings = servings
        self.ingredients = ingredients
        self.moreinfo = moreinfo
    def main():
        print("1 for adding a new recepi")
        print("2 for searching in your reciepe ")
        print("3 for making a shop list")
        awnser = input("What do you want to do?") 
        if awnser == "1":
            def newrecipe(food):
                account.foodname = input("what is the name of this food")

                


class schedule(recipe):
    def __init__(self,day,mealtime,foodname,category,preptime,servings,ingredients,moreinformation):
        super().__init__(foodname,category,preptime,servings,ingredients,moreinformation)
        

    def list():
        pass
account.acsess()