from pytube import YouTube

link = "https://youtu.be/BEhELujC83Q"
youtubSource = YouTube(link)

#getting video title
print("Title : "+youtubSource.title)

#getting video streams 720p, 144p
videos = youtubSource.streams.all()
vid = list(enumerate(videos))
for i in vid:
    print(i)
print()
strm = int(input("Select your file type : "))
videos[strm].download()
print('Download Successfully')