#!/usr/bin/python

'''
 Student ID - 21249298
 Name - Karthik Elangkumaran
 Git URL - https://github.com/Karthikpek0512/ARC.git 
'''

import os, sys
import json
import numpy as np
import re

### YOUR CODE HERE: write at least three functions which solve
### specific tasks by transforming the input x and returning the
### result. Name them according to the task ID as in the three
### examples below. Delete the three examples. The tasks you choose
### must be in the data/training directory, not data/evaluation.
def solve_22eb0ac0(x):
    rows,columns = x.shape
    y = x.copy()
    for row in range(0,rows):      
        if(y[row][0] == y[row][columns-1] ):
            for column in range(0,columns):
                y[row][column] = y[row][0]
    return y

def solve_6cdd2623(x):
    rows,columns = x.shape
    row_traverse = x.copy()
    column_traverse = x.copy()
    match_val = 0
    for row in range(0,rows):
        for column in range(0,columns):
            if row_traverse[row][0] == row_traverse[row][columns-1]:
                match_val = max(row_traverse[row][0],match_val)
                row_traverse[row][column] = row_traverse[row][0]
            else:
                  row_traverse[row][column] = 0
    for column in range(0,columns): 
            for row in range(0,rows):
                if column_traverse[0][column] == column_traverse[rows-1][column] == match_val:
                    column_traverse[row][column] = column_traverse[0][column]
                else:
                      column_traverse[row][column] = 0
    return (np.where(row_traverse == 0, column_traverse, row_traverse))

def solve_d06dbe63(x):
    x = x.copy()
    rows, columns = x.shape
    start_row,start_column = np.where(x == x.max())
    start_row = int(start_row)
    up_traverse = int (start_column)
    iter_up = 1
## Iteratively traverse up midpoint moving 2 points up and 3 across till end of array 
    for row in range(start_row-1, -1,-1):
        if (iter_up % 2 == 0) :
            x[row][up_traverse] = 5
            if(up_traverse+1 < columns):
                x[row][up_traverse+1] = 5
            else:
                break
            if(up_traverse+1 < columns):
                x[row][up_traverse+2] = 5 
            else:
                break
            up_traverse+=2
        if (iter_up % 2 == 1) :
            x[row][up_traverse] = 5
        iter_up +=1
##initiate variable for next iteration        
    down_traverse = int (start_column)
    iter_down = 1
## Iteratively traverse up midpoint moving 2 points up and 2 across till end of array    
    for row in range(start_row+1, rows):
        if (iter_down % 2 == 0) : 
            x[row][down_traverse] = 5
            if down_traverse-1 >= 0:
                x[row][down_traverse-1] = 5 
            else:
                break
            if down_traverse-2 >= 0:
                x[row][down_traverse-2] = 5 
            else:
                break
            down_traverse-=2
        if (iter_down % 2 == 1)  :
            x[row][down_traverse] = 5
        iter_down +=1
    return x    
# This is a working solution for  6150a2bd - commented out because its very simple
# def solve_6150a2bd(x):
#     x = np.flip(x)
#     return x

def main():
    # Find all the functions defined in this file whose names are
    # like solve_abcd1234(), and run them.

    # regex to match solve_* functions and extract task IDs
    p = r"solve_([a-f0-9]{8})" 
    tasks_solvers = []
    # globals() gives a dict containing all global names (variables
    # and functions), as name: value pairs.
    for name in globals(): 
        m = re.match(p, name)
        if m:
            # if the name fits the pattern eg solve_abcd1234
            ID = m.group(1) # just the task ID
            solve_fn = globals()[name] # the fn itself
            tasks_solvers.append((ID, solve_fn))

    for ID, solve_fn in tasks_solvers:
        # for each task, read the data and call test()
        directory = os.path.join("..", "data", "training")
        json_filename = os.path.join(directory, ID + ".json")
        data = read_ARC_JSON(json_filename)
        test(ID, solve_fn, data)
    
def read_ARC_JSON(filepath):
    """Given a filepath, read in the ARC task data which is in JSON
    format. Extract the train/test input/output pairs of
    grids. Convert each grid to np.array and return train_input,
    train_output, test_input, test_output."""
    
    # Open the JSON file and load it 
    data = json.load(open(filepath))

    # Extract the train/test input/output grids. Each grid will be a
    # list of lists of ints. We convert to Numpy.
    train_input = [np.array(data['train'][i]['input']) for i in range(len(data['train']))]
    train_output = [np.array(data['train'][i]['output']) for i in range(len(data['train']))]
    test_input = [np.array(data['test'][i]['input']) for i in range(len(data['test']))]
    test_output = [np.array(data['test'][i]['output']) for i in range(len(data['test']))]

    return (train_input, train_output, test_input, test_output)


def test(taskID, solve, data):
    """Given a task ID, call the given solve() function on every
    example in the task data."""
    print(taskID)
    train_input, train_output, test_input, test_output = data
    print("Training grids")
    for x, y in zip(train_input, train_output):
        yhat = solve(x)
        show_result(x, y, yhat)
    print("Test grids")
    for x, y in zip(test_input, test_output):
        yhat = solve(x)
        show_result(x, y, yhat)

        
def show_result(x, y, yhat):
    print("Input")
    print(x)
    print("Correct output")
    print(y)
    print("Our output")
    print(yhat)
    print("Correct?")
    if y.shape != yhat.shape:
        print(f"False. Incorrect shape: {y.shape} v {yhat.shape}")
    else:
        print(np.all(y == yhat))


if __name__ == "__main__": main()

