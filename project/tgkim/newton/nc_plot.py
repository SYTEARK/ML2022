from netCDF4 import Dataset
import matplotlib.pyplot as plt

# Use latex
plt.rc('text', usetex=True)
plt.rc('font', family='serif')

# ==============================================================================
# Free Fall
# ==============================================================================
# Import netCDF file
ncfile = './data/free_fall.nc'
data = Dataset(ncfile)
var = data.variables

# Prepare Data to Plot
t = var['t'][:]
s = var['s'][:]  
v = var['v'][:]

# Prepare Plot
plt.figure(figsize=(10,6), dpi=300)
plt.title(r"Free Fall", fontsize=16)
plt.xlabel(r'$t$', fontsize=14)
plt.ylabel(r'$s$', fontsize=14)


# Plot with Legends
plt.plot(t, s, label=r'Position')

# Other options
plt.legend(fontsize=12)
plt.grid()
plt.savefig("fig/freefall_position.png", dpi=300)

# ==============================================================================
# Free Fall - Velocity
# ==============================================================================
# Prepare Plot
plt.figure(figsize=(10,6), dpi=300)
plt.title(r"Free Fall", fontsize=16)
plt.xlabel(r'$t$', fontsize=14)
plt.ylabel(r'$v$', fontsize=14)

# Plot with Legends
plt.plot(t, v, label=r'Velocity')

# Other options
plt.legend(fontsize=12)
plt.grid()
plt.savefig("fig/freefall_velocity.png", dpi=300)

# ==============================================================================
# Drag Fall
# ==============================================================================
# Import netCDF file
ncfile = './data/drag_fall.nc'
data = Dataset(ncfile)
var = data.variables

# Prepare Data to Plot
t = var['t'][:]
s = var['s'][:]  
v = var['v'][:]

# Prepare Plot
plt.figure(figsize=(10,6), dpi=300)
plt.title(r"Falling with Air Drag", fontsize=16)
plt.xlabel(r'$t$', fontsize=14)
plt.ylabel(r'$s$', fontsize=14)


# Plot with Legends
plt.plot(t, s, label=r'Position')

# Other options
plt.legend(fontsize=12)
plt.grid()
plt.savefig("fig/dragfall_position.png", dpi=300)

# ==============================================================================
# Free Fall - Velocity
# ==============================================================================
# Prepare Plot
plt.figure(figsize=(10,6), dpi=300)
plt.title(r"Falling with Air Drag", fontsize=16)
plt.xlabel(r'$t$', fontsize=14)
plt.ylabel(r'$v$', fontsize=14)

# Plot with Legends
plt.plot(t, v, label=r'Velocity')

# Other options
plt.legend(fontsize=12)
plt.grid()
plt.savefig("fig/dragfall_velocity.png", dpi=300)

# ==============================================================================
# SHO
# ==============================================================================
# Import netCDF file
ncfile = './data/sho.nc'
data = Dataset(ncfile)
var = data.variables

# Prepare Data to Plot
t = var['t'][:]
s = var['s'][:]  
v = var['v'][:]

# Prepare Plot
plt.figure(figsize=(10,6), dpi=300)
plt.title(r"Simple Harmonic Oscillator", fontsize=16)
plt.xlabel(r'$t$', fontsize=14)
plt.ylabel(r'$s$', fontsize=14)


# Plot with Legends
plt.plot(t, s, label=r'Position')

# Other options
plt.legend(fontsize=12)
plt.grid()
plt.savefig("fig/sho_position.png", dpi=300)

# ==============================================================================
# SHO - Velocity
# ==============================================================================
# Prepare Plot
plt.figure(figsize=(10,6), dpi=300)
plt.title(r"Simple Harmonic Oscillator", fontsize=16)
plt.xlabel(r'$t$', fontsize=14)
plt.ylabel(r'$v$', fontsize=14)

# Plot with Legends
plt.plot(t, v, label=r'Velocity')

# Other options
plt.legend(fontsize=12)
plt.grid()
plt.savefig("fig/sho_velocity.png", dpi=300)

# ==============================================================================
# SHO with Friction
# ==============================================================================
# Import netCDF file
ncfile = './data/sho_friction.nc'
data = Dataset(ncfile)
var = data.variables

# Prepare Data to Plot
t = var['t'][:]
s = var['s'][:]  
v = var['v'][:]

# Prepare Plot
plt.figure(figsize=(10,6), dpi=300)
plt.title(r"Simple Harmonic Oscillator with Friction", fontsize=16)
plt.xlabel(r'$t$', fontsize=14)
plt.ylabel(r'$s$', fontsize=14)


# Plot with Legends
plt.plot(t, s, label=r'Position')

# Other options
plt.legend(fontsize=12)
plt.grid()
plt.savefig("fig/shofriction_position.png", dpi=300)

# ==============================================================================
# SHO with Friction - Velocity
# ==============================================================================
# Prepare Plot
plt.figure(figsize=(10,6), dpi=300)
plt.title(r"Simple Harmonic Oscillator with Friction", fontsize=16)
plt.xlabel(r'$t$', fontsize=14)
plt.ylabel(r'$v$', fontsize=14)

# Plot with Legends
plt.plot(t, v, label=r'Velocity')

# Other options
plt.legend(fontsize=12)
plt.grid()
plt.savefig("fig/shofriction_velocity.png", dpi=300)

# ==============================================================================
# SHO with Friction (GL4)
# ==============================================================================
# Import netCDF file
ncfile = './data/sho_friction_gl4.nc'
data = Dataset(ncfile)
var = data.variables

# Prepare Data to Plot
t = var['t'][:]
s = var['s'][:]  
v = var['v'][:]

# Prepare Plot
plt.figure(figsize=(10,6), dpi=300)
plt.title(r"Simple Harmonic Oscillator with Friction", fontsize=16)
plt.xlabel(r'$t$', fontsize=14)
plt.ylabel(r'$s$', fontsize=14)


# Plot with Legends
plt.plot(t, s, label=r'Position')

# Other options
plt.legend(fontsize=12)
plt.grid()
plt.savefig("fig/shofriction_gl4_position.png", dpi=300)

# ==============================================================================
# SHO with Friction - Velocity (GL4)
# ==============================================================================
# Prepare Plot
plt.figure(figsize=(10,6), dpi=300)
plt.title(r"Simple Harmonic Oscillator with Friction", fontsize=16)
plt.xlabel(r'$t$', fontsize=14)
plt.ylabel(r'$v$', fontsize=14)

# Plot with Legends
plt.plot(t, v, label=r'Velocity')

# Other options
plt.legend(fontsize=12)
plt.grid()
plt.savefig("fig/shofriction_gl4_velocity.png", dpi=300)
