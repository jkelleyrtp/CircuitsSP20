#%%

import os, subprocess
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
#%%
# dir_addr = "../data/experiment2/block1"
dir_addr = "../data/experiment2/block2"

#%%
for file in os.listdir(dir_addr):
    print(file+" is the filename")

# %%
data = []
for file in os.listdir(dir_addr):
    # Add the tuple
    data.append(pd.read_csv(dir_addr+"/"+file, delimiter=","))
    # data.append( (file, np.genfromtxt(dir_addr+"/"+file, delimiter=",")))

fig = plt.figure(dpi = 200)

idx = 1
for (data_as_np) in data:
    # ax = plt.subplot(len(data), 1, idx)
    plt.plot(data_as_np['V'], data_as_np['I'] * 1e6)
    # plt.legend("Rail: " + str(idx))
    idx += 1
plt.legend([
    "Rail 1",
    "Rail 2",
    "Rail 3",
    "Rail 4",
    "Rail 5",
    "Rail 6",
    "Rail 7",
    "Rail 8",
])
plt.xlabel("Voltgage (Volts)")
plt.ylabel("Current (microamps)")
plt.show()


# %%
a = pd.read_csv(dir_addr+"/"+file, delimiter=",")
# %%
plt.plot(a['V'], a['I'])


# %%
