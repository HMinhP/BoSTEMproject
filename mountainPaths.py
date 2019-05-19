import matplotlib.pyplot
import copy
import random 
"""
def read_data(name, rows, columns):
    
    Read data from file
    Save the data as floats in a 2D list indexed by row number, column number 
       For example, l[0] = the first row, l[0][0] is the element in the first column of the first row
    Return the 2D list of data

    name: file name
    rows: number of rows 
    columns: number of columns 
 """
    # Your code here
def get_min(data):
    """
    Find the minimum value in data

    data: a 2D list of floats
    """
    # Your code here 
    new_value = [0] [0]
    for inner_list in data:
        for item in inner_list:
            if item < new_value:
                return new_value 
             
                
             
                
                
                
                
            
        
               

def get_max(data):
    """
    Find the minimum value in data

    data: a 2D list of floats 
    """
    # Your code here 
    new_value = [0] [0]
    for inner_list in data:
        for item in inner_list:
            if item > new_value:
                return new_value 


## Test for min_value:
test = [[2,2,2],[3,2,3],[2,1,2]]
test2 = [[-2,-2,-2],[-3,-2,-3],[-2,-1,-2]]
if get_min(test) != 1 or get_min(test2) != -3:
    print("get_min test failed")
else:
    print("get_min test succeeded") 
if get_max(test) != 3 or get_max(test2) != -1:
    print("get_max test failed")
else:
    print("get_max test succeeded")

## Test for read_data
data = read_data("Colorado_844x480.dat", 480, 844)

if data[0][0] != 2564.0 or data[50][50] != 2074.0 or data[99][99] != 2038.0:
    print("read_data test failed")
else:
    print("read_data test succeeded")
    matplotlib.pyplot.imshow(data)
    matplotlib.pyplot.show()
