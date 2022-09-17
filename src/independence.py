import random
from fractions import Fraction

def coin_toss(result,exp_length = 1,exp_num = 1):
	
	#Do the Experiment
	data = []
	for i in range(exp_num):
		exp = []
		for i in range(exp_length):
			rng = random.randint(0,1)
			exp.append(rng)
		data.append(exp)
	

	#calculate the probability of result
	result_count = 0
	for i in data:
		if i == result:
			result_count += 1

	probability = result_count/exp_num

	return probability


#result = [0,1,0,0] 
#print(coin_toss(result,exp_num = 200000,exp_length = len(result) ))
#print(1/2**len(result))






def independent_vars(result,exp_length = 1,exp_num = 1,die_side = 2):
	
	#Do the Experiment
	data = []
	for i in range(exp_num):
		exp = []
		for i in range(exp_length):
			rng = random.randint(0,die_side - 1)
			exp.append(rng)
		data.append(exp)
	

	#calculate the probability of result
	result_count = 0
	for i in data:
		if i == result:
			result_count += 1

	probability = result_count/exp_num

	return probability

result = [0,2,1]
sides = 3 
print(independent_vars(result,exp_num = 200000,exp_length = len(result),die_side = sides))
print(1/sides**len(result))

