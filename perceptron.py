import random as rand

lr = 0.01
w = [rand.uniform(-1, 1), rand.uniform(-1, 1)]
x1 = 5
x2 = 7


def threshold(value):
	if value >= 0:
		return 1
	else:
		return 0

def sum(x1, x2):
	return x1 * w[0] + x2 * w[1]

# printing output before training 
value = sum(x1, x2)
print('Before Training')
print('output: ', threshold(value))
print('w[0]:', w[0])
print('w[1]:', w[1])


# creating 1000 data
data = []
for x in range(10000):
	data.append([])
	for y in range(2):
		data[x].append(rand.randrange(100))

# creating result of data
result = []
for x in data:
	if x[0] >= x[1]:
		result.append(1)
	else:
		result.append(0)

# training with data
def train(data, result):
	i = 0
	for x in data:
		value = (sum(x[0], x[1]))
		output = threshold(value)
		error = result[i] - output
		if error:
			del_w0 = error * x[0] * lr
			del_w1 = error * x[1] * lr
			w[0] += del_w0
			w[1] += del_w1
		i += 1


train(data, result)

value = sum(x1, x2)
#printing result after training
print('\n\nAfter training')
print('output:', threshold(value))
print('w[0]:', w[0])
print('w[1]:', w[1])
