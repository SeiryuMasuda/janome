# -*- coding:utf-8 -*-
from janome.tokenizer import Tokenizer

t = Tokenizer()

text = input('文章を入力：')

for token in t.tokenize(text):
    if token.part_of_speech.split(',')[0] == '名詞':
    print(token.part_of_speech.split(',')[0], token.surface)