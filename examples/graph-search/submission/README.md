# Graph Search

For this assignment, you will implement some common graph search algorithms.
For illustration purposes, this repo contains a starter implementation that randomly chooses an unexplored node to visit next.


## Sample data and evaluation

### Input format

`../sample/data` contain examples of what the input to your program will look like.
The starter code takes these inputs and constructs a graph, then runs a query over the graph.


### Output format

`../sample/gold` contains examples of what the output of your program must look like.
During evaluation, we will give your program different graphs and queries.


### Your submission program

Please implement `myprogram.py`.
The starter code runs each search algorithm (you have to implement them) and write out the exploration order of the algorithm to the output directory.
Please break ties using the provided `tie_break` function, which breaks ties alphabetically.
To implement A* search, please use the provided `heuristic` function.

Your submission must adhere to the [TestMe API](https://github.com/r2llab/testme).
In addition, please include a file in your submission (e.g. `user.txt`) that contains your UserID.
For convenience, we have created a `submit.sh` that produces a submission zip file.
Please modify `submit.sh` to include the files you require for your program to run.


### Evaluation
`../grader.py` contains the evaluation script we will use to evaluate your submission.
You can check your submission using the sample data we provide.

```
# Compile the submissions folder
bash submit.sh
# Run the grader and store output in tmp
python ../grader.py --submission submit --data ../sample/data --gold ../sample/gold --output tmp
```

During development, you can also mount your current directory as `/src` as you edit `myprogram.py` to generate predictions.

```
python ../grader.py --submission $PWD --data ../sample/data --gold ../sample/gold --output tmp
```

However, to avoid submission errors, please do a final check by mounting `submit` to `/src`.
Once you are comfortable with your submission, please submit `submit.zip`.
