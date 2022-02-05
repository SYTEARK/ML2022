from netCDF4 import Dataset
import matplotlib.pyplot as plt
import numpy as np

# Import netCDF file
ncfile = 'data/ex_1_10.nc'
data = Dataset(ncfile)
var = data.variables

# Use latex
plt.rc('text', usetex=True)
plt.rc('font', family='serif')

# Prepare Plot
plt.figure(figsize=(10,6), dpi=300)
plt.title(r"Histogram for experiments", fontsize=16)
plt.xlabel(r'$\nu$', fontsize=14)
plt.ylabel(r'Numbers', fontsize=14)

# Prepare Data to Plot
nu_1 = var['nu_1'][:]
nu_rand = var['nu_rand'][:]
nu_min = var['nu_min'][:]

# Plot with Legends
plt.hist(nu_1, bins=30, color='red', label=r'$\nu_1$', alpha=0.5)
plt.hist(nu_rand, bins=30, color='blue', label=r'$\nu_{\rm rand}$', alpha=0.5)
plt.hist(nu_min, bins=30, color='orange', label=r'$\nu_{\rm min}$', alpha=0.5)

# Other options
plt.legend(fontsize=12)
plt.grid()
plt.savefig("hist.png", dpi=300)

def calc_confidence(nu, mu, epsilon):
    return np.count_nonzero(np.abs(nu - mu) > epsilon) / len(nu)

def hoeffding_bound(epsilon):
    return 2 * np.exp(-2 * epsilon ** 2 * 10)

epsilon = np.arange(0, 0.51, 0.01)

f_1 = lambda x: calc_confidence(nu_1, 0.5, x)
f_1 = np.vectorize(f_1)
c_1 = f_1(epsilon)

f_rand = lambda x: calc_confidence(nu_rand, 0.5, x)
f_rand = np.vectorize(f_rand)
c_rand = f_rand(epsilon)

f_min = lambda x: calc_confidence(nu_min, 0.5, x)
f_min = np.vectorize(f_min)
c_min = f_min(epsilon)

plt.figure(figsize=(10,6), dpi=300)
plt.title(r"Hoeffding Bound for experiments", fontsize=16)
plt.xlabel(r'$\epsilon$', fontsize=14)
plt.ylabel(r'$\nu$', fontsize=14)

plt.plot(epsilon, c_1, color='red', label=r'$\nu_1$', alpha=0.5)
plt.plot(epsilon, c_rand, color='blue', label=r'$\nu_{\rm rand}$', alpha=0.5)
plt.plot(epsilon, c_min, color='orange', label=r'$\nu_{\rm min}$', alpha=0.8)
plt.plot(epsilon, hoeffding_bound(epsilon), color='black', label=r'Hoeffding Bound', alpha=0.5)

plt.legend(fontsize=12)
plt.grid()
plt.savefig("hoeffding.png", dpi=300)