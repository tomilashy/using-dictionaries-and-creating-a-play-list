Playlist = {
    "title" : "World cup",
    "author": "J lo",
    "year": 2018,
    "songs": [
      {"title": "Ole ola", "author":["J lo","Pitbull"], "Duration":4.25},
      {"title": "La la la", "author":["J lo","Shakira"], "Duration":6.18},
      {"title": "Anything", "author":["J lo"], "Duration":5.40},
      {"title": "New song", "author":["J lo","Selena"], "Duration":6.00}
      ]
}

#total duration
total = 0;
for song in Playlist["songs"]:
  total+=song["Duration"];
  
print(f"Total duration of the album is {total} Minutes")

#duration of a particular song
check = input("What's the name of the song which you want to check its duration?")
check=check.capitalize();
for song in Playlist["songs"]:
  if song["title"]==check:
    print(f"Its duration is {song['Duration']} Minutes")
    
    
#authors of a particular song
check = input("What's the name of the song which you want to check its author(s)?");
check=check.capitalize();
for song in Playlist["songs"]:
  if song["title"]==check:
    if len(song["author"]) >= 2:
      print("These are the followimg authors: ");
      for x in song["author"]:
        print(x);
    elif len(song["author"]) == 1:
      for x in song["author"]:
        print(f"The author is {x}");
        
    
    
    