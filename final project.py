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
                # log in
                if awnser == "yes":
                    userin = input("What is your user name?").strip()
                    passwordin = input("what is your password?").strip()

                    # checking the file
                    with open("user-catering.txt","r") as file:
                        content = file.read()
                    users_blocks = content.split(" ` "*10)
                    user_found = None
                    for block in users_blocks:
                        lines = block.strip().split("\n")
                        current_user = {}
                        for line in lines:
                              line = line.strip()
                              if line.startswith("User ID:"):
                                   current_user['userid'] = line.split(":",1)[1].strip()
                              elif line.startswith("Password:"):
                                   current_user['password'] = line.split(":",1)[1].strip()
                        if current_user.get('userid') == userin:
                            user_found = current_user
                            break
                    if user_found is None:
                        print("user not founded")
                    elif user_found.get('password') == passwordin:
                        print('login complited')
                        break
                    else:
                        print("login failed")

                # sign in                                  
                elif awnser == "no":
                   
                        account.firstname = input("what is your first name?")
                        account.lastname = input("what is your last name?")
                        
                    # checking the userid
                        while True:
                            account.userid = input("give us a user id:")
                            with open("user-catering.txt","r") as file:
                                content = file.read()
                            users_blocks = content.split(" ` "*10)
                            user_found = None
                            for block in users_blocks:
                                lines = block.strip().split("\n")
                                current_user = {}
                                for line in lines:
                                    line = line.strip()
                                    if line.startswith("User ID:"):
                                        current_user['userid'] = line.split(":",1)[1].strip()
                                if current_user.get('userid') ==  account.userid:
                                     user_found = True
                                     break
                            if user_found:
                                 print("someone is using this id try another")
                            else:
                                print("username accepted")
                                break
                        




                    
                while True:
                            account.password = input("give us a password:")
                            verify = input("verify your pass word:")
                            if account.password == verify:

                            # fill the file
                                with open("user-catering.txt","a") as file:
                                
                                    file.write("\n")
                                    file.write("First name:")
                                    file.write(account.firstname)
                                    file.write("\n")
                                    file.write(f"Last name:")
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
                                print("it's done")
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
        print("2 for searching in your reciepe and send it to someone")
        print("3 for making a shop list")
        
        awnser = input("What do you want to do?")

        if awnser == "1":
            
                recipe.foodname = input("what is the name of this food")
                recipe.category = input("What is the category of this")
                recipe.preptime = input("How long dose it take to  make")
                recipe.ingredients = input("write ingredients")
                recipe.moreinfo = input("Who can't eat this?")

                with open("food-catering.txt","a") as file:
                        
                        file.write("\n")
                        file.write({current_user})
                        file.write("\n")
                        file.write(f"food name: {recipe.foodname}")
                        file.write("\n")
                        file.write(f"category: {recipe.category}")
                        file.write("\n")
                        file.write(f"preptime: {recipe.preptime} ")
                        file.write("\n")
                        file.write(f"ingreadient: {recipe.ingredients}")
                        file.write("\n")
                        file.write(f"more info: {recipe.moreinfo}")
                        file.write("\n")
                        file.write(" ` "*10)
                        file.write("\n")
                        print("it's done")
                        print(">"*40)
                        
                        
        elif awnser == "2":
                pass
        elif awnser == "3":
                pass
    

                

class schedule(recipe):
    def __init__(self,day,mealtime,foodname,category,preptime,servings,ingredients,moreinformation):
        super().__init__(foodname,category,preptime,servings,ingredients,moreinformation)
        

    def list():
        pass
account.acsess()
recipe.main()