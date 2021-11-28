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
#def solve_0dfd9992(x):
#    return x

def solve_22eb0ac0(x):
    rows = x.shape[0]
    columns = x.shape[1]
    for i in range(0,rows):
        if(x[i][0] != 0):
            if(x[i][0] == x[i][columns-1]):
                for j in range(0,columns):
                    x[i][j] = x[i][0]
    return x

# def top_d06dbe6(x,pos_x,pos_y):
#     columns = x.shape[1]
    
#     if((pos_x < (0)) or (pos_y == columns)):
#         return
    
#     if((pos_x-1)<0):
#         return
#     x[pos_x-1][pos_y] = 5;
    
#     if((pos_x-2)<0):
#         return
#     x[pos_x-2][pos_y] = 5;
    
#     if((pos_y+1) == columns):
#         return
#     x[pos_x-2][pos_y+1] = 5;
    
#     if((pos_y+2)<0):
#         return
#     x[pos_x-2][pos_y+2] = 5; 

#     return top_d06dbe6(x,pos_x-2,pos_y+2)

# def bottom_d06dbe6(x,pos_x,pos_y):
#     rows = x.shape[0]
    
#     if((pos_x >= (rows)) or (pos_y < 0 )):
#         return
    
#     if((pos_x+1) >= rows):
#         return
#     x[pos_x+1][pos_y] = 5;
    
#     if((pos_x+2) >= rows):
#         return
#     x[pos_x+2][pos_y] = 5;
    
#     if((pos_y-1) < 0):
#         return
#     x[pos_x+2][pos_y-1] = 5;
    
#     if((pos_y-2)<0):
#         return
#     x[pos_x+2][pos_y-2] = 5; 

#     return bottom_d06dbe6(x,pos_x+2,pos_y-2)
    

# def solve_d06dbe63(x):
#     mid = 8
#     rows = x.shape[0]
#     columns = x.shape[1]
#     mid_x = 0
#     mid_y = 0
#     for i in range(0,rows-1):
#         for j in range(0,columns-1):
#             if(x[i][j] == mid):
#                 mid_x = i
#                 mid_y = j
#     top_d06dbe6(x,mid_x,mid_y)
#     bottom_d06dbe6(x,mid_x,mid_y)
#     return x
    

def solve_6150a2bd(x):
    x = np.flip(x)
    return x

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

