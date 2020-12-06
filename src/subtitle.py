from pytube import YouTube
from PyKomoran import *
from xml.etree import ElementTree
from textrank import KeywordSummarizer
from textrank import KeysentenceSummarizer
import numpy as np
from operator import itemgetter

def komoran_tokenize(sent):
    words = sent.split()
    words = [w for w in words if ('/NN' in w or '/XR' in w or '/VA' in w or '/VV' in w)]
    return words

def subtitle(video_url, topk_size):
    #youtube url의 자막 -> xml으로 가져오기
    topk_size = 30
    video_url = 'https://www.youtube.com/watch?v=ecUWKU_v318'
    yt = YouTube(video_url)
    title = yt.title
    description = yt.description
    caption = yt.captions.get_by_language_code('ko')
    caption_xml = caption.xml_captions

    #xml -> string list로 파싱
    root = ElementTree.fromstring(caption_xml)
    texts = []
    texts.append(title)
    for child in root.findall("text"):
        text = child.text.replace('\n', ' ')
        texts.append(text)
    topk_size = texts.size() * 100 // topk_size

    #Komoran을 통해 형태소 단위로 분리 후 태깅
    komoran = Komoran('STABLE')
    sents = []
    for text in texts:
        tokened_text = komoran.get_plain_text(text)
        sents.append(tokened_text)

    keyword_extractor = KeywordSummarizer(
        tokenize = komoran_tokenize,
        window = -1,
        verbose = False
    )
    keywords = keyword_extractor.summarize(sents, topk=30)

    summarizer = KeysentenceSummarizer(
        tokenize = lambda x:x.split(),
        min_sim = 0.5,
        verbose = False
    )
    bias = np.ones(len(texts))
    bias[0] = 5
    keysents = summarizer.summarize(texts, topk=topk_size, bias=bias)
    keysents.sort(key=itemgetter(0))
    first = True
    ret = ''
    for _, _, sent in keysents:
        sent = sent.replace('&#39;', "'")
        ret = ret + sent
        if first:
            ret += '\n'
            first = False
        else:
            ret += ' '
    return ret;
