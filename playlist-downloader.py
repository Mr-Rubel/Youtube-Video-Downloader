from pytube import Playlist

py = Playlist("https://youtube.com/playlist?list=PLAUJg8vDmW1pxU_WG7pe-hZsYZWZHbzBh")

print(f'Downloading : {py.title}')

for i in py.videos:
    i.streams.first().download()
    print("Complete!")

print("All files downloading are completed!")