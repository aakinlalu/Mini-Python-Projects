#!/usr/bin/env python
"""
Created on Thu Aug 14 19:53:55 2014

@author: adebayo

read a list of points from a CSV file and print out the length of the perimiter of the shape that is formed by joining the points in their listed order

"""

import csv
import sys
import numpy


def main(file_name):
    

    with open(file_name, 'rb') as fp:
        reader = csv.reader(fp, delimiter = ' ')
        
        points = []
        try:
            header = True
            for row in reader:
                if header:
                    header = False
                    continue
                x = row[0]
                y = row[1]
                points.append([x,y])
        except csv.Error as e:
           sys.exit('file %s, line %d %s' %('filename', reader.line_num, e))
                
    print points
    
    points = convert(points)
    
    points = numpy.array(points)   
    
    length = perimeter(points)

    print length

if __name__ == "__main__":

    file_name = sys.argv[0]
    main(file_name)
    

def convert(points):
    """ to convert list of string to list of int  """
    distance = []
    for i in points:
        x = int(i[0])
        y = int(i[1])
        distance.append([x,y])
    return distance
    
def perimeter(points):
    """ 
        Calculates polygon perimeter.
        x = points[:,0], y = points[:,1]
    """
    points1 = numpy.roll(points,-1,axis = 0) # shift by -1
    return numpy.sum(numpy.sqrt((points1[:,0] - points[:,0])**2 + (points1[:,1] - points[:,1])**2))