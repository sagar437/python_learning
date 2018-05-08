#!/usr/bin/env python3
import random
goalstring = "methinks it is like a weasel"
def generate(strlen):
	res = ""
	alphabet = "abcdefghijklmnopqrstuvwxyz "
	for i in range(strlen):
		res = res + alphabet[random.randrange(27)]
	return res

#print( generate(28) )

def score(goal,teststring):
	numsame = 0
	for i in range(len(goal)):
		if goal[i] == teststring[i]:
			numsame = numsame + 1
	return numsame/len(goal)

def main():
	result = generate(28)
	marks =  score(goalstring,result)
	best = 0
#	print(result)
#	print(marks)
	while marks < 1:
		if marks > best:
		#	print(marks, result)
			best = marks
		result = generate(28)
		marks = score(goalstring,result)
		#print(best)
main()
