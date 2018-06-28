a = []
count = 0
k_total = 0
with open('C:/Users/Also_Lenovo/Desktop/reviews.txt', 'r') as txt:
	for t in txt:
		a.append(t.strip())
		count += 1
		#if count % 1000 == 0:
			#print(count)
			
		#print(t)
		k = len(t)
		k_total = k_total + k

k_average = k_total/len(a)
print(k_average)
