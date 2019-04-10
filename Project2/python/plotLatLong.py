import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import pandas as pd

def plotlatlong(matlab_ind):
    filename = 'Temple.txt'
    columns = ["temple name", "location","index","lat","long" ]
    temples = pd.read_csv(filename, delimiter='\t', names=columns)

    matlab_ind = np.subtract(np.array(matlab_ind),1).astype(int)

    lat_coords = temples.values[:,3]
    long_coords = temples.values[:,4] # long is negative in the US

    lat_coords = lat_coords[matlab_ind]
    long_coords = long_coords[matlab_ind]

    fig = plt.figure(figsize=(8, 8))
    m = Basemap(projection='lcc', resolution=None,
                width=6E6, height=6E6, 
                lat_0=45, lon_0=-100,)
    m.etopo(scale=1.0, alpha=0.5)

    # Map (long, lat) to (x, y) for plotting
    x,y = m(long_coords,lat_coords)  
    plt.plot(x, y)
    plt.show()
    
if __name__ == "__main__":
    matlab_ind = [52,48,36,39,62,50,23,69,68,1,34,59,25,16,5,46,21,14,3,41,49,35,24,8,47,15,33,27,18,12,65,42,29,0,66,6,20,17,71,53,40,19,45,28,58,9,44,10,31,67,4,56,26,70,7,38,63,13,61,2,51,37,55,57,22,32,43,60,54,30,64,11,52]
    newpath = [52.0, 48.0, 36.0, 62.0, 10.0, 43.0, 50.0, 23.0, 69.0, 68.0, 39.0, 71.0, 1.0, 34.0, 59.0, 16.0, 25.0, 46.0, 21.0, 14.0, 3.0, 41.0, 24.0, 8.0, 12.0, 49.0, 35.0, 47.0, 15.0, 27.0, 18.0, 33.0, 5.0, 65.0, 29.0, 42.0, 72.0, 66.0, 6.0, 20.0, 17.0, 53.0, 40.0, 19.0, 45.0, 58.0, 28.0, 70.0, 44.0, 9.0, 31.0, 67.0, 4.0, 56.0, 26.0, 7.0, 38.0, 63.0, 13.0, 61.0, 2.0, 51.0, 37.0, 55.0, 57.0, 22.0, 32.0, 60.0, 54.0, 30.0, 64.0, 11.0]
    bestpathsofar = [20.0, 52.0, 48.0, 36.0, 40.0, 62.0, 17.0, 19.0, 50.0, 23.0, 69.0, 68.0, 39.0, 1.0, 34.0, 59.0, 25.0, 16.0, 5.0, 46.0, 21.0, 14.0, 3.0, 41.0, 49.0, 35.0, 24.0, 8.0, 47.0, 15.0, 33.0, 18.0, 27.0, 12.0, 65.0, 42.0, 29.0, 72.0, 66.0, 6.0, 67.0, 71.0, 38.0, 53.0, 45.0, 28.0, 58.0, 9.0, 44.0, 10.0, 31.0, 64.0, 26.0, 56.0, 70.0, 4.0, 7.0, 63.0, 13.0, 61.0, 2.0, 51.0, 37.0, 55.0, 57.0, 22.0, 32.0, 43.0, 60.0, 54.0, 30.0, 11.0]
    percentage1 = [26.0, 52.0, 70.0, 48.0, 36.0, 60.0, 39.0, 17.0, 62.0, 50.0, 23.0, 69.0, 68.0, 1.0, 34.0, 59.0, 25.0, 16.0, 5.0, 46.0, 21.0, 14.0, 3.0, 41.0, 49.0, 35.0, 24.0, 47.0, 15.0, 33.0, 27.0, 18.0, 12.0,
65.0, 8.0, 42.0, 29.0, 72.0, 66.0, 6.0, 20.0, 71.0, 53.0, 40.0, 19.0, 45.0, 28.0, 58.0, 9.0, 44.0, 10.0, 31.0, 67.0, 4.0, 56.0, 7.0, 38.0, 63.0, 13.0, 61.0, 2.0, 51.0, 37.0, 55.0, 57.0, 22.0, 32.0, 43.0, 54.0, 30.0, 64.0, 11.0]
    percentage2 = [50.0, 52.0, 48.0, 20.0, 36.0, 43.0, 39.0, 62.0, 23.0, 69.0, 68.0, 1.0, 34.0, 59.0, 25.0, 16.0, 5.0, 46.0, 21.0, 14.0, 3.0, 41.0, 49.0, 47.0, 35.0, 24.0, 8.0, 15.0, 33.0, 27.0, 18.0, 12.0, 65.0, 42.0, 29.0, 72.0, 66.0, 6.0, 17.0, 53.0, 40.0, 31.0, 45.0, 28.0, 58.0, 9.0, 44.0, 10.0, 67.0, 4.0, 56.0, 26.0, 19.0, 70.0, 7.0, 38.0, 71.0, 63.0, 13.0, 61.0, 2.0, 51.0, 37.0, 55.0, 57.0, 22.0, 32.0, 60.0, 54.0, 30.0, 64.0, 11.0]
    bext = [48.0, 40.0, 11.0, 34.0, 35.0, 49.0, 18.0, 16.0, 12.0, 66.0, 15.0, 7.0, 51.0, 61.0, 21.0, 5.0, 3.0, 27.0, 36.0, 45.0, 26.0, 60.0, 64.0, 69.0, 38.0, 4.0, 63.0, 6.0, 46.0, 52.0, 31.0, 29.0, 72.0, 62.0, 1.0, 13.0, 37.0, 22.0, 67.0, 44.0, 57.0, 53.0, 70.0, 32.0, 54.0, 43.0, 59.0, 42.0, 33.0, 47.0, 25.0, 50.0, 2.0, 20.0, 71.0, 39.0, 9.0, 19.0, 56.0, 65.0, 41.0, 24.0, 8.0, 14.0, 23.0, 28.0, 10.0, 58.0, 30.0, 55.0, 17.0, 68.0]
    plotlatlong(bext)
