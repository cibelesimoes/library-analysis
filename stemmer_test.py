#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 18:43:41 2020

@author: cibelesantos
"""
from nltk.stem.snowball import SnowballStemmer

stemmer = SnowballStemmer("portuguese")

words = ['corrida','correu', 'corredor', 'corridinha','torceu', 'torcida', 'maçã']

for word in words:
    print(word + ' ------> ' + stemmer.stem(word))


