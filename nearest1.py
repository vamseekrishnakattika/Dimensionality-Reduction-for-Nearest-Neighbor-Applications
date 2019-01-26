import numpy as np
import sys

if len(sys.argv) != 7 :
    print('usage : ', sys.argv[0], 'reduced_data_file vector_file labels_file queried_point_file label output_file')
    sys.exit()
  
reducedDataFile = open(sys.argv[1],"r")
vectorsFile = open(sys.argv[2],"r")
labelsFile = open(sys.argv[3],"r")
queriedPointFile = open(sys.argv[4],"r")
queriedLableFile = open(sys.argv[5],"r")
output_file = sys.argv[6]

data = np.loadtxt(reducedDataFile,delimiter=',')
vectors = np.loadtxt(vectorsFile,delimiter=',')
labels = np.loadtxt(labelsFile)
queried_points = np.loadtxt(queriedPointFile,delimiter=',')
queriedLable = np.loadtxt(queriedLableFile,delimiter=',')

nn_idx = []
vectors_r = vectors.T

lalbelList = labels.tolist()
labelsList = list(set(lalbelList))

reducedQueryPoint = np.dot(queried_points,vectors_r)

n = queried_points.shape

if(len(n)==2):
	for idx,rp in enumerate(reducedQueryPoint):
		if(queriedLable[idx]==-1):
			minDist = sys.maxsize
			index = []
			for i,xt in enumerate(data):
				dist = np.linalg.norm(rp-xt)
				if(dist<minDist):
					minDist = dist
			for i,xt in enumerate(data):
				dist = np.linalg.norm(rp-xt)
				if(dist==minDist):
					index.append(i)
			nn_idx.append(index)
		else:
			for label in labelsList:
				if(queriedLable[idx]==label):
					minDist = sys.maxsize
					index = []
					for i,xt in enumerate(data):
						if(labels[i]==label):
							dist = np.linalg.norm(rp-xt)
							if(dist<minDist):
								minDist = dist
					for i,xt in enumerate(data):
						if(labels[i]==label):
							dist = np.linalg.norm(rp-xt)
							if(dist==minDist):
								index.append(i)
					nn_idx.append(index)

np.savetxt(output_file, nn_idx, delimiter=',',fmt='%s')