def URLget(name,media):
    from tmdbv3api import TMDb, Search
    tmdb = TMDb()
    
    tmdb.api_key = input("Enter api key")
    search = Search()
    if media=='t':
        results = search.tv_shows({"query": name})
    else:
        results = search.movies({"query": name})
    for i in results:
        path=(i.poster_path)
        if path!=None:
            return path,True
    
