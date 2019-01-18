import csv
import cv2
import time
from os import listdir
from os.path import isfile, join
import numpy as np

trainfile = '/Users/abhaysinghal/Documents/Kaggle/Salt/train.csv'
mypath = '/Users/abhaysinghal/Documents/Kaggle/Salt/images'
depthfile = '/Users/abhaysinghal/Documents/Kaggle/Salt/depths.csv'

ids = [f for f in listdir(mypath) if isfile(join(mypath, f))] # list of image ids

reader = csv.reader(open(depthfile, 'r'))
depths = {}
for row in reader:
   k, v = row
   depths[k] = v

print(len(ids))

train = []
valid = []

t = time.clock()

print("Starting")

done_ids = [] # tracking processed images allows dataset generation in pieces in RAM constrained environments

i = 0
valid = []
dids = []

# repeat below code to generate a validation set containing separate images,
# break when i = desired number of images in train / valid set

with open("salt_test_final_test" + ".csv", "a") as my_csv:
    csvWriter = csv.writer(my_csv, delimiter=',')

    for id in ids:
        id = id[:-4]
        if id not in done_ids:
            dids.append([id])
            im = cv2.imread('/Users/abhaysinghal/Documents/Kaggle/Salt/images/' + id + '.png', cv2.IMREAD_GRAYSCALE)
            # mask = cv2.imread('/Users/abhaysinghal/Documents/Kaggle/Salt/train/masks/' + id + '.png', cv2.IMREAD_GRAYSCALE)
            # uncomment when generating train set

            max = np.amax(im)
            min = np.amin(im)
            avg = np.average(im)

            for x in range(im.shape[0]):
                for y in range(im.shape[1]):
                    valid = [id, int(depths[id]), x, y, im[x,y], # image id, depth, pixel x, pixel y, pixel greyscale
                                  im[x-1,y] if x > 0 else None, # greyscale pixel value of pixel left
                                  im[x+1,y] if x < 100 else None, # greyscale pixel value of pixel right
                                  im[x,y-1] if y > 0 else None, # greyscale pixel value of pixel above
                                  im[x,y+1] if y < 100 else None, # greyscale pixel value of pixel below
                                  max, min, avg, # greyscale max, min, mean values for each image
                                  # (mask[x,y]==255) # ground truth used in training
                                  ]
                    csvWriter.writerow(valid)
            if (i % 100) == 0:
                print("i: " + str(i))
                t = time.clock() - t
                print("Time: " + str(t))
            i += 1

t = time.clock() - t
print(t)

