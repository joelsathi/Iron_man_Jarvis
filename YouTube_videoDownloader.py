from pytube import YouTube

class YouTubeDownloader():
    def video(self, url, path):
        youtube_video = YouTube(str(url))
        videolist = youtube_video.streams.filter(file_extension="mp4")
        i = 1
        for video in videolist:
            print(str(i)+" . ", end="")
            print(video)
            i += 1
        index = int(input("Enter the quality of the video by typing the i-tag: "))
        youtube_video.streams.get_by_itag(index).download( output_path=path )
        print("This video has been downloaded.\nThank you fo using Python!! ")

bot = YouTubeDownloader()
url = "https://www.youtube.com/watch?v=hb7Q33ysCwI"
path = r"C:\Users\MAC\Videos\Captures"
bot.video(url, path)
