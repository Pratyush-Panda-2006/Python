import time

print("--- Color Choosing Game ---")

while True:
    print("\nChoose a color:")
    print("1: Red")
    print("2: Yellow")
    print("3: Green")
    
    col = input("Enter your choice (1, 2, or 3): ").strip()
    if col == '3': 
        print("Checking result...")
        time.sleep(5)  
        print("You Won!")
        print("Ending Game.")
        break
        
    elif col == '2':
        print("Checking result...")
        time.sleep(2)  
        print("You lose! (Alert)")
        continue 
        
    else:
        print("Checking result...")
        time.sleep(4)  
        print("You lose! (Restarting)")
        continue