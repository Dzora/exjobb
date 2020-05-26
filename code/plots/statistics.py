import matplotlib.pyplot as plt
import csv
import sys
import os
import numpy as np
from matplotlib.lines import Line2D
from matplotlib.patches import Polygon
from scipy import stats



def readCSV(filename):
	file = open(filename)
	CSV = csv.reader(file,delimiter=',')
	return CSV


def readLatencyToArray(CSV):
	label = sys.argv[1]
	data = [];

	iterCSV = iter(CSV)
	next(iterCSV)
	for row in iterCSV:
		if row[2] == label:
			data.append(row[4])

	#print(home)		

	data = list(map(int, data))

	return data


def plotArray(data):

	data = sorted(data)
	fit = stats.norm.pdf(data, np.mean(data), np.std(data))  #this is a fitting indeed
	print(data)

	plt.plot(data,fit,'-o')


	plt.hist(data, bins=range(min(data), max(data) + 1, 1))
	
	#plt.hist(data, bins=[0, 5, 10, 15, 20, 25, 30])
	plt.show()

def openJaegerFiles():
	cur_path = os.path.dirname(__file__)
	new_path = os.path.relpath('..//resultsJaeger//20//TestResult_20200504-122725.csv', cur_path)
	CSV = readCSV(new_path)
	jaeger20 = readLatencyToArray(CSV)

	cur_path = os.path.dirname(__file__)
	new_path = os.path.relpath('..//resultsJaeger//40//TestResult_20200504-123927.csv', cur_path)
	CSV = readCSV(new_path)
	jaeger40 = readLatencyToArray(CSV)

	cur_path = os.path.dirname(__file__)
	new_path = os.path.relpath('..//resultsJaeger//60//TestResult_20200504-125129.csv', cur_path)
	CSV = readCSV(new_path)
	jaeger60 = readLatencyToArray(CSV)

	cur_path = os.path.dirname(__file__)
	new_path = os.path.relpath('..//resultsJaeger//80//TestResult_20200504-130332.csv', cur_path)
	CSV = readCSV(new_path)
	jaeger80 = readLatencyToArray(CSV)

	cur_path = os.path.dirname(__file__)
	new_path = os.path.relpath('..//resultsJaeger//100//TestResult_20200504-131534.csv', cur_path)
	CSV = readCSV(new_path)
	jaeger100 = readLatencyToArray(CSV)

	return jaeger20, jaeger40, jaeger60, jaeger80, jaeger100

def openNoTracing():
	cur_path = os.path.dirname(__file__)
	new_path = os.path.relpath('..//resultsNoTracing//20//TestResult_20200504-105859.csv', cur_path)
	CSV = readCSV(new_path)
	noTrace20 = readLatencyToArray(CSV)

	cur_path = os.path.dirname(__file__)
	new_path = os.path.relpath('..//resultsNoTracing//40//TestResult_20200504-111102.csv', cur_path)
	CSV = readCSV(new_path)
	noTrace40 = readLatencyToArray(CSV)

	cur_path = os.path.dirname(__file__)
	new_path = os.path.relpath('..//resultsNoTracing//60//TestResult_20200504-112304.csv', cur_path)
	CSV = readCSV(new_path)
	noTrace60 = readLatencyToArray(CSV)

	cur_path = os.path.dirname(__file__)
	new_path = os.path.relpath('..//resultsNoTracing//80//TestResult_20200504-113506.csv', cur_path)
	CSV = readCSV(new_path)
	noTrace80 = readLatencyToArray(CSV)

	cur_path = os.path.dirname(__file__)
	new_path = os.path.relpath('..//resultsNoTracing//100//TestResult_20200504-114709.csv', cur_path)
	CSV = readCSV(new_path)
	noTrace100 = readLatencyToArray(CSV)

	return noTrace20, noTrace40, noTrace60, noTrace80, noTrace100

def openZipkin():
	cur_path = os.path.dirname(__file__)
	new_path = os.path.relpath('..//resultsZipkin//20//TestResult_20200504-135859.csv', cur_path)
	CSV = readCSV(new_path)
	zipkin20 = readLatencyToArray(CSV)

	cur_path = os.path.dirname(__file__)
	new_path = os.path.relpath('..//resultsZipkin//40//TestResult_20200504-141101.csv', cur_path)
	CSV = readCSV(new_path)
	zipkin40 = readLatencyToArray(CSV)

	cur_path = os.path.dirname(__file__)
	new_path = os.path.relpath('..//resultsZipkin//60//TestResult_20200504-142304.csv', cur_path)
	CSV = readCSV(new_path)
	zipkin60 = readLatencyToArray(CSV)

	cur_path = os.path.dirname(__file__)
	new_path = os.path.relpath('..//resultsZipkin//80//TestResult_20200504-143506.csv', cur_path)
	CSV = readCSV(new_path)
	zipkin80 = readLatencyToArray(CSV)

	cur_path = os.path.dirname(__file__)
	new_path = os.path.relpath('..//resultsZipkin//100//TestResult_20200504-144709.csv', cur_path)
	CSV = readCSV(new_path)
	zipkin100 = readLatencyToArray(CSV)

	return zipkin20, zipkin40, zipkin60, zipkin80, zipkin100

def ttest(data1, data2):
	lenData1 = len(data1)
	lenData2 = len(data2)
	if(lenData1 != lenData2):
		if(lenData1 < lenData2):
			data2.pop()
		if(lenData1 > lenData2):
			data1.pop()


	stat, p = stats.mannwhitneyu(data1, data2,alternative='greater')

	print('Statistics=%.3f, p=%.1000f' % (stat, p))
	# interpret
	alpha = 0.05
	if p > alpha:
		print('fail to reject H0')
	else:
		print('reject H0')
	

def main():

	noTrace20, noTrace40, noTrace60, noTrace80, noTrace100 = openNoTracing()
	
	jaeger20, jaeger40, jaeger60, jaeger80, jaeger100 = openJaegerFiles()

	zipkin20, zipkin40, zipkin60, zipkin80, zipkin100 = openZipkin()

	#data = [noTrace20, jaeger20, zipkin20, noTrace40, jaeger40, zipkin40, noTrace60, jaeger60, zipkin60, noTrace80, jaeger80, zipkin80, noTrace100, jaeger100, zipkin100]

	#plotArray(jaeger20)



	jaeger = jaeger20 + jaeger40 + jaeger60 + jaeger80 + jaeger100
	zipkin = zipkin20 + zipkin40 + zipkin60 + zipkin80 + zipkin100

	ttest(jaeger,zipkin)

if __name__ == "__main__":
	main()
