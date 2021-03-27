import random
start = input('請輸入開始值: ')
end = input('請輸入結束值: ')
start = int(start)
end = int(end)
r = random.randint(start, end)
count = 0
while True:
	count += 1 #count = count + 1
	num = input('請輸入數字: ')
	num = int(num)
	print('這是你猜的第', count, '次')
	if num == r:
		print('恭喜答對了!')
		break	
	elif num > r:
		print('很可惜你猜太大了!')
	elif num < r:
		print('很可惜你猜太小了!')
