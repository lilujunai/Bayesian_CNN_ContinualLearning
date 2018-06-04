import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.style.use("seaborn")
import re
import numpy as np
plt.rc('font', family='serif', size=16)
plt.rcParams.update({'xtick.labelsize': 16, 'ytick.labelsize': 16, 'axes.labelsize': 16})

tasks = 2  # tasks continually learnt

os.chdir("/home/felix/Dropbox/publications/Bayesian_CNN_continual/results/")

with open("diagnostics_1.txt", 'r') as file:
    acc = re.findall(r"'acc':\s+tensor\((.*?)\)", file.read())
    print(acc)

train_1 = acc[1::2]
valid_1 = acc[0::2]
train_1 = np.array(train_1).astype(np.float32)
valid_1 = np.array(valid_1).astype(np.float32)

with open("diagnostics_2.txt", 'r') as file:
    acc = re.findall(r"'acc':\s+tensor\((.*?)\)", file.read())
    print(acc)

train_2 = acc[1::2]
valid_2 = acc[0::2]
train_2 = np.array(train_2).astype(np.float32)
valid_2 = np.array(valid_2).astype(np.float32)

with open("diagnostics_2_eval.txt", 'r') as file:
    valid_2_eval = re.findall(r"'acc':\s+tensor\((.*?)\)", file.read())
    print(valid_2_eval)

valid_2_eval = np.array(valid_2_eval).astype(np.float32)

f = plt.figure(figsize=(10, 8))

plt.plot(valid_1, "--", label=r"Validation, prior: $U(a, b)$", color='maroon')
plt.plot(valid_2, "--", label=r"Validation, prior: $q(w | \theta_A)$", color='navy')
plt.plot(valid_2_eval, "--", label=r"Validation task A after training task B", color='#89c765')


plt.xlabel("Epochs")
plt.ylabel("Accuracy")
x_ticks = range(len(valid_1))
plt.xticks(x_ticks[9::10], map(lambda x: x+1, x_ticks[9::10]))

f.suptitle("Evaluating continual learning")
plt.legend(loc=5)

plt.savefig("results_continual.png")
