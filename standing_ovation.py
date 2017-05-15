

def  call(n, m):
	sum=0
	need=0
	n= int(n)
	for i in range(0, n+1):
		if sum < i:
			need+= i - sum
			sum+= i - sum
		sum+= int(m[i])
	return need


t = int(input())

for i in range(1, t + 1):
	n=0
	m=0
	n, m = [s for s in input().split(" ")]
	print("Case #{}: {}".format(i, call(n, m)))

