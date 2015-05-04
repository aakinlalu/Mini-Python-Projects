# -*- coding: utf-8 -*-
"""
Created on Thu Aug 14 02:38:34 2014

@author: adebayo
"""
import csv, sys, numpy
with open('rand1.csv', 'rb') as fp:
        reader = csv.reader(fp)
        
        points = []
        try:
            header = True
            for row in reader:
                if header:
                    header = False
                    continue
                x = int(row[0])
                y = int(row[1])
                points.append([x,y])
        except csv.Error as e:
           sys.exit('file %s, line %d %s' %('triangle.csv', reader.line_num, e))

print points



def perimeter(points):
    """ 
        Calculates polygon perimeter.
        x = points[:,0], y = points[:,1]
    """
    points1 = numpy.roll(points,-1,axis = 0) # shift by -1
    return numpy.sum(numpy.sqrt((points1[:,0] - points[:,0])**2 + (points1[:,1] - points[:,1])**2))

points = numpy.array(points)   
    
length = perimeter(points)


print length
