
def cSort(arr, exp1):

	n = len(arr)


	out = [0] * (a)


	count = [0] * (10)

	for i in range(0, a):
		ind = (arr[i]/exp1)
		count[int((ind)%10)] += 1


	for i in range(1,10):
		count[i] += count[i-1]


	i = a-1
	while i>=0:
		ind = (arr[i]/exp1)
		out[ count[ int((ind)%10) ] - 1] = arr[i]
		count[int((ind)%10)] -= 1
		i -= 1


	i = 0
	for i in range(0,len(arr)):
		arr[i] = out[i]

def rSort(arr):

	max1 = max(arr)

	exp = 1
	while max1/exp > 0:
		cSort(arr,exp)
		exp *= 10

arr = [ 123, 23, 87, 31, 33, 12, 1, 44]
rSort(arr)

for i in range(len(arr)):
	print(arr[i]),
