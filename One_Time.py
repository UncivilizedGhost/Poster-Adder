from url import *
def onetime():
    media=''
    import pyperclip
    while media!='m' and media!='t':
        media=input("m for movie or t for tv:  ")
    name=input("Enter name   ")
    try:
         path,valid=URLget(name,media)
         pyperclip.copy("cover::https://image.tmdb.org/t/p/original"+path)
    except:
        print("incorrect name")

if __name__ == "__main__":
    onetime()
