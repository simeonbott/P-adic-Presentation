#!/usr/bin/env python
# coding: utf-8

# In[9]:


#Writing a sequence of numbers to higher and higher powers.
#The user can set the following variables:
#starting_value, the first number in the sequence.
#depth, the length of the sequence to show on screen.
#accuracy, the length of numbers to show on screen.
#power, the rate of increase in size of the numbers in the sequence.
#base, normally people use base = 10. This code supports values up to 36.
import numpy as np
import random
import math
from tabulate import tabulate
import matplotlib.pyplot as plt
power = 10
base = 10
accuracy = 40
depth =40
starting_value = 18
alpha = [str(i) for i in range(10)] + [chr(i+65) for i in range(26)]

answer = [starting_value] + ["none"] * (depth-1)
answer_length = [math.floor(1 + math.log(starting_value, base))] + ["none"] * (depth-1)
for i in range(1,depth):
    previous_answer, new_answer = answer[i-1], answer[i-1]
    for j in range(power - 1):
        new_answer = (new_answer*previous_answer) % (base**accuracy)
    answer[i] = new_answer
    answer_length[i] = math.floor(1 + math.log(starting_value, base)*power**i)
    
#base converter.
if base != 10:
    for i in range(depth):
        converted = []
        number = answer[i]
        while number > 0:
            converted.append(alpha[(number % base)])
            number //= base
        converted.reverse()
        answer[i] = "".join(converted)
else:
    for i in range(len(answer)):
        answer[i] = str(answer[i])
    
#matplotlib section.
image = np.zeros(accuracy*depth)

for i in range(depth):
    for j in range(len(answer[i])):
        image[accuracy*i + j + accuracy - len(answer[i])] = alpha.index(answer[i][j])
image = image.reshape((depth, accuracy))
plt.matshow(image)
plt.show()

#tabulate section.
table = ["none"] * (depth)
for i in  range(depth):
    if answer_length[i] > accuracy:
        answer[i] = str(answer[i]).zfill(accuracy)
        z = "..."
    else:
        z = "" 
    table[i] = [answer_length[i], "", str(starting_value) + "^(" + str(power) + "^" + str(i) + ")", "=", z, answer[i]]
col_names = ["length (number of digits)", "", "number", "", "", "value (base " + str(base) + ")"]
print(tabulate(table, headers=col_names, stralign="right"))


# In[ ]:




