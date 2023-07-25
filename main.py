import csv
import copy
from utilities import create_random_array
from utilities import bubble_sort, selection_sort, quick_sort

#create empty arrays for each of the arrays used
test_array = []
bubble_comparisons_list = []
selection_comparisons_list = []
quick_comparisons_list = []

input_list_type = input("What sort of list do you want to sort (random, ordered, reverse)?")

#compare different sorting algorithums and print them to csv file 
#open/create the file
with open('Sort.csv','w',newline='') as csvfile:
    #create the writer object
    csvwriter = csv.writer(csvfile)
    #write header row
    csvwriter.writerow(['data points','bubble', 'selection', 'quick'])
    #create a data for array size 5 to 100 inclusive
    for data_points in range(5, 201):
        #for each array create a new random array and then sort using the three
        #sorting algorithums
        for i in range(10):
            #create a random array of numbers that will be sorted
            match input_list_type:
                case "random":
                    test_array = create_random_array(data_points)
                case "ordered":
                    for i in range(data_points):
                        test_array.append(i)
                case "reverse":
                    for i in reversed(range(data_points)):
                        test_array.append(i)
                case "same":
                    for i in range(data_points):
                        test_array.append(1)

            #deep copy the array
            temp_array = copy.deepcopy(test_array)
            temp_array, bubble_comparisons = bubble_sort(temp_array)
            bubble_comparisons_list.append(bubble_comparisons)

            temp_array = copy.deepcopy(test_array)
            temp_array, selection_comparisons = selection_sort(temp_array)
            selection_comparisons_list.append(selection_comparisons)

            temp_array = copy.deepcopy(test_array)
            temp_array, quick_comparisons = quick_sort(temp_array)
            quick_comparisons_list.append(quick_comparisons)

            test_array = []
        
        #average each of the sorting methods
        bubble_average = sum(bubble_comparisons_list)/len(bubble_comparisons_list)
        selection_average = sum(selection_comparisons_list)/len(selection_comparisons_list)
        quick_average = sum(quick_comparisons_list)/len(quick_comparisons_list)
        
        #write a line for each random array that is sorted of size 5 to 100
        csvwriter.writerow([data_points, bubble_average, selection_average, quick_average])
        
        #zero all the comarrison lists
        bubble_comparisons_list = []
        selection_comparisons_list = []
        quick_comparisons_list = []
