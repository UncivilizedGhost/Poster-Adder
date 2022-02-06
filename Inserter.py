def pictureInserter(og,address,list):
    j=0
    for i in og:
        file1 = open(address+'/'+i, "a")
        x="\ncover::https://image.tmdb.org/t/p/original/"+list[j]
        file1.writelines(x)
        file1.close()
        j=j+1

        