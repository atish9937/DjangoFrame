import yt_dlp
class download:
    def get_info(self,URL):
        ydl_opts={}
        info=''
        with yt_dlp.YoutubeDL(ydl_opts) as yt:
            info=yt.extract_info(URL,download=False)
        return info



