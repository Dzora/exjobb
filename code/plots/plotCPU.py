import matplotlib.pyplot as plt
import csv
import sys
import os


def readCSV(filename):
	file = open(filename)
	CSV = csv.reader(file,delimiter=';')
	return CSV


def readCPUToArray(CSV):
	data = [];

	iterCSV = iter(CSV)
	next(iterCSV)
	for row in iterCSV:
		data.append(row[2])

	data = list(map(float, data))

	return data


def plotArray(data):

	
	xLabels = ["noTrace20", "jaeger20", "zipkin20", "noTrace40", "jaeger40", "zipkin40", "noTrace60", "jaeger60","zipkin60", "noTrace80","jaeger80","zipkin80", "noTrace100", "jaeger100", "zipkin100"]

	#xLabels = ["jeger20","jeger40","jaeger60","jaeger80", "jaeger100"]
	fig, ax = plt.subplots()
	ax.boxplot(data,sym='k+', whis=[1,99], showfliers=True)
	ax.set_xticklabels(xLabels, rotation=45)
	ax.set_ylabel("Total % (Max 1600)")
	ax.yaxis.grid(True, linestyle='-', which='major', color='lightgrey', alpha=0.5)

	[ax.axvline(x, color = 'grey', linestyle='-') for x in [3.5,6.5,9.5,12.5]]
	#ax.set_ylim(-5, 400)
	ax.set_title("Total CPU")

	plt.show()

def openJaegerFiles():
	cur_path = os.path.dirname(__file__)
	new_path = os.path.relpath('..//resultsJaeger//20//totCPU_20.csv', cur_path)
	CSV = readCSV(new_path)
	jaeger20 = readCPUToArray(CSV)

	cur_path = os.path.dirname(__file__)
	new_path = os.path.relpath('..//resultsJaeger//40//totCPU_40.csv', cur_path)
	CSV = readCSV(new_path)
	jaeger40 = readCPUToArray(CSV)

	cur_path = os.path.dirname(__file__)
	new_path = os.path.relpath('..//resultsJaeger//60//totCPU_60.csv', cur_path)
	CSV = readCSV(new_path)
	jaeger60 = readCPUToArray(CSV)

	cur_path = os.path.dirname(__file__)
	new_path = os.path.relpath('..//resultsJaeger//80//totCPU_80.csv', cur_path)
	CSV = readCSV(new_path)
	jaeger80 = readCPUToArray(CSV)

	cur_path = os.path.dirname(__file__)
	new_path = os.path.relpath('..//resultsJaeger//100//totCPU_100.csv', cur_path)
	CSV = readCSV(new_path)
	jaeger100 = readCPUToArray(CSV)

	return jaeger20, jaeger40, jaeger60, jaeger80, jaeger100

def openNoTracing():
	cur_path = os.path.dirname(__file__)
	new_path = os.path.relpath('..//resultsNoTracing//20//totCPU_20.csv', cur_path)
	CSV = readCSV(new_path)
	noTrace20 = readCPUToArray(CSV)

	cur_path = os.path.dirname(__file__)
	new_path = os.path.relpath('..//resultsNoTracing//40//totCPU_40.csv', cur_path)
	CSV = readCSV(new_path)
	noTrace40 = readCPUToArray(CSV)

	cur_path = os.path.dirname(__file__)
	new_path = os.path.relpath('..//resultsNoTracing//60//totCPU_60.csv', cur_path)
	CSV = readCSV(new_path)
	noTrace60 = readCPUToArray(CSV)

	cur_path = os.path.dirname(__file__)
	new_path = os.path.relpath('..//resultsNoTracing//80//totCPU_80.csv', cur_path)
	CSV = readCSV(new_path)
	noTrace80 = readCPUToArray(CSV)

	cur_path = os.path.dirname(__file__)
	new_path = os.path.relpath('..//resultsNoTracing//100//totCPU_100.csv', cur_path)
	CSV = readCSV(new_path)
	noTrace100 = readCPUToArray(CSV)

	return noTrace20, noTrace40, noTrace60, noTrace80, noTrace100

def openZipkin():
	cur_path = os.path.dirname(__file__)
	new_path = os.path.relpath('..//resultsZipkin//20//totCPU_20.csv', cur_path)
	CSV = readCSV(new_path)
	zipkin20 = readCPUToArray(CSV)

	cur_path = os.path.dirname(__file__)
	new_path = os.path.relpath('..//resultsZipkin//40//totCPU_40.csv', cur_path)
	CSV = readCSV(new_path)
	zipkin40 = readCPUToArray(CSV)

	cur_path = os.path.dirname(__file__)
	new_path = os.path.relpath('..//resultsZipkin//60//totCPU_60.csv', cur_path)
	CSV = readCSV(new_path)
	zipkin60 = readCPUToArray(CSV)

	cur_path = os.path.dirname(__file__)
	new_path = os.path.relpath('..//resultsZipkin//80//totCPU_80.csv', cur_path)
	CSV = readCSV(new_path)
	zipkin80 = readCPUToArray(CSV)

	cur_path = os.path.dirname(__file__)
	new_path = os.path.relpath('..//resultsZipkin//100//totCPU_100.csv', cur_path)
	CSV = readCSV(new_path)
	zipkin100 = readCPUToArray(CSV)

	return zipkin20, zipkin40, zipkin60, zipkin80, zipkin100

def main():

	noTrace20, noTrace40, noTrace60, noTrace80, noTrace100 = openNoTracing()
	
	jaeger20, jaeger40, jaeger60, jaeger80, jaeger100 = openJaegerFiles()

	zipkin20, zipkin40, zipkin60, zipkin80, zipkin100 = openZipkin()

	data = [noTrace20, jaeger20, zipkin20, noTrace40, jaeger40, zipkin40, noTrace60, jaeger60, zipkin60, noTrace80, jaeger80, zipkin80, noTrace100, jaeger100, zipkin100]

	#CSV = readCSV(sys.argv[1])

	#data = readCPUToArray(CSV)
	plotArray(data)

if __name__ == "__main__":
	main()
