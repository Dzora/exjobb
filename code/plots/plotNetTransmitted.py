import matplotlib.pyplot as plt
import csv
import sys
import os


def readCSV(filename):
	file = open(filename)
	CSV = csv.reader(file,delimiter=';')
	return CSV


def readToArray(CSV):
	data = [];

	iterCSV = iter(CSV)
	next(iterCSV)
	for row in iterCSV:
		data.append(row[2])

	data = list(map(float, data))

	return data


def plotArray(data):

	
	xLabels = ["noTrace20", "jaeger20", "zipkin20", "noTrace40", "jaeger40", "zipkin40", "noTrace60", "jaeger60","zipkin60", "noTrace80","jaeger80","zipkin80", "noTrace100", "jaeger100", "zipkin100"]

	fig, ax = plt.subplots()
	ax.boxplot(data,sym='k+', whis=[1,99], showfliers=True)
	ax.set_xticklabels(xLabels, rotation=45)
	ax.set_ylabel("Bytes")
	ax.yaxis.grid(True, linestyle='-', which='major', color='lightgrey', alpha=0.5)
	ax.set_yscale('log')
	[ax.axvline(x, color = 'grey', linestyle='-') for x in [3.5,6.5,9.5,12.5]]
	#ax.set_ylim(-5, 400)
	ax.set_title("Total Network Transmitted")

	plt.show()

def openJaegerFiles():
	cur_path = os.path.dirname(__file__)
	new_path = os.path.relpath('..//resultsJaeger//20//totNetTrans_20.csv', cur_path)
	CSV = readCSV(new_path)
	jaeger20 = readToArray(CSV)

	cur_path = os.path.dirname(__file__)
	new_path = os.path.relpath('..//resultsJaeger//40//totNetTrans_40.csv', cur_path)
	CSV = readCSV(new_path)
	jaeger40 = readToArray(CSV)

	cur_path = os.path.dirname(__file__)
	new_path = os.path.relpath('..//resultsJaeger//60//totNetTrans_60.csv', cur_path)
	CSV = readCSV(new_path)
	jaeger60 = readToArray(CSV)

	cur_path = os.path.dirname(__file__)
	new_path = os.path.relpath('..//resultsJaeger//80//totNetTrans_80.csv', cur_path)
	CSV = readCSV(new_path)
	jaeger80 = readToArray(CSV)

	cur_path = os.path.dirname(__file__)
	new_path = os.path.relpath('..//resultsJaeger//100//totNetTrans_100.csv', cur_path)
	CSV = readCSV(new_path)
	jaeger100 = readToArray(CSV)

	return jaeger20, jaeger40, jaeger60, jaeger80, jaeger100

def openNoTracing():
	cur_path = os.path.dirname(__file__)
	new_path = os.path.relpath('..//resultsNoTracing//20//totNetTrans_20.csv', cur_path)
	CSV = readCSV(new_path)
	noTrace20 = readToArray(CSV)

	cur_path = os.path.dirname(__file__)
	new_path = os.path.relpath('..//resultsNoTracing//40//totNetTrans_40.csv', cur_path)
	CSV = readCSV(new_path)
	noTrace40 = readToArray(CSV)

	cur_path = os.path.dirname(__file__)
	new_path = os.path.relpath('..//resultsNoTracing//60//totNetTrans_60.csv', cur_path)
	CSV = readCSV(new_path)
	noTrace60 = readToArray(CSV)

	cur_path = os.path.dirname(__file__)
	new_path = os.path.relpath('..//resultsNoTracing//80//totNetTrans_80.csv', cur_path)
	CSV = readCSV(new_path)
	noTrace80 = readToArray(CSV)

	cur_path = os.path.dirname(__file__)
	new_path = os.path.relpath('..//resultsNoTracing//100//totNetTrans_100.csv', cur_path)
	CSV = readCSV(new_path)
	noTrace100 = readToArray(CSV)

	return noTrace20, noTrace40, noTrace60, noTrace80, noTrace100

def openZipkin():
	cur_path = os.path.dirname(__file__)
	new_path = os.path.relpath('..//resultsZipkin//20//totNetTrans_20.csv', cur_path)
	CSV = readCSV(new_path)
	zipkin20 = readToArray(CSV)

	cur_path = os.path.dirname(__file__)
	new_path = os.path.relpath('..//resultsZipkin//40//totNetTrans_40.csv', cur_path)
	CSV = readCSV(new_path)
	zipkin40 = readToArray(CSV)

	cur_path = os.path.dirname(__file__)
	new_path = os.path.relpath('..//resultsZipkin//60//totNetTrans_60.csv', cur_path)
	CSV = readCSV(new_path)
	zipkin60 = readToArray(CSV)

	cur_path = os.path.dirname(__file__)
	new_path = os.path.relpath('..//resultsZipkin//80//totNetTrans_80.csv', cur_path)
	CSV = readCSV(new_path)
	zipkin80 = readToArray(CSV)

	cur_path = os.path.dirname(__file__)
	new_path = os.path.relpath('..//resultsZipkin//100//totNetTrans_100.csv', cur_path)
	CSV = readCSV(new_path)
	zipkin100 = readToArray(CSV)

	return zipkin20, zipkin40, zipkin60, zipkin80, zipkin100

def main():

	noTrace20, noTrace40, noTrace60, noTrace80, noTrace100 = openNoTracing()
	
	jaeger20, jaeger40, jaeger60, jaeger80, jaeger100 = openJaegerFiles()

	zipkin20, zipkin40, zipkin60, zipkin80, zipkin100 = openZipkin()

	data = [noTrace20, jaeger20, zipkin20, noTrace40, jaeger40, zipkin40, noTrace60, jaeger60, zipkin60, noTrace80, jaeger80, zipkin80, noTrace100, jaeger100, zipkin100]

	plotArray(data)

if __name__ == "__main__":
	main()
