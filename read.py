data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))
print('檔案讀取完了，總共有', len(data),'筆資料')

sunlen = 0
for d in data:
	sunlen += len(d)
print('平均是', sunlen/len(data))

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有',len(new), '筆留言字數小於100')
