import random

 #simulated database of users
users = {"user1" : {"password": "password123", "otp_secret" : None},
 "user2" : {"password": "password1234", "otp_secret": None} }

 #function to generate and set OTP for a user
def generate_and_set_OTP(username) :
    users[username]["otp_secret"] = str(random.randint(10000, 99999))
    return users[username]["otp_secret"]

#simulated OTP generator
def generate_otp(username):
    if users[username]["otp_secret"] is None:
        return users[username]["otp_secret"]

#simulated login function
def login(username, password, otp):
    if username in users:
        if password == users[username]["password"]:
            generated_otp = generate_otp(username)
            print(f"generated OTP for {username}: {generated_otp}")

#display otp
        if otp == generated_otp:
             print("login complete")
    else:
        print("incorrect username or password. login failed")

#simulated login attempt
def simulate_login():
    username = input("enter username: ")
    password = input("enter password: ")
    otp = generate_otp(username)

#generate otp before informing user
    print(f"generated otp for {username}: {otp}")

#display otp
    otp_input = input("enter otp:")
    login(username, password, otp_input)

#main function
    def main():
        print("simulated multi-aunthentication system")
        print("--------------------------------------")
        simulate_login()

    if __name__ == "__main__":
        main()