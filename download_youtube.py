from pytube import YoutTube
def Download(link):
    youtubeObject=YouTube(link)
    youtubeObject=youtubeObject.streams-get_highest_resolution()
    try:
        youtubeObject.download()
    except:
        print("Eein Fehlet auftreten")
    print("Download completed.")

link=input("Enter the YouTube video URL: ")
Download(link)