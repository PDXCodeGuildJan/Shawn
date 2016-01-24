from functools import lru_cache


@lru_cache(maxsize = None)
def fib(num):
	print(num)
	if num == 0 or num == 1:
		return num
	else: return fib(num-1)+fib(num-2)

def main():

	x = int(input("Give me an integer to calculate the nth Fibbonacci:"))
	i = 0
	while i < x:
		print(fib(int(i)), end = " ")
		i += 1

main()