import os
import sys
import time
PRODUCT_KEY = "5973-0828-7047-8005"

def type_in_product_key():

    print("Please While we Prepare...")

    for step in range(100):
        print("#", end="", flush=True)
        time.sleep(0.05)


    print(" Type in the product key using keyboard events.")
    user_input = input("Please enter the product key: ")


    if user_input == PRODUCT_KEY:
        print("Product key is valid.")
        print("Please wait while we prepare your actvation...")
        # Simulate typing the product key
        for step in range(100):
            print("#", end="", flush=True)
            time.sleep(0.05)

        print(" Activating Commands...")
        for step in range(100):
            print("#", end="", flush=True)
            time.sleep(0.05)
        
            print(" Activation complete!")
            sys.exit(0)


        
    elif user_input == "exit":
            print("Exiting...") 
            sys.exit(0)

    else:
        print("Invalid product key. Please try again.")
        os.system("cls")
        type_in_product_key()

if __name__ == "__main__":
    os.system("cls")
    type_in_product_key()