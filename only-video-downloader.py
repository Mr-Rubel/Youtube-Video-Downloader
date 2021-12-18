from pytube import YouTube

link = "https://youtu.be/BEhELujC83Q"
videoSource = YouTube(link)

#getting video title
print("Title : "+videoSource.title)

#getting video streams 720p, 144p
videos = videoSource.streams.filter(only_video=True)
vid = list(enumerate(videos))
for i in vid:
    print(i)
print()
strm = int(input("Select your file type : "))
videos[strm].download()
print('Download Successfully')