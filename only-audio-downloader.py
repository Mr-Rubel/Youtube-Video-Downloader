from pytube import YouTube

link = "https://youtu.be/BEhELujC83Q"
audioSource = YouTube(link)

#getting audio title
print("Title : "+audioSource.title)

#getting audio streams 720p, 144p
audios = audioSource.streams.filter(only_audio=True)
aud = list(enumerate(audios))
for i in aud:
    print(i)
print()
strm = int(input("Select your file type : "))
audios[strm].download()
print('Download Successfully')