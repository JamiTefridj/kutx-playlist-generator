from selenium.webdriver import Chrome

def generate_song_dict(url):
    browser = Chrome()
    browser.get(url)
    track_dict = {}
    playlist = browser.find_elements_by_class_name('track')
    for song in playlist:
        # Clensing Time Data
        time = song.find_element_by_class_name('time').text
        hyphen_index = time.index('-') + 2
        time_parsed = time[hyphen_index:]

        title =song.find_element_by_class_name('name').text 
        artist = song.find_element_by_class_name('desc').text
        album = song.find_element_by_class_name('collection').text
        track_dict[title] = {'time': time_parsed, 'artist': artist, 'album': album}

    browser.close()
    return track_dict

tracks = generate_song_dict('https://kutx.org/playlist')
print(tracks)
quit()