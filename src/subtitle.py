from pytube import YouTube
from xml.etree import ElementTree

#youtube url의 자막 -> xml으로 가져오기
video_url = 'https://www.youtube.com/watch?v=ecUWKU_v318'
yt = YouTube(video_url)
title = yt.title
description = yt.description
caption = yt.captions.get_by_language_code('ko')
caption_xml = caption.xml_captions

#xml -> string list로 파싱(문장별)
root = ElementTree.fromstring(caption_xml)
sentences = []
print(root.tag, root.attrib)
for child in root.findall("text"):
    sentences.append(child.text.replace('\n', ' '))
print(sentences)