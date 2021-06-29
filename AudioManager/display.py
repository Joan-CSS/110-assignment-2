def print_menu():
    print("-" * 30 )
    print("* Audio Manager *")
    print("-" * 30)

    print("[1] Register Album")
    print("[2] Register Song")
    print("[3] Print Catalog")
    print("[5] Count all the song in the system")
    print("[6] Total $ in the catalog")
    print("[7] delete album")
    print("[8] delete Song")
    print("[9] print the most expensive album")
    print("[10] print the unique genres")
    print("[q] quit ")

def clear():
    if(os.name == 'nt'):
     os.system('cls')
    else:
     os.system('clear')

   # os.system('cls' if os.name == 'nt' else 'clear')

def print_header(text):
    clear()
    print("-" * 30)
    print(text)
    print("-" * 30)
