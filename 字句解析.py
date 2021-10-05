# -*- coding:utf-8 -*-
from janome.tokenizer import Tokenizer

t = Tokenizer()

text = '増田は千葉県在住の男性です。'

for token in t.tokenize(text):
    #if token.part_of_speech.split(',')[0] == '名詞':
    print(token.part_of_speech.split(',')[0], token.surface)