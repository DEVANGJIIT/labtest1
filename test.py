import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as signal


temp_data = np.random.uniform(10, 200, size=1440)

noise = np.random.normal(0, 1, size=1440) * 3
noisy_data = temp_data + noise

plt.plot(noisy_data)
plt.show()


fs = 1 
cutoff = 0.1  
b, a = signal.butter(10, cutoff, fs=fs, btype='lowpass')
smoothed_data = signal.filtfilt(b, a, noisy_data)
plt.plot(smoothed_data)
plt.show()




        
