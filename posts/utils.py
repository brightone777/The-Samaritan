def set_no_cache_for_media(headers, _path, url):
    if url.startswith("/media/"):
        headers["Cache-Control"] = "no-cache"
