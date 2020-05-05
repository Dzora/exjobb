import matplotlib.pyplot as plt
import csv
import sys
import os


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

	
	xLabels = ["noTrace20", "jaeger20", "zipkin20", "noTrace40", "jaeger40", "zipkin40", "noTrace60", "jaeger60","zipkin60", "noTrace80","jaeger80","zipkin80", "noTrace100", "jaeger100", "zipkin100"]

	fig, ax = plt.subplots()
	ax.boxplot(data,sym='k+', whis=[1,99], showfliers=False)
	ax.set_xticklabels(xLabels, rotation=45)
	ax.set_ylabel("Milliseconds")
	ax.yaxis.grid(True, linestyle='-', which='major', color='lightgrey', alpha=0.5)

	[ax.axvline(x, color = 'grey', linestyle='-') for x in [3.5,6.5,9.5,12.5]]
	#ax.set_ylim(0, 600)
	ax.set_title(sys.argv[1])

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

def main():

	noTrace20, noTrace40, noTrace60, noTrace80, noTrace100 = openNoTracing()
	
	jaeger20, jaeger40, jaeger60, jaeger80, jaeger100 = openJaegerFiles()

	zipkin20, zipkin40, zipkin60, zipkin80, zipkin100 = openZipkin()

	data = [noTrace20, jaeger20, zipkin20, noTrace40, jaeger40, zipkin40, noTrace60, jaeger60, zipkin60, noTrace80, jaeger80, zipkin80, noTrace100, jaeger100, zipkin100]

	plotArray(data)

if __name__ == "__main__":
	main()
