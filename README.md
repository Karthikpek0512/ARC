# Purpose of this fork/repository

This repository contains solution for 3 tasks in the The Abstraction and Reasoning Corpus (ARC). Further details on ARC data and testing interface for the tasks is provided in the desciption of the orginal respository below.
Please note that all grids visually represented in the tasks are 2-d array and each color is represented by a number from 0-9 Ex : Back is represented by zero.

## Below is snapshot of task_22eb0ac0
![task_22eb0ac0](https://github.com/Karthikpek0512/ARC/blob/master/Tasks/22eb0ac0.PNG)

### Description of task
The task is to analyse each row in the grid horizontally. When the  start and end point of the row in the grid is the same colour the expected output is to link the two points with the same color.

### Transformation required
A python function that accepts a 2-d array as input. The function should then traverse each row of the array, when the start and end point is the same fill the row with the same number.
Please refer to comments in the code https://github.com/Karthikpek0512/ARC/blob/master/src/manual_solve.py for detailed comments on the rationale of the code.

### Testing results
The method provided correct result for all test and training grids.

## Below is snapshot of task_6cdd2623
![task_6cdd2623](https://github.com/Karthikpek0512/ARC/blob/master/Tasks/6cdd2623.PNG)

### Description of task
The task is to analyse each row in the grid  horizontally and then vertically. When the  start and end point of the row in the grid is the same colour when traversing horizontally they should connected by the same colour.
While traversing vertically if the the start and end are same color (should also be the same colour as horizontal match) then they are connected by same colour. 
Once the vertical and horizontal elements are connected the grids filled with colours outside of the link should be detaulted to black(ie.,0). Refer Task demonstration ex 3 which covers all scenarios.

### Transformation required
A python function that accepts a 2-d array as input. The function should first traverse each row of the array, when the start and end point is the same fill the row with the same number also store the number.
Next is vertical traversal to find the start and end points with same value and connected them with same number . Finally numbers outside of the link should be changed to zero(black)
Please refer to comments in the code https://github.com/Karthikpek0512/ARC/blob/master/src/manual_solve.py for detailed comments on the rationale of the code.

### Testing results
The method provided correct result for all test and training grids.


# Original forked repository description
## The Abstraction and Reasoning Corpus (ARC)

Original repository contains the ARC task data, as well as a browser-based interface for humans to try their hand at solving the tasks manually.

*"ARC can be seen as a general artificial intelligence benchmark, as a program synthesis benchmark, or as a psychometric intelligence test. It is targeted at both humans and artificially intelligent systems that aim at emulating a human-like form of general fluid intelligence."*

A complete description of the dataset, its goals, and its underlying logic, can be found in: [The Measure of Intelligence](https://arxiv.org/abs/1911.01547).

As a reminder, a test-taker is said to solve a task when, upon seeing the task for the first time, they are able to produce the correct output grid for *all* test inputs in the task (this includes picking the dimensions of the output grid). For each test input, the test-taker is allowed 3 trials (this holds for all test-takers, either humans or AI).


## Task file format

The `data` directory contains two subdirectories:

- `data/training`: contains the task files for training (400 tasks). Use these to prototype your algorithm or to train your algorithm to acquire ARC-relevant cognitive priors.
- `data/evaluation`: contains the task files for evaluation (400 tasks). Use these to evaluate your final algorithm. To ensure fair evaluation results, do not leak information from the evaluation set into your algorithm (e.g. by looking at the evaluation tasks yourself during development, or by repeatedly modifying an algorithm while using its evaluation score as feedback).

The tasks are stored in JSON format. Each task JSON file contains a dictionary with two fields:

- `"train"`: demonstration input/output pairs. It is a list of "pairs" (typically 3 pairs).
- `"test"`: test input/output pairs. It is a list of "pairs" (typically 1 pair).

A "pair" is a dictionary with two fields:

- `"input"`: the input "grid" for the pair.
- `"output"`: the output "grid" for the pair.

A "grid" is a rectangular matrix (list of lists) of integers between 0 and 9 (inclusive). The smallest possible grid size is 1x1 and the largest is 30x30.

When looking at a task, a test-taker has access to inputs & outputs of the demonstration pairs, plus the input(s) of the test pair(s). The goal is to construct the output grid(s) corresponding to the test input grid(s), using 3 trials for each test input. "Constructing the output grid" involves picking the height and width of the output grid, then filling each cell in the grid with a symbol (integer between 0 and 9, which are visualized as colors). Only *exact* solutions (all cells match the expected answer) can be said to be correct.


## Usage of the testing interface

The testing interface is located at `apps/testing_interface.html`. Open it in a web browser (Chrome recommended). It will prompt you to select a task JSON file.

After loading a task, you will enter the test space, which looks like this:

![test space](https://arc-benchmark.s3.amazonaws.com/figs/arc_test_space.png)

On the left, you will see the input/output pairs demonstrating the nature of the task. In the middle, you will see the current test input grid. On the right, you will see the controls you can use to construct the corresponding output grid.

You have access to the following tools:

### Grid controls

- Resize: input a grid size (e.g. "10x20" or "4x4") and click "Resize". This preserves existing grid content (in the top left corner).
- Copy from input: copy the input grid to the output grid. This is useful for tasks where the output consists of some modification of the input.
- Reset grid: fill the grid with 0s.

### Symbol controls

- Edit: select a color (symbol) from the color picking bar, then click on a cell to set its color.
- Select: click and drag on either the output grid or the input grid to select cells.
    - After selecting cells on the output grid, you can select a color from the color picking to set the color of the selected cells. This is useful to draw solid rectangles or lines.
    - After selecting cells on either the input grid or the output grid, you can press C to copy their content. After copying, you can select a cell on the output grid and press "V" to paste the copied content. You should select the cell in the top left corner of the zone you want to paste into.
- Floodfill: click on a cell from the output grid to color all connected cells to the selected color. "Connected cells" are contiguous cells with the same color.

### Answer validation

When your output grid is ready, click the green "Submit!" button to check your answer. We do not enforce the 3-trials rule.

After you've obtained the correct answer for the current test input grid, you can switch to the next test input grid for the task using the "Next test input" button (if there is any available; most tasks only have one test input).

When you're done with a task, use the "load task" button to open a new task.
