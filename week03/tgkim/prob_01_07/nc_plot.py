from netCDF4 import Dataset
import matplotlib.pyplot as plt

# Import netCDF file
ncfile = 'data/prob_01_07.nc'
data = Dataset(ncfile)
var = data.variables

# Use latex
plt.rc('text', usetex=True)
plt.rc('font', family='serif')

# Prepare Plot
plt.figure(figsize=(10,6), dpi=300)
plt.title(r"Hoeffding Bound for experiments", fontsize=16)
plt.xlabel(r'$\epsilon$', fontsize=14)
plt.ylabel(r'Probability', fontsize=14)

# Prepare Data to Plot
eps = var['epsilon'][:]
result = var['result'][:]
bound = var['bound'][:]

# Plot with Legends
plt.plot(eps, result, label=r'$P[\max|\nu - \mu|>\epsilon]$')
plt.plot(eps, bound, label=r'Hoeffding Bound')

# Other options
plt.legend(fontsize=12)
plt.grid()
plt.savefig("hoeffding.png", dpi=300)
