import math

n=int(input("数字を入力してください。\n"))

if n > 10000:
	print("10000以下の数字を入力してください。")
else:
	def Prime(n):
		flag=0
		if n<2 or n%2 == 0:
			print("{0}は素数ではありません。".format(n))

		elif n==2:
			print("{0}は素数です。".format(n))

		else:
			y=math.sqrt(n)
			for i in range(3,int(y)+2,2):
				if n%i == 0:
					flag=1
					break

			if flag == 1:
				print("{0}は素数ではありません。".format(n))
			else:
				print("{0}は素数です。".format(n))

	Prime(n)



