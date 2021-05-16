# kutx-playlist-generator

Requirements
1. Scrape https://kutx.org/playlist for songs (https://realpython.com/beautiful-soup-web-scraper-python/)  
  a. Get to the webpage  
  b. Pull All Data for Each Song  
  c. Parse into iterable format  
  d. (Async LearnPython https://realpython.com/python-async-features/)  
 
2. Search for Each Song on Spoitify  
  a. Iterate through song data, search on spotify  
  b. Return ID or error handling, verification step here (data integrity)  
  c. Append Spoifty ID to Song Data  
  
3. Add all songs with Spotify ID to playlist that are not already in playlist  
  a. Return Meta Data - Counts of Songs who Made it, List of Songs that could not be found.  
  
