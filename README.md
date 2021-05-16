# kutx-playlist-generator

Requirements
1. Scrape https://kutx.org/playlist for songs (https://realpython.com/modern-web-automation-with-python-and-selenium/)  
  a. Get to the webpage X  
  b. Pull All Data for Each Song  X  
  c. Parse into iterable format  X  
  d. (Async LearnPython https://realpython.com/python-async-features/)  
 
2. Search for Each Song on Spoitify X  
  a. Iterate through song data, search on spotify  X  
  b. Return ID X or error handling, verification step here (data integrity) X   
  c. Append Spoifty ID to Song Data  X  
  
3. Add all songs with Spotify ID to playlist that are not already in playlist X    
  a. Return Meta Data - Counts of Songs who Made it, List of Songs that could not be found. X  
   
Next Steps  
Load to NoSQL Mongo DB
    Add EveryTime they play a song  
NO DUPLICATE ENTRIES  
Handle Special Characters  
Handle "Remasters"  
Async (Runs without Manual Intervention)  
