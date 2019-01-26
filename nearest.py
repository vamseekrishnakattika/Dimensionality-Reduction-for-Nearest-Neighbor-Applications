import numpy as np
import sys

if len(sys.argv) != 7 :
    print('usage : ', sys.argv[0], 'reduced_data_file vector_file labels_file queried_point_file label output_file')
    sys.exit()
  
reducedDataFile = open(sys.argv[1],"r")
vectorsFile = open(sys.argv[2],"r")
labelsFile = open(sys.argv[3],"r")
queriedPointFile = open(sys.argv[4],"r")
queriedLable = int(sys.argv[5])
output_file = sys.argv[6]

data = np.loadtxt(reducedDataFile,delimiter=',')
vectors = np.loadtxt(vectorsFile,delimiter=',')
labels = np.loadtxt(labelsFile)
queried_points = np.loadtxt(queriedPointFile,delimiter=',')
nn_idx = []
vectors_r = vectors.T

lalbelList = labels.tolist()
labelsFile = list(set(lalbelList))

reducedQueryPoint = np.dot(queried_points,vectors_r)

n = queried_points.shape

if(len(n)==2):
	if(queriedLable==-1):
		for rp in reducedQueryPoint:
			minDist = sys.maxsize
			for i,xt in enumerate(data):
				dist = np.linalg.norm(rp-xt)
				if(dist<minDist):
					minDist = dist
					idx = i
			nn_idx.append(idx)
	for label in labelsFile:	
		if(queriedLable==label):
			for rp in reducedQueryPoint:
				minDist = sys.maxsize
				for i,xt in enumerate(data):
					if(labels[i]==label):
						dist = np.linalg.norm(rp-xt)
						if(dist<minDist):
							minDist = dist
							idx = i
				nn_idx.append(idx)

		
if(len(n)==1):
	if(queriedLable==-1):
		minDist = sys.maxsize
		for i,xt in enumerate(data):
			dist = np.linalg.norm(reducedQueryPoint-xt)
			if(dist<minDist):
				minDist = dist
				idx = i
		nn_idx.append(idx)

	for label in labelsFile:	
		if(queriedLable==label):
			minDist = sys.maxsize
			for i,xt in enumerate(data):
				if(labels[i]==label):
					dist = np.linalg.norm(rp-xt)
					if(dist<minDist):
						minDist = dist
						idx = i
			nn_idx.append(idx)	
			
np.savetxt(output_file, nn_idx, delimiter=',')