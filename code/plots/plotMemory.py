import matplotlib.pyplot as plt
import csv
import sys
import os
import numpy as np
from matplotlib.lines import Line2D
from matplotlib.patches import Polygon


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
	newData = []

	for i in data:
		newData.append((i / 60000000000) * 100)

	return newData


def plotArray(data):

	
	xLabels = ["noTrace20", "jaeger20", "zipkin20", "noTrace40", "jaeger40", "zipkin40", "noTrace60", "jaeger60","zipkin60", "noTrace80","jaeger80","zipkin80", "noTrace100", "jaeger100", "zipkin100"]

	fig, ax = plt.subplots()
	bp = ax.boxplot(data,sym='k+', whis=[1,99], showfliers=True)
	ax.set_xticklabels(xLabels, rotation=45)
	ax.set_ylabel("Total % (Max 100)")
	ax.yaxis.grid(True, linestyle='-', which='major', color='lightgrey', alpha=0.5)
	#ax.set_yscale('log')
	[ax.axvline(x, color = 'grey', linestyle='-') for x in [3.5,6.5,9.5,12.5]]

	box_colors = ['darkkhaki', 'royalblue','purple']
	num_boxes = len(data)
	medians = np.empty(num_boxes)
	for i in range(num_boxes):
	    box = bp['boxes'][i]
	    boxX = []
	    boxY = []
	    for j in range(5):
	        boxX.append(box.get_xdata()[j])
	        boxY.append(box.get_ydata()[j])
	    box_coords = np.column_stack([boxX, boxY])
	    # Alternate between Dark Khaki and Royal Blue
	    ax.add_patch(Polygon(box_coords, facecolor=box_colors[i % 3]))
	    # Now draw the median lines back over what we just filled in
	    med = bp['medians'][i]
	    medianX = []
	    medianY = []
	    for j in range(2):
	        medianX.append(med.get_xdata()[j])
	        medianY.append(med.get_ydata
	        	()[j])
	        ax.plot(medianX, medianY, 'k')
	    medians[i] = medianY[0]

	custom_lines = [Line2D([0], [0], color='darkkhaki', lw=4),
                Line2D([0], [0], color='royalblue', lw=4),
                Line2D([0], [0], color='purple', lw=4)]

	ax.legend(custom_lines, ['No Tracing','Jaeger','Zipkin'])

	ax.set_title("Total Memory")

	plt.show()

def openJaegerFiles():
	cur_path = os.path.dirname(__file__)
	new_path = os.path.relpath('..//resultsJaeger//20//totMem_20.csv', cur_path)
	CSV = readCSV(new_path)
	jaeger20 = readToArray(CSV)

	cur_path = os.path.dirname(__file__)
	new_path = os.path.relpath('..//resultsJaeger//40//totMem_40.csv', cur_path)
	CSV = readCSV(new_path)
	jaeger40 = readToArray(CSV)

	cur_path = os.path.dirname(__file__)
	new_path = os.path.relpath('..//resultsJaeger//60//totMem_60.csv', cur_path)
	CSV = readCSV(new_path)
	jaeger60 = readToArray(CSV)

	cur_path = os.path.dirname(__file__)
	new_path = os.path.relpath('..//resultsJaeger//80//totMem_80.csv', cur_path)
	CSV = readCSV(new_path)
	jaeger80 = readToArray(CSV)

	cur_path = os.path.dirname(__file__)
	new_path = os.path.relpath('..//resultsJaeger//100//totMem_100.csv', cur_path)
	CSV = readCSV(new_path)
	jaeger100 = readToArray(CSV)

	return jaeger20, jaeger40, jaeger60, jaeger80, jaeger100

def openNoTracing():
	cur_path = os.path.dirname(__file__)
	new_path = os.path.relpath('..//resultsNoTracing//20//totMem_20.csv', cur_path)
	CSV = readCSV(new_path)
	noTrace20 = readToArray(CSV)

	cur_path = os.path.dirname(__file__)
	new_path = os.path.relpath('..//resultsNoTracing//40//totMem_40.csv', cur_path)
	CSV = readCSV(new_path)
	noTrace40 = readToArray(CSV)

	cur_path = os.path.dirname(__file__)
	new_path = os.path.relpath('..//resultsNoTracing//60//totMem_60.csv', cur_path)
	CSV = readCSV(new_path)
	noTrace60 = readToArray(CSV)

	cur_path = os.path.dirname(__file__)
	new_path = os.path.relpath('..//resultsNoTracing//80//totMem_80.csv', cur_path)
	CSV = readCSV(new_path)
	noTrace80 = readToArray(CSV)

	cur_path = os.path.dirname(__file__)
	new_path = os.path.relpath('..//resultsNoTracing//100//totMem_100.csv', cur_path)
	CSV = readCSV(new_path)
	noTrace100 = readToArray(CSV)

	return noTrace20, noTrace40, noTrace60, noTrace80, noTrace100

def openZipkin():
	cur_path = os.path.dirname(__file__)
	new_path = os.path.relpath('..//resultsZipkin//20//totMem_20.csv', cur_path)
	CSV = readCSV(new_path)
	zipkin20 = readToArray(CSV)

	cur_path = os.path.dirname(__file__)
	new_path = os.path.relpath('..//resultsZipkin//40//totMem_40.csv', cur_path)
	CSV = readCSV(new_path)
	zipkin40 = readToArray(CSV)

	cur_path = os.path.dirname(__file__)
	new_path = os.path.relpath('..//resultsZipkin//60//totMem_60.csv', cur_path)
	CSV = readCSV(new_path)
	zipkin60 = readToArray(CSV)

	cur_path = os.path.dirname(__file__)
	new_path = os.path.relpath('..//resultsZipkin//80//totMem_80.csv', cur_path)
	CSV = readCSV(new_path)
	zipkin80 = readToArray(CSV)

	cur_path = os.path.dirname(__file__)
	new_path = os.path.relpath('..//resultsZipkin//100//totMem_100.csv', cur_path)
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
