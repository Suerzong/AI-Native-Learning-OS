# -*- coding: utf-8 -*-
import sys, os, re, time
sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from scrape_runoob import scrape_topic, combine_topic_md

pages = scrape_topic('TensorFlow', 'https://www.runoob.com/tensorflow/')
combine_topic_md('TensorFlow', pages)
print("TensorFlow done:", len(pages), "pages")
