from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.conf import settings
import random

from elasticsearch import Elasticsearch
es = Elasticsearch()

# Create your views here.
from scrapper.tasks import parse_cnet_rss,parse_foxnews_rss,parse_nytimes_rss,parse_pcmag_rss

headers = {
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}

# Create your views here.
def index(request):
    cnet_res = es.search(index="cnet-index", body={"size":1,"sort": { "timestamp": "desc"},"query": {"match_all": {}}})
    cnet_data = cnet_res['hits']['hits'][0]['_source']['body']

    nytimes_res = es.search(index="nytimes-index", body={"size":1,"sort": { "timestamp": "desc"},"query": {"match_all": {}}})
    nytimes_data = nytimes_res['hits']['hits'][0]['_source']['body']
    
    foxnews_res = es.search(index="foxnews-index", body={"size":1,"sort": { "timestamp": "desc"},"query": {"match_all": {}}})
    foxnews_data = foxnews_res['hits']['hits'][0]['_source']['body']

    pcmag_res = es.search(index="pcmag-index", body={"size":1,"sort": { "timestamp": "desc"},"query": {"match_all": {}}})
    pcmag_data = pcmag_res['hits']['hits'][0]['_source']['body']

    data = cnet_data+nytimes_data+foxnews_data+pcmag_data
    random.shuffle(data)

    return render(request,'index.html',{'data':data})




