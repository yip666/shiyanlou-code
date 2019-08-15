i = 0
while i < 100:
	i += 1
	if i % 10 == 7 or i // 10 == 7 or i % 7 == 0:
		continue
	else:
		print(i)
