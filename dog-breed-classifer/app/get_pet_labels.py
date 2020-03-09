#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Leo Tomatsu
# DATE CREATED: 03/07/2020                                 
# REVISED DATE: 
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir, path

# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create 
#       with this function
# 
def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    # Replace None with the results_dic dictionary that you created with this
    # function
    
    # Retrieve the filesnames from image_dir
    filename_list = listdir(image_dir)
    # Create list of labels
    label_list = []
    
    # Populate labels based on filename
    for filename in filename_list:
        # ignore dot/hidden files
        if not filename.startswith('.'):
            # remove file extensions
            filename = path.splitext(filename)[0]
            # Sets string to lower case letters
            low_filename = filename.lower()
            # Splits lower case string by _ to break into words
            word_list_filename = low_filename.split("_")
            # Create label starting as empty string
            label = ''
            # Loops to check if word in filename is only
            # alphabetic characters - if true append word
            # to filename separated by trailing space
            for word in word_list_filename:
                if word.isalpha():
                    label += word + ' '
            # Remove final trailing space
            label = label.strip()
            # Append label to label list
            label_list.append(label)
     
        
    # Create empty dictionary
    results_dic = dict()
    
    # Adds new key-value pairs to the dictionary ONLY
    # when key doesn't already exist. This dictionary
    # value is a list that contains only one item - the
    # image name label
    for index in range(len(filename_list)):
        filename = filename_list[index]
        if filename not in results_dic:
            results_dic[filename] = [label_list[index]]
    return results_dic
