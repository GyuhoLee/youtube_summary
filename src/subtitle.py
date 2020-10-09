from pytube import YouTube

video_url = 'https://www.youtube.com/watch?v=Zg3j6anDU6U'
yt = YouTube(video_url)
caption = yt.captions.get_by_language_code('ko')
if(caption == None):
    caption = yt.captions.all()[0]
caption.xml_captions()