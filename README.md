# Dimensionality-Reduction-for-Nearest-Neighbor-Applications

Feature extraction can be guided by various criteria. In this part our goal is to perform dimensionality
reduction for nearest neighbor applications. Specifically, training is performed with the input. Then, given a test vector x of length m, it is reduced into two dimensions vx; vy. The
program searches for the vector in the training data that is nearest to vx; vy and returns its index.

You are asked to implement such programs for two cases. In the first case all items in the training data
are candidates for the nearest neighbor. In the second case the nearest neighbor must be of a specific label.

Programs

1. reducedim1.py : reduced dimension for the first case.

2. reducedim2.py : reduced dimension for the second case.

3. nearest.py : find nearest neighbor.

The arguments for reducedim1.py and reducedim2.py are the same as in Part I. The arguments for
nearest.py are as follows:

nearest.py reduced.txt V.txt labels.txt label

Here reduced.txt and V.txt are the output files of the dimensionality reduction programs. labels.txt is
the same as the input to the dimensionality reduction program. If Label is 1/2/3/ compute nearest neighbor
of the appropriate label. Otherwise ignore the label in computing the nearest neighbor.

The output of the program is the row of the nearest neighbor in the reduced.txt file.
