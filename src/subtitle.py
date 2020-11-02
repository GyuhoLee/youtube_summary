from pytube import YouTube

video_url = 'https://www.youtube.com/watch?v=ecUWKU_v318'
yt = YouTube(video_url)
title = yt.title
description = yt.description
caption = yt.captions.get_by_language_code('ko')
caption_xml = caption.xml_captions