import random
 
def guess_number():
   
    secret_number = random.randint(1, 100)
    print("********************************************")
    print("ทายตัวเลขที่มีค่าอยู่ที่ 1 - 100 กันเถอะ")
    while True:
        try:
           
            user_guess = int(input("ป้อนตัวเลขที่ต้องการทาย : "))
           
            if user_guess == secret_number:
                print("*****************************************")
                print("ยินดีด้วยคุณทายถูก")
                break
            elif user_guess < secret_number:
                print("*****************************************")
                print("คุณทายผิด ตัวเลขที่ป้อนน้อยไป")
            else:
                print("*****************************************")
                print("คุณทายผิด ตัวเลขที่ป้อนมากไป")
        except ValueError:
            print("*****************************************")
            print("โปรดป้อนตัวเลขที่ถูกต้อง")
 
if __name__ == "__main__":
    guess_number()
    print("********************************************")