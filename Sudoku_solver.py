'''
e1:
First functioning code

e2:
Added comments 
Removed hard coding
Includes incomplete backtracking function
Includes confirmation for sudoku taken as input
Includes incomplete print_sudoku function

e3:
Functioning backtracking code

e4:
Added single function to check rows, cols & box
Combined 2 methods
Made modifications

e5:
Added possibility to see multiple soltuions if they exist
Count number of possible solutions

e6:
UI for input/ output

e7:
Reset function
Robustness to wrong input
Gray out solve and reset without previous solve finishing

This version:

To be done:
Generalisation of number of sections in sudoku in gui code
Make a full ui
Ability to create sudoku based on insights
'''

import tkinter as tk


def solve_sudoku(sudoku,backtrack):
	''' This function solves the sudoku using methods similar to human solving.
	It checks every column, row, then box for miossing numbers and fills it in 
	if there is only one possible option. This can be run with only the column 
	or row or box segment, to get solution. It failes for difficult sudokus that
	require guessing. '''

	# Initialising variables
	global size_row,size_col,n_range,num_rows_cols
	new_sudoku = [[j for j in i ]for i in sudoku] #new sudoku to store changes

	# Looping till sudoku is solved
	while not is_sudoku_complete(sudoku):

		#  Filling missing numbers in each column
		for col in range(num_rows_cols):				
			for test_number in n_range:
				
				# Skipping filled numbers
				if in_col(new_sudoku,1,col,test_number):
					continue

				# Initialise list for possible positions for number
				possible_positions = []
				for row in range(num_rows_cols):
					# Add to list if suitable candidate
					if (new_sudoku[row][col] == 0) \
					and can_write(new_sudoku,row,col,test_number):
						possible_positions.append(row)
				
				# Fill in if we find unique solution
				if len(possible_positions) == 1:
					new_sudoku[possible_positions[0]][col] = test_number
		
		# # Filling missing numbers in each row
		# for row in range(num_rows_cols):
		# 	for test_number in n_range:

		# 		# Skipping filled numbers
		# 		if in_row(new_sudoku,row,1,test_number):
		# 			continue

		# 		# Initialise list for possible positions for number
		# 		possible_positions = [] 
		# 		for col in range(num_rows_cols):
		# 			# Add to list if suitable candidate
		# 			if (new_sudoku[row][col] == 0) \
		# 			and can_write(new_sudoku,row,col,test_number):
		# 				possible_positions.append(col)
				
		# 		# Fill in if we find unique solution
		# 		if len(possible_positions) == 1:
		# 			new_sudoku[row][possible_positions[0]] = test_number

		# #  Filling missing numbers in each box
		# for box in range(num_rows_cols):
		# 	for test_number in n_range:
				
		# 		# Skipping filled numbers
		# 		brow = int(box/size_row)*size_row #starting row of box
		# 		bcol = (box%size_row)*size_col #starting column of box
		# 		if in_box(new_sudoku,brow,bcol,test_number):
		# 			continue

		# 		# Initialise list for possible positions for number
		# 		possible_positions = []
		# 		for i in range(num_rows_cols):
		# 			row = brow + int(i/size_col)
		# 			col = bcol + (i%size_col)
		# 			# Add to list if suitable candidate
		# 			if (new_sudoku[row][col] == 0) \
		# 			and can_write(new_sudoku,row,col,test_number):
		# 				possible_positions.append((row,col))
				
		# 		# Fill in if we find unique solution
		# 		if len(possible_positions) == 1:
		# 			new_sudoku[possible_positions[0][0]][possible_positions[0][1]] = test_number

		# Calculating number of positions filled
		change = 0
		for row in range(num_rows_cols):
			for col in range(num_rows_cols):
				if new_sudoku[row][col] != sudoku[row][col]:
					change += 1
		# print(change)
		if change>0:
			# print_sudoku(new_sudoku)
			pass
		else:
			# Either solved or cannot be solved without backtracking
			if backtrack:
				return solve_sudoku_backtrack(sudoku)
			else:
				break 

		# Adding solution to original sudoku
		sudoku = [[j for j in i ]for i in new_sudoku] \

	disp_sudoku_soln(sudoku)
	return sudoku


def solve_sudoku_backtrack(sudoku):
	''' This recursive function is called to solve a sudoku using backtracking methods.
	This is important in more difficult sudokus where guessing needs to be 
	done. It also identifies if there are multiple possible solutions. '''

	global size_row,size_col,n_range,num_rows_cols
	global fwc_counter #initialise recursive counter
	fwc_counter = 0

	# Initialise and fill in domain values
	domain = [[[] for col in range(num_rows_cols)] for row in range(num_rows_cols)]
	
	for row in range(num_rows_cols):
		for col in range(num_rows_cols):

			# If filled, just add the filled value as the domain
			if sudoku[row][col]!=0: 
				domain[row][col].append(sudoku[row][col])
			else: 
				# Append every possible value
				for test_number in n_range:
					if can_write(sudoku,row,col,test_number):
						domain[row][col].append(test_number)

	fwc_recursive(sudoku, domain)
	print("Recursive count: "+str(fwc_counter))

	# return sudoku
	return sudoku


''' Following are helper functions. '''

def fwc_recursive(sudoku, domain):
	''' Recursive function for implementing backtracking. '''

	global size_row,size_col,n_range,num_rows_cols
	global fwc_counter, num_soln, multiple, toggle
	fwc_counter +=1 #increment recursive counter

	# Check if sudoku is solved
	if is_sudoku_complete(sudoku):
		num_soln += 1 #increment number of solutions
		print_sudoku(sudoku)
		print("Is sudoku solved correctly? "+str(sudoku_checker(sudoku)))
		if num_soln==1:
			disp_sudoku_soln(sudoku)
			while 1:
				ans = input("\n1 solution found, look for more? (y/n): ")
				if ans=='n':
					multiple = 0
					break
				elif ans=='y':
					multiple = 1
					break
		elif (num_soln%30)==0 and toggle==1:
			while 1:
				ans = input("\n"+str(num_soln)+" solutions found, look for more?\
 yes,no,donot ask again(y/n/d): ")
				if ans=='n':
					multiple = 0
					break
				elif ans=='y':
					break
				elif ans=='d':
					toggle = 0
					break
		return True

	else:

		# Check all possible empty slots
		for row in range(num_rows_cols):
			for col in range(num_rows_cols):

				# Check if empty
				if sudoku[row][col]==0:

					# Creating new domain variables
					old_domain = [[[val for val in domain_col] for domain_col in domain_row] for domain_row in domain]
					new_domain = [[[val for val in domain_col] for domain_col in domain_row] for domain_row in domain]

					# Update and check for all possible values
					for test_number in old_domain[row][col]: 

						sudoku[row][col] = test_number
						new_domain = update_domain(new_domain, row, col, test_number)

						# Forward check for updated domain
						if domain_checker(new_domain):
							if fwc_recursive(sudoku, new_domain):
								if multiple==0:
									return True 

						# Reset: either not solved of searching for next solution
						sudoku[row][col] = 0
						new_domain = [[[val for val in domain_col] for domain_col in domain_row] for domain_row in old_domain]

					return False


def in_row(sudoku,row,col,test_number):
	''' Function to check if given number is present in row of
	element given by 'row' and 'col' values. '''

	global num_rows_cols

	for col in range(num_rows_cols):
		if sudoku[row][col] == test_number:
			return True
	return False


def in_col(sudoku,row,col,test_number):
	''' Function to check if given number is present in column of
	element given by 'row' and 'col' values. '''
	
	global num_rows_cols

	for row in range(num_rows_cols):
		if sudoku[row][col] == test_number:
			return True
	return False


def in_box(sudoku,row,col,test_number):
	''' Function to check if given number is present in box of
	element given by 'row' and 'col' values. '''
	
	global size_row,size_col

	Box_row = int(row/size_row)*size_row
	Box_col = int(col/size_col)*size_col
	for i in range(size_row):
		for j in range(size_col):
			if sudoku[Box_row][Box_col] == test_number:
				return True
			Box_col += 1
		Box_row += 1
		Box_col -= size_col
	return False


def can_write(sudoku,row,col,test_number):
	''' Combines row, col and box checker. '''

	if test_number==0:
		return True
	if  (not in_row(sudoku,row,col,test_number)) \
	and (not in_col(sudoku,row,col,test_number)) \
	and (not in_box(sudoku,row,col,test_number)):
		return True


def is_sudoku_complete(sudoku):
	''' Function to check if sudoku is completed, i.e., 
	there are no values left to fill. '''
	
	global num_rows_cols, num_soln

	for row in range(num_rows_cols):
		for col in range(num_rows_cols):
			if sudoku[row][col] == 0: #unfilled element
				return False
	print("\nSOLVED! Solution number: "+str(num_soln+1))
	return True


def sudoku_checker(sudoku, solved=1):
	''' Check if sudoku is solved correctly. '''

	global num_rows_cols

	for row in range(num_rows_cols):
		for col in range(num_rows_cols):
			num = sudoku[row][col]
			sudoku[row][col] = 0
			if (not can_write(sudoku,row,col,num)) or (solved and num==0):
				print("Row: ",row,"Col: ",col,"Val: ",num)
				return False
			sudoku[row][col] = num

	return True


def update_domain(domain, row, col, test_number):
	''' Updates domain to remove newly added number from domains of positions in
	the same row/ col/ box. '''

	global size_row,size_col,num_rows_cols

	# Remove test_number from all domains for this column and all possible rows
	for domain_row in range(num_rows_cols):
		if test_number in domain[domain_row][col]:
			domain[domain_row][col].remove(test_number)

	# Remove test_number from all domains for this row and all possible columns
	for domain_col in range(num_rows_cols):
		if test_number in domain[row][domain_col]:
			domain[row][domain_col].remove(test_number)

	# Remove test_number from all domains for the box of current coordinate
	for i in range(num_rows_cols):
		if test_number in domain[int(row/size_row)*size_row+int(i/size_col)][int(col/size_col)*size_col+i%size_col]:
			domain[int(row/size_row)*size_row+int(i/size_col)][int(col/size_col)*size_col+i%size_col].remove(test_number)

	# Re-enter current position
	domain[row][col] = [test_number]
	return domain


def domain_checker(domain):
	''' Returns False if the potential domain fails the forward check. '''

	global num_rows_cols

	# Check all possible empty slots
	for row in range(num_rows_cols):
		for col in range(num_rows_cols):
			if len(domain[row][col])==0:
				return False

	return True


def input_sudoku():
	''' Function to take unsolved sudoku as input and return it. '''

	global size_row,size_col,n_range,num_rows_cols

	# # sample puzzle 1 - easy
	# size_row = 3
	# size_col = 3
	# n_range = range(1, (size_row*size_col)+1)
	# sudoku = [[0,0,4,	0,5,0,	0,0,0],
	#           [9,0,0,	7,3,4,	6,0,0],
	#           [0,0,3,	0,2,1,	0,4,9],

	#           [0,3,5,	0,9,0,	4,8,0],
	#           [0,9,0,	0,0,0,	0,3,0],
	#           [0,7,6,	0,1,0,	9,2,0],

	#           [3,1,0,	9,7,0,	2,0,0],
	#           [0,0,9,	1,8,2,	0,0,3],
	#           [0,0,0,	0,6,0,	1,0,0]]


	# # sample puzzle 2 - difficult
	# size_row = 3
	# size_col = 3
	# n_range = range(1, (size_row*size_col)+1)
	# sudoku = [[0,0,0,	8,0,0,	4,2,0],
	#           [5,0,0,	6,7,0,	0,0,0],
	#           [0,0,0,	0,0,9,	0,0,5],

	#           [7,4,0,	1,0,0,	0,0,0],
	#           [0,0,9,	0,3,0,	7,0,0],
	#           [0,0,0,	0,0,7,	0,4,8],

	#           [8,0,0,	4,0,0,	0,0,0],
	#           [0,0,0,	0,9,8,	0,0,3],
	#           [0,9,5,	0,0,3,	0,0,0]]


	# sample puzzle 3 - multiple solutions
	# size_row = 3
	# size_col = 3
	# n_range = range(1, (size_row*size_col)+1)
	# sudoku = [[0,0,0,	8,0,0,	4,2,0],
	#           [5,0,0,	6,0,0,	0,0,0],
	#           [0,0,0,	0,0,9,	0,0,5],

	#           [7,4,0,	1,0,0,	0,0,0],
	#           [0,0,9,	0,3,0,	7,0,0],
	#           [0,0,0,	0,0,7,	0,4,8],

	#           [8,0,0,	4,0,0,	0,0,0],
	#           [0,0,0,	0,9,8,	0,0,3],
	#           [0,9,5,	0,0,3,	0,0,0]]


	# # sample puzzle 4 - 2 solutions
	# size_row = 3
	# size_col = 3
	# n_range = range(1, (size_row*size_col)+1)
	# sudoku = [[2,9,5,	7,4,3,	8,6,1],
	#           [4,3,1,	8,6,5,	9,0,0],
	#           [8,7,6,	1,9,2,	5,4,3],

	#           [3,8,7,	4,5,9,	2,1,6],
	#           [6,1,2,	3,8,7,	4,9,5],
	#           [5,4,9,	2,1,6,	7,3,8],

	#           [7,6,3,	5,2,4,	1,8,9],
	#           [9,2,8,	6,7,1,	3,5,4],
	#           [1,5,4,	9,3,8,	6,0,0]]


	# Initialising sudoku
	# sudoku = [[0,0,0,	0,0,0,	0,0,0],
	#           [0,0,0,	0,0,0,	0,0,0],
	#           [0,0,0,	0,0,0,	0,0,0],

	#           [0,0,0,	0,0,0,	0,0,0],
	#           [0,0,0,	0,0,0,	0,0,0],
	#           [0,0,0,	0,0,0,	0,0,0],

	#           [0,0,0,	0,0,0,	0,0,0],
	#           [0,0,0,	0,0,0,	0,0,0],
	#           [0,0,0,	0,0,0,	0,0,0]]
	sudoku = [[0 for i in range(num_rows_cols)] for j in range(num_rows_cols)]


	# # Alternative 1 (easy)

	# # Taking input one number at a time
	# for row in range(num_rows_cols):
	# 	for col in range(num_rows_cols):
	# 		sudoku[row][col] = int(input("Enter for row "+str(row+1)+", column "+str(col+1)+": "))

	# # Taking input one line at a time
	# for row in range(num_rows_cols):
	# 	line = input("Enter entire row "+str(row+1)+", comma separated: ")
	# 	line = [("0"+x) for x in line.split(',')]
	# 	sudoku[row] = [int(x.strip()) for x in line]
	# 	print(sudoku[row])
	# 	if len(sudoku[row]) != num_rows_cols:
	# 		print("INVALID ROW INPUT PLEASE TRY AGAIN")
	# 		row -= 1


	# Alternative 2 - create a UI so user can input filled boxes visually
	# use ent_num[i][j].get() to retrieve data
	warn=0

	for row in range(num_rows_cols):
		for col in range(num_rows_cols):
			try:
				if int(ent_num[row][col].get()) in n_range:
					sudoku[row][col] = int(ent_num[row][col].get())
				else:
					warn=1
					wrow = row
					wcol = col
			except:
				if ent_num[row][col].get() == '' or ent_num[row][col].get() == '0':
					sudoku[row][col] = 0
				else:
					print("ERROR: Wrong input!!!")
					return [[9 for i in range(num_rows_cols)] for j in range(num_rows_cols)]


	# Alternative 3 - image processing (how hard would that be?)


	# Checking if vlue taken as input is correct
	print_sudoku(sudoku)
	if warn==1:
		print("\nWARNING: Please check row ",wrow," and column ",wcol)
	while 1:
		ans = input("Is this your sudoku? yes/no/exit (y/n/e): ")
		if ans=='n':
			return input_sudoku()
		elif ans=='y':
			break
		elif ans=='e':
			return 0
	
	return sudoku


def disp_sudoku_soln(sudoku):
	
	for i in range(3):
		for j in range(3):
			frame = tk.Frame(master=window)
			frame.grid(row=i, column=3+j, padx=5, pady=5)
			for a in range(3):
				for b in range(3):
					lbl_num = tk.Label(master=frame, width=2, text=sudoku[(3*i)+a][(3*j)+b])
					lbl_num.grid(row=a, column=b)

	frame = tk.Frame(master=window)
	frame.grid(row=4, column=4, padx=5, pady=5)
	lbl_solve = tk.Label(master=frame, text="SOLVED SUDOKU")
	lbl_solve.pack()


def print_sudoku(sudoku):
	''' Function to display sudoku. '''

	print()
	for row in sudoku:
		print(row)
	print()

def start_solve_sudoku():
	
	global size_row,size_col,n_range,num_rows_cols
	global num_soln, toggle, btn_reset, btn_solve

	btn_reset["state"]='disabled'
	btn_solve["state"]='disabled'

	sudoku = input_sudoku() 

	num_soln = 0 #number of solutions to sudoku, in multiple mode
	toggle = 1 #whether to confirm continuing after every 30 solutions
	
	# backtrack = 0, manual = 1, multiple = 0, without backtracking
	# backtrack = 1, manual = 0, multiple = x, only backtracking
	# backtrack = 1, manual = 1, multiple = x, hybrid (fastest)
	# backtrack = 1, manual = x, multiple = 1, prints every solution (if multiple)
	# NOTE: with multiple on, solved sudoku will not be returned
	backtrack = 1
	manual = 1
	multiple = 1

	if sudoku==0:
		btn_reset["state"]='normal'
		btn_solve["state"]='normal'
		return
	if not sudoku_checker(sudoku, solved=0):
		print("INVALID ENTRY\n")
		btn_reset["state"]='normal'
		btn_solve["state"]='normal'
		return
	if manual == 1:
		sudoku = solve_sudoku(sudoku,backtrack)
	elif manual == 0:
		sudoku = solve_sudoku_backtrack(sudoku)
	
	if multiple==0:
		print_sudoku(sudoku)	
		print("Is sudoku solved correctly? "+str(sudoku_checker(sudoku)))
	else:
		print("Number of solutions found: "+str(num_soln))

	btn_reset["state"]='normal'
	btn_solve["state"]='normal'


def reset_sudoku():
	
	for i in range(3):
		for j in range(3):
			frame = tk.Frame(master=window)
			frame.grid(row=i, column=j, padx=5, pady=5)
			for a in range(3):
				for b in range(3):
					ent_num[(3*i)+a][(3*j)+b].delete(0,'end')

def test_button():
	print("Button was clicked!")

def create_window():

	# Initialising variables
	global window, ent_num, btn_reset, btn_solve, btn_quit
	global size_row,size_col,n_range,num_rows_cols

	window = tk.Tk()

	ent_num = [[0 for i in range(num_rows_cols)] for j in range(num_rows_cols)]

	for i in range(3):
		for j in range(3):
			frame = tk.Frame(master=window)
			frame.grid(row=i, column=j, padx=5, pady=5)
			for a in range(3):
				for b in range(3):
					ent_num[(3*i)+a][(3*j)+b] = tk.Entry(master=frame, width=2)
					ent_num[(3*i)+a][(3*j)+b].grid(row=a, column=b)

	frame = tk.Frame(master=window)
	frame.grid(row=4, column=0, padx=5, pady=5)
	btn_reset = tk.Button(master=frame, text="RESET", command=reset_sudoku)
	btn_reset.pack()

	frame = tk.Frame(master=window)
	frame.grid(row=4, column=1, padx=5, pady=5)
	btn_solve = tk.Button(master=frame, text="SOLVE", command=start_solve_sudoku)
	btn_solve.pack()

	frame = tk.Frame(master=window)
	frame.grid(row=4, column=2, padx=5, pady=5)
	btn_quit = tk.Button(master=frame, text="QUIT", command=window.destroy)
	btn_quit.pack()

	window.mainloop()

if __name__ == '__main__':
	
	global size_row,size_col,n_range,num_rows_cols

	# Initialising sudoku dimensions
	size_row = 3
	size_col = 3
	num_rows_cols = size_row*size_col
	n_range = range(1, num_rows_cols+1)

	create_window()
	

