def URLget(name,media):
    from tmdbv3api import TMDb, Search
    tmdb = TMDb()
    tmdb.api_key = "af78f153258ffed0f4a5b45fa5b6ad5b"
    search = Search()
    if media=='t':
        results = search.tv_shows({"query": name})
    else:
        results = search.movies({"query": name})
    for i in results:
        path=(i.poster_path)
        if path!=None:
            return path,True
    
