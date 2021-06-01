# Instructions

To run go on exec.py

change [Your Search] to what you want to search for example worship song, kpop or any musics category you are looking for.

Then on console do the following:
```
python exec.py
```
You will need python installed, and selenium

If you want to execute some the stuff manually, I have program this script in 3 part shared within each other song_namescollection.py parents of downloads.py parents of youtubetomp3.py

song_namescollection.py -> downloads.py -> youtubetomp3.py

For each class, the function that you will need:

song_namescollection.py - makeTheSearch which takes only 1 argument that is the names of the search. It will return an arrays of name associated to the search

downloads.py - goToYoutubeAndSearch which takes only 1 argument that is the search you will do on youtube and return an array of objects containing links, names, authors, time

youtubetomp3.py - Will take an array of objects and download the youtube music to mp3.

Note: 
The name length of the music is fixed at 20 excluding authors' name 
The music time range is fixed less than 7 min.

I uses google.com to make the category searches, youtube to collect the data to be downloaded and https://youtubetomp3music.com/ to convert youtube to mp3

# Preview

![](previews/preview.gif)


