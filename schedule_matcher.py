
'''Schedule Matcher:
		INPUT: 2 entities each give a sequence of tasks, in the order they would
		like to complete them.

		OUTPUT: Provides the longest sequence of tasks the entities can complete
		together, while still remaining loyal to their requested orders

		RUNTIME: Given the length of sequence A is x and the length of B is y,
		program takes O(x*y). This is because we fill a table ot x * y entries,
		each taking constant time to compute. Bottum-up tabulation (dynamic
		programming) approach.

'''

import copy

def print_lcs_matrix(lcs_matrix):
	for row in lcs_matrix:
		print(f'	{row}\n')

#TESTING ONLY: Get Input of 2 lists representing sequences
'''
all_sequences = []
for x in range(2):
	line = input()
	all_sequences.append(line.split())
seq_a = all_sequences[0]
len_a = len(seq_a)
seq_b = all_sequences[1]
len_b = len(seq_b)
'''

#Three helper functions to simply format raw input
def getStrings(text_a, text_b):
	seq_a = list(text_a)
	seq_b = list(text_b)
	return seq_a, len(seq_a), seq_b, len(seq_b)

def getLists(text_a, text_b):
	seq_a = text_a.split()
	seq_b = text_b.split()
	return seq_a, len(seq_a), seq_b, len(seq_b)
def getLists2(text_a, text_b):
	seq_a = text_a.split('\n')
	seq_b = text_b.split('\n')
	return seq_a, len(seq_a), seq_b, len(seq_b)

#Main function
def findLCS(seq_a, seq_b, len_a, len_b):

	#Create matrix (a+1 x b+1), where each of the a rows spans the length of b
	#Note that the indices are [0 = NO VAR] and [len_a = LAST VAR OF A]
	#						   [0 = NO VAR] and [len_b = LAST VAR OF B]
	#Set base case (any row or column 0 has no LCS)
	lcs_matrix = []
	for x in range(len_a+1):
		lcs_matrix.append([0]*(len_b+1))

	#helper_matrix = lcs_matrix.copy() ; This holds directions, so we can backtrack and actually
	#	get the LCS
	helper_matrix = copy.deepcopy(lcs_matrix)

	#Fill up matrix by traversing [1...len_a] x [1...len_b]
	for i in range(1,len_a+1):
		for j in range(1, len_b+1):
			'''
			print(f'ITERATION: i = {i}, j = {j}')
			print(f'\tlcs_matrix[{i-1}][{j}] = {lcs_matrix[i-1][j]}')
			print(f'\tlcs_matrix[{i}][{j-1}] = {lcs_matrix[i][j-1]}')
			'''

			if seq_a[i-1] == seq_b[j-1]:
				lcs_matrix[i][j] = lcs_matrix[i-1][j-1] + 1
				helper_matrix[i][j] = 'D'
			elif lcs_matrix[i-1][j] >= lcs_matrix[i][j-1]:
				lcs_matrix[i][j] = lcs_matrix[i-1][j]
				helper_matrix[i][j] = 'U'
			else:
				lcs_matrix[i][j] = lcs_matrix[i][j-1]
				helper_matrix[i][j] = 'L'
	'''
	print('LCS Matrix:')
	print_lcs_matrix(lcs_matrix)
	print('HELPER Matrix:')
	print_lcs_matrix(helper_matrix)
	'''
	#Backtrack to retrieve the largest common subsequence
	LCS_len = lcs_matrix[len_a][len_b]
	LCS = []
	row = len_a
	col = len_b

	while (row > 0) and (col > 0):
		if helper_matrix[row][col] == 'D':
			LCS.insert(0, seq_a[row-1])
			row -= 1
			col -= 1
		elif helper_matrix[row][col] == 'L':
			col -= 1
		else:
			row -= 1

	return LCS, len(LCS)












