
# Imports
from display import print_menu,clear,print_header
from album import Album
from song import Song
import pickle
 
# Globals
catalog[]
# Functions

def serialize_data():
 try:
   writter = open('songManager.data','wb')#WB write binary
   pickle.dump(catalog,writter)
   writter.close()
   print("** Data saved!")
 except:
   print("**Error: Data was not saved!")

def deserialize_data():
 try:
    reader =open('songManager.data','rb') #rb Read Binary
    temp_list = pickle.load(reader)
    reader.close()
    
    for item in temp_list:
        catalog.append(item)
    print(f"Loaded{len(catalog)} albums ")
 except:
   print("** Error : No data was loaded!")

def registrer_album():
    print_header("Registrer Album")
  
    title = input ("provide the Title : ")
    genre = input ("Provide the Genre : ")
    artist = input ("Provide the Artist Name : ")
    price = float(input ("Provide the price: "))
    release_year = int(input ("Provide the Release Year: "))
    id = 1
    if(len(catalog)>0):
      id= catalog[-1].id + 1 

    album = Album(1,title,genre,artist,price,release_year)
    print(album)
    catalog.append(album)
    print("Album Saved!")

def print_catalog():
    print_header("Your current catalog")
    # iterate the list and print each album

    for album in catalog:
        print (album)
     
    opt = input ("Select an album to see its songs ,or [x] to close")
    if (opt == 'x'): return
    
    try:
     #find the album witth that id 
      the_id =int(id)

      found = False
      for album in catalog:
          if(album.id == the_id):
              found = True
              # Print the songs of album
              for song in album.songs:
               print(song)

               return album 

          if(not found):
             print("*Error : invalid id,try again")
    except:
      print("invalid entry,try again")

def register_song():
 print_catalog(False)
 id = int(input("Please select an Id: "))


def delete_song():
    album = print_catalog(True)
    print("-" * 30)
    id


def register_song():
    print_catalog()
    id = input ("Please select an id:")
    
    #validate the id
    found = False  
    for album in catalog:
        if(album.id == id):
           found = true
           print_header("Register a Song to" + album.title)
           title = input ("provide the title: ")
           length_secs = input("Provide the lenght in secs: ")
           author = input("Provide the author: ")
   
           song = Song(1,title,length_secs,author)
           album.songs.append(song)

        if(not found):
           print("**Error: Invalid id ,try again!")
 
# Instructions 
deserialize_data()
input("Press Enter to continue....")

option = ''
while (option != 'q'):
    clear()
    print_menu()
    option = input("Please select an option ")

    if(option == 'q'):
        break
    if(option == '1'):
        register_album()
        serialize_data()

    if(option == '2'):
        register_song()
        serialize_data()

    if(option == '3'):
       print_catalog()
    
    if(option == '8'):
        if(delete_song())
        serialize_data()
        
     input("Press Enter to continue...")

print("Good bye!")