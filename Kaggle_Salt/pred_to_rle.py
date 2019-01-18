import numpy as np
import csv
from os import listdir
from os.path import isfile, join
import pandas as pd
import time
import gc
import scipy.misc

t = time.clock()

predfile = '/Users/abhaysinghal/Documents/Kaggle/Salt/autoencoded_mamodevu_preds_fccf7389.csv' # Driverless AI predictions
mypath = '/Users/abhaysinghal/Documents/Kaggle/Salt/images'
iden = [f for f in listdir(mypath) if isfile(join(mypath, f))] # image ids
n = len(iden)
# n = 100
rows = 101*101*n
preds = pd.read_csv(predfile, sep=",", low_memory=False, nrows=rows, names = ["False", "True"]) # load predictions with pandas
print(preds.shape)
preds2 = pd.DataFrame((preds["False"] < preds["True"]), columns = ["salt"]) # reduces True/False probability to boolean
preds = preds2
gc.collect()
print("Read")
print(preds.shape)

print("Done with preds")
t = time.clock() - t
print("Time:" + str(t))

preds = np.asarray(preds)
preds = np.reshape(preds, (n, 101, 101))
print(preds.shape)

images = {}
for i in range(preds.shape[0]):
    # print(i)
    iden[i] = iden[i][:-4]
    images[iden[i]] = (preds[i][:][:]).astype(np.float32)
    scipy.misc.imsave('/Users/abhaysinghal/Documents/Kaggle/Salt/autoencoder_predictions/' + iden[i] + '.png', images[iden[i]])

print("Converted to image")
t = time.clock() - t
print("Time:" + str(t))

def rle(x): # written by rakhlin, https://www.kaggle.com/rakhlin/fast-run-length-encoding-python
    '''
    x: numpy array of shape (height, width), 1 - mask, 0 - background
    Returns run length as list
    '''
    dots = np.where(x.T.flatten()>=0.5)[0] # .T sets Fortran order down-then-right
    run_lengths = []
    prev = -2
    for b in dots:
        if (b>prev+1): run_lengths.extend((b+1, 0))
        run_lengths[-1] += 1
        prev = b

    rl = str(run_lengths)
    rl = rl.replace(',', '')
    rl = rl.replace('[', '')
    rl = rl.replace(']', '')
    return rl

rlepred = []
for i in range(preds.shape[0]):
    rlepred.append([iden[i], rle(images[iden[i]])]) # generates submission dataframe

print("Converted to predictions array")
t = time.clock() - t
print("Time:" + str(t))

with open("salt_submission.csv","w+") as my_csv: # saves submission dataframe to csv
    csvWriter = csv.writer(my_csv,delimiter=',')
    csvWriter.writerow(["id", "rle_mask"])
    csvWriter.writerows(rlepred)

print("Done with CSV")
t = time.clock() - t
print("Time:" + str(t))