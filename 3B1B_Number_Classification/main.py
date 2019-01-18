import numpy as np
from sympy import *
import numpy.matlib as mat

multSigmoid = 1

def m_sum(m):
    val=0
    for i in range(0, len(m)):
        val+=m[i]
    return val


def m_sub(m1, m2):
    if(len(m1)==len(m2)):
        tempArray=[]
        for i in range(0, len(m1)):
            tempArray.append(m1[i]-m2[i])
        return tempArray

def m_pow(m1, m2):
    tempArray=[]
    for i in range(0, len(m1)):
        tempArray.append(pow(m1[i],m2))
    return tempArray


def sigmoid(z):
    return 1.0/(1+2.718281**(-multSigmoid*z))

def sigmoidArray(z):
    tempVar = []
    for i in range(0, len(z)):
        tempVar.append(sigmoid(z[i]))
    return tempVar

def inverseSigmoid(z):
    if z != 1:
        return (1.0/multSigmoid)*ln(z/(1-z))
    return "DNE"

def getMaxIndex(array):
    k = 0
    max = array[k]

    for i in range(0, len(array)):
        if array[i] > max:
            max = array[i]
            k = i

    return k

def getMax(array):
    k = 0
    max = array[k]

    for i in range(0, len(array)):
        if array[i] > max:
            max = array[i]
            k = i

    return max

training = [
    # [[5, 10], 20],
    # [[6, 12], 24],
    # [[9, 18], 36]
]

for i in range(0, 100):
    training.append([])
    var = np.random.randint(20)

    for j in range(0, 2):
        if (j%2) == 0:
            training[i].append([var, 2*var])
        else:
            training[i].append(4*var)

values = []
answer = []

for i in range(0, len(training)):
    for j in range(0, len(training[i])):
        if (j % 2) == 0:
            values.append(training[i][j])
        else:
            answer.append(training[i][j])

class Neural_Network():

    def __init__(self, layers):
        self.layers = layers
        self.wb = [] #weights and biases
        self.pwb = [] #previous weights and biases
        self.trained = False

        for i in range(0, self.layers.__len__()-1):
            self.wb.append([])
            for j in range(0, self.layers[i+1]):
                self.wb[i].append([])
                for k in range(0, self.layers[i]+1):
                    self.wb[i][j].append(1)
        self.pwb = 0

    def func(self, input):
        neurons = []

        for i in range(0, len(self.layers)):
            neurons.append([])
            for j in range (0, self.layers[i]):
                neurons[i].append(0)

        neurons[0] = input

        for i in range(0, len(self.layers)-1): #previous layer
            for j in range(0, self.layers[i+1]): #current neuron
                tempVar = 0
                for k in range(0, self.layers[i]): #previous layer's neurons
                    tempVar += neurons[i][k] * self.wb[i][j][k]
                    tempVar += self.wb[i][j][k+1]
                neurons[i+1][j] = sigmoid(tempVar)
        return neurons[len(self.layers)-1]

    def getAnswer(self, input):
        return getMaxIndex(self.func(input))

    def getAnswerContinuous(self, input):
        print(self.func(input)[0])
        return inverseSigmoid(self.func(input)[0])

    def getCost(self, val: object, answer: object) -> object:
        wanted = []
        for i in range(0, 10):
            wanted.append(0)
        wanted[answer] = 1
        return m_sum(m_pow(m_sub(self.func(val), wanted), 2))/(2*len(answer))

    def partialDer(self, i, j, k, y):
        pass

    def gradientDescent(self, data, answers, alpha):
        tempArray = self.wb
        pCost = 0
        cost = 0

        for i in range(0, len(self.layers) - 1):  # previous layer
            for j in range(0, self.layers[i + 1]):  # current neuron
                for k in range(0, self.layers[i]):  # previous layer's neurons
                    tempArray[i][j][k] = 0

        for h in range(0, len(data)):
            for i in range(0, len(self.layers) - 1):  # previous layer
                for j in range(0, self.layers[i + 1]):  # current neuron
                    for k in range(0, self.layers[i]):  # previous layer's neurons
                            tempArray[i][j][k] += alpha*(self.getAnswerContinuous(data[h]) - answers[h])
            pCost += self.getCost(data[h], answers[h])
        self.wb += tempArray

        for h in range(0, len(data)):
            cost += self.getCost(data[h], answers[h])
            # print(self.getCost(data[h], answers[h])

    # def normalEquations(self, input):
    #     features = mat.matrix(input)

net = Neural_Network([2, 3, 1])
net.gradientDescent(values, answer, 0.01)

print(net.getAnswerContinuous(2, 4))
# print(inverseSigmoid(0.5))