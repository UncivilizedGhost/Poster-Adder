def get_filepaths(directory):
    import os
    import re
    media_names = []  # List which will store all of the full names.
    file_names=[]

    for root, directories, files in os.walk(directory):
        for i in files:            
            cover_check=open(directory+'\\'+i )
            info=cover_check.read()
            checker=re.compile(r'cover::')
            occurance=checker.search(info)
            if occurance == None:
                filepath = os.path.join(i)
                file_names.append(filepath)
                j= filepath.replace("-", ":")    
                media_names.append(j[0:len(j)-3])

    return media_names ,file_names


