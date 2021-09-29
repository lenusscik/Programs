import translators as ts

wyw_text = 'Привет, меня зовут Леон. Хотелось бы с вами познакомиться.'
chs_text = 'Hello'


# input languages
print(ts.google(wyw_text)) # default: from_language='auto', to_language='en'

# output language_map
# print(ts._google.language_map)

# professional field
# ("general","message","offer")
print(ts.alibaba(wyw_text, professional_field='common'))
# ('common','medicine','electronics','mechanics')
#print(ts.baidu(wyw_text, professional_field='common'))
# ("medicine","law","machinery")
#print(ts.caiyun(wyw_text, from_language='zh', professional_field=None))
'''
# property
rs = [ts.tencent(x) for x in [wyw_text, chs_text]]
print(ts._tencent.query_count)
print(dir(ts._tencent))

# requests
print(ts.youdao(wyw_text, sleep_seconds=5, proxies={}))

# host service
print(ts.google(wyw_text, if_use_cn_host=True))
print(ts.bing(wyw_text, if_use_cn_host=False))

# detail result
print(ts.sogou(wyw_text, is_detail_result=True))

# translate html
print(ts.translate_html(html_text, translator=ts.google, to_language='en', n_jobs=-1))

# help
help(ts.google)'''
