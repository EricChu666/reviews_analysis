import time
import random

data = []

with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)


def count_avg_words(data):	#計算資料平均字數、有幾筆小於100字
	new = []
	sum_len = 0
	for d in data:
		if len(d) < 100:
			new.append(d)
		sum_len = sum_len + len(d)

	print('There are', len(new), 'datas which length is under 100.')
	print('The average length of the data is:', sum_len / len(data))


def count_good_word(data):	#計算有good的資料有幾筆
	good = []
	for d in data:
		if 'good' in d:
			good.append(d)
	print('There are', len(good), 'datas include the word "good."')


#faster typing: good   =   [d   for   d	 in   date   if good in d]
#			   output	 運算	   變數		 清單	篩選條件


def count_bad_word(data):#快寫法
	bad = ['bad' in d for d in data]
	print('There are', len(bad), 'datas include the word "bad."')


#文字計數
def word_count(data):
	wc = {}	#word_count
	start_time = time.time()

	for d in data:
		words = d.strip().split()
		for word in words:
			if word in wc:
				wc[word] += 1
			else:
				wc[word] = 1

	end_time = time.time()
	print('花費時間:', end_time - start_time, 'secs')
	return wc


def search_word(wc):
	while True:
		word = input('請輸入你想要查找的字: ')
		if word == 'q':
			break
		if word in wc:
			print(word, '的出現次數為:', wc[word], '次')
		else:
			print('這個字沒有出現過喔!')
	print('感謝你使用查找功能。')






count_avg_words(data)
wc = word_count(data)
search_word(wc)