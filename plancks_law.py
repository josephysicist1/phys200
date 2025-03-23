import math
import matplotlib.pyplot as plt

h = 6.62607015e-34  
c = 3.0e8           
k_B = 1.380649e-23  

def func_planck(wavelength, temperature):         # Calculating the spectral radiance of a black body at a given wavelength and temperature using Planck's Law.

    numerator = 2 * h * c**2
    exponent = (h * c) / (wavelength * k_B * temperature)
    
    # Making correction for large exponent values 
    if exponent > 700:
        return 0.0                                # When exponent is too large, the spectral radiance is close to 0 
    
    denominator = (wavelength**5) * (math.exp(exponent) - 1)
    return numerator / denominator

def simpson_integrate(f, a, b, N):
    
    # Calculating Simpson integration with boundaries a,b and with the N intervals 
    
    if N % 2 == 1:                                #It gives an error about intervals of Simpson integral
        raise ValueError("N must be an even number.")
    
    h = (b - a) / N
    x = [a + i*h for i in range(N + 1)]
    y = [f(xi) for xi in x]
    S = y[0] + y[-1]
    for i in range(1, N, 2):
        S += 4 * y[i]
    for i in range(2, N, 2):
        S += 2 * y[i]
        
    return S * h / 3

# Definition of parameters
temperature = 5000                                                    # in Kelvin
wavelengths = [1e-9 + i * (3e-6 - 1e-9) / 1000 for i in range(1001)]  # I've chosen wavelength range from 1 nm to 3 micrometers by creating a thousand of sample

# Calculating the Planck function for the wavelengths we've decided 
radiance = [func_planck(w, temperature) for w in wavelengths]

wave_nano = [w * 1e9 for w in wavelengths]                            # Converting wavelength to nanometers
plt.plot(wave_nano, radiance)                    
plt.xlabel("Wavelength (nm)")
plt.ylabel("Spectral Radiance")
plt.title(f"Black Body Radiation at T={temperature} K")
plt.grid(True)
plt.show()

# Calculating the area under the curve using Simpson's rule
area = simpson_integrate(lambda x: func_planck(x, temperature), wavelengths[0], wavelengths[-1], 1000)
area_exact = float("{:.4f}".format(area))
print(f"The area under the distribution is: {area:.4e} W/m^2")
print(f"The area under the distribution is: {area_exact} W/m^2")