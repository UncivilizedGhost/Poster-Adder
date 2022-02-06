def listgetter(names):
    from url import URLget
    list=[]     
    media=''
    while media!='m' and media!='t':
        media=input("Enter m for movie or t for tv: ")
    for i in names:      
        link,valid=URLget(i,media)
        if valid==False:
            list.append("Incorrect name")
        list.append(link)
    return list
