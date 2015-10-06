#Given: Three positive integers k, m, and n, representing a population containing k+m+n organisms: k individuals are homozygous dominant for a factor, m are heterozygous, and n are homozygous recessive.

#Return: The probability that two randomly selected mating organisms will produce an individual possessing a dominant allele (and thus displaying the dominant phenotype). Assume that any two organisms can mate.

my_list = ['dom', 'het', 'rec']

import sys
k = int(sys.argv[1])
m = int(sys.argv[2])
n = int(sys.argv[3])

pop_dict = {'dom' : k, 'het': m, 'rec': n }

T = k + m + n

prob_dict = {}

for first in my_list:
    prob_dict.update( {first: float(pop_dict[first]) / float(T) } )


punnet_wt = {'domdom': 1, 'domhet' : 1, 'domrec': 1, 
	     'hetdom': 1, 'hethet' : .75, 'hetrec': .5,
	      'recdom': 1, 'rechet' : .5, 'recrec': 0}



#print prob_dict


total = 0
for first in my_list:
    new_prob_dict = {}
    for second in my_list:
	combo = first+second
        if second == first:
	    new_prob_dict.update({second: float(pop_dict[second] - 1) / float(T - 1)} )
	else:
	    new_prob_dict.update({second: float(pop_dict[second]) / float(T - 1)} )
	#print new_prob_dict
	total = total + punnet_wt[combo] * prob_dict[first] * new_prob_dict[second]
	
	print combo, prob_dict[first], new_prob_dict[second], prob_dict[first] * new_prob_dict[second]

print ''
print ''
print ''
print ''

print total

