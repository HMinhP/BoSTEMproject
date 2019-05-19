import matplotlib.pyplot
import copy
import random 

def data_to_2d(data, rows, columns):
    """
    Convert input 1D data list into a 2D list. 
    Data should be indexed by row number, column number 
       For example, l[0] = the first row, l[0][0] is the element in the first column of the first row
    Return the 2D list of data

    data: 1D list of data
    rows: number of rows 
    columns: number of columns 
    """
    
    list_2d= []
    i= 0
    for row in range (rows):
        list_2d.append([])
        for column in range (columns):
            list_2d[row].append(data[i])
            i = i + 1
    return list_2d
    
        

def read_file(name):
    """
    Return a list of ints out of a data file. Assumes input is whitespace separated. 

    name: file name
    """
    f = open(name, 'r')
    lines = f.read()
    chars = lines.split() # Splits on whitespace 
    nums = list(map(int, chars)) # Converts each string to a number
    return nums
    
def get_min(data):
    """
    Find the minimum value in data

    data: a 2D list of floats
    """
    # Your code here 
    new_value = data [0][0]
    for inner_list in data:
        for item in inner_list:
            if item < new_value:
                new_value = item
    return new_value
                

    
def get_max(data):
    """
    Find the minimum value in data

    data: a 2D list of floats 
    """
    # Your code here
    new_value = data [0] [0]
    for inner_list in data:
        for item in inner_list:
            if item > new_value:
                new_value = item
    return new_value

def convert_data_to_image(data, min_val, max_val):
    """
    Converts each value in data into a list of three floats between 0 and 1
    Data values that are max_val will be converted to [1,1,1]
    Data values that are min_val will be converted to [0,0,0] 
    All other values are scaled linearly between min and max 

    Return a 3D list representing the data 
    Leave input data list unchanged

    data: 2D list of floats representing elevation 
    min_val: minimum elevation value 
    max_val: maximum elevation value 
    """
    
    image = [] # new list of lists
    num_rows = len(data) # Number of rows is number of rows in 2D list
    num_cols = len(data[0]) # Number of columns is length of one row
    for row in range(num_rows):
        image.append([]) # Array to hold the values for this row 
        for column in range(num_cols):
            elevation = data[row][column]  
            pixel_val = [(elevation- min_val)/ (max_val-min_val),(elevation- min_val)/ (max_val-min_val),(elevation- min_val)/ (max_val-min_val)]
            image[row].append(pixel_val)
    return image
    
       
    

def calc_path(data, image, start_row):
    """
    Finds a lowest-elevation-change path starting at the given start row with a greedy algorithm 
    Draws the cells that path travels through in the image 
    
    Return 
    Change image list, DO NOT change data list (You'll need it to calculate other paths!)

    data: 2D list of elevation for every cell in your map 
    image: 3D list of pixel values for every cell in your map 
    start_row: row to start searching on 
    """
    
    green= [0,1,0]
    image[50][50] = green
    row= start_row
    column=0
    for column in range(len(image[row])-1):
        #print(column)
        #image[50][column]=green
        upper_box = data[(row+1)][(column+1)]
        current_box= data[row][column]
        lower_box= data[row-1][column+1]
        next_box= data[row][column+1]
        move_up= (data[row+1][column+1])- (data[row][column])
        move_down= (data[row][column]) - (data[row-1][column+1])
        forward= (data[row][column+1]) - (data[row][column])
        
        total_elevation=0        
        if abs(move_up) < abs (forward) and abs(move_up) < abs(move_down):
            image[(row+1)][(column+1)] = green
            current_box = upper_box 
            row=row+1
            change= abs(move_up)
       
            
            
        elif abs(forward) < abs(move_up) and abs(forward) < abs(move_down):
            image[row][column+1] = green
            current_box = next_box 
            change= abs(forward)
            
        elif abs(forward) < abs(move_down) or abs(forward) == abs(move_down):
            image[row][column+1] = green
            current_box = next_box
            change= abs(forward)
            
           
        elif abs(move_down) < abs(move_up):
            image[row-1][column+1] = green
            current_box = lower_box
            row=row-1
            change= abs(move_down)
            
            
        elif abs(move_down) < abs (forward):
            image[row-1][column+1] = green
            current_box = lower_box
            row=row-1
            change = abs(move_down)
            
            
        elif abs(move_up) == abs(move_down) == abs(forward):
            image[row][column+1] = green
            current_box = next_box
            change = abs(forward)
        
        
            
        elif abs(move_up) == abs(move_down):
            if (random.random()) > .5:  
                current_box= upper_box
                change= abs(move_up)
                #row=row+1
            else:
                current_box = lower_box
                change= abs(move_down) 
                #row=row-1
        
        
               
        total_elevation=total_elevation+change
    return total_elevation
    
    
    
    return image 
    
    
def run_colorado():
    """
    Load in Colorado data, convert it to an image, 
    then run your path finding algorithm on every starting row. 
    Find the starting row with the least total elevation change
    and print it with its elevation change. The best elevation change
    should be around 15000 meters. 
    """


## Test functions 
    
    data_1d = read_file("Colorado_844x480.dat")
    data = data_to_2d(data_1d, 480, 844)
    image = convert_data_to_image(data, get_min(data), get_max(data))
    calc_path(data,image,100)
    matplotlib.pyplot.imshow(image)
    matplotlib.pyplot.show()

    
def test_min_max():
    ## Test for min_value:
    test = [[2,2,2],[3,2,3],[2,1,2]]
    test2 = [[-2,-2,-2],[-3,-2,-4],[-2,-1,-2]]
    if get_min(test) != 1 or get_min(test2) != -4:
        print("get_min test failed")
    else:
        print("get_min test succeeded") 
    if get_max(test) != 3 or get_max(test2) != -1:
        print("get_max test failed")
    else:
        print("get_max test succeeded")

def test_convert_data_2d():
    ## Test with small set
    test = [2,2,2,3,3,3]
    two_d = data_to_2d(test, 2, 3)
    if len(two_d) == 2 and len(two_d[0])==3 and two_d[0][0] == 2:
        print("Small conversion test succeeded, trying big test")
        data_1d = read_file("Colorado_844x480.dat")
        data = data_to_2d(data_1d, 480, 844)
        if data[0][0] != 2564 or data[50][50] != 2074 or data[99][99] != 2038 or data[479][843] != 1110:
            print("Big conversion to 2d failed")
        else:
            print ("Conversion to 2D test succeeded")
            
# Assumes a working data_to_2d and min/max
def test_convert_data_image():
    data_1d = read_file("Colorado_844x480.dat")
    data = data_to_2d(data_1d, 480, 844)
    # Check dimensions of converted image
    image = convert_data_to_image(data, get_min(data), get_max(data))
    if len(image[0][0]) == 3 and len(image[479][843]) == 3:
        print("Dimensions of image conversion ok, displaying image.")
        matplotlib.pyplot.imshow(image)
        matplotlib.pyplot.show()

# Assumes working data_to_2d, convert_data_to_image, min, max
def test_calc_path():
    data_1d = read_file("testMountains.dat")
    data = data_to_2d(data_1d, 100, 100)
    image = convert_data_to_image(data, get_min(data), get_max(data))
    calc_path(data,image,40)
    if calc_path(data, image, 1) == 0 and calc_path(data, image, 40) == 0 and calc_path(data, image, 49) == 0:
        print("Elevation change in test map was sensible. Test image should display with 3 paths.")
    matplotlib.pyplot.imshow(image)
    matplotlib.pyplot.show()
        

## Calls to test functions - uncomment when you are ready to test a method
    
test_min_max()
test_convert_data_2d()
test_convert_data_image()
test_calc_path()

## Once you're done testing, run your full route finding algorithm!

run_colorado()


    
