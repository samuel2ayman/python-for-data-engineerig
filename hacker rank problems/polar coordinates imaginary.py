import cmath 
inn=complex(input())
print(abs(complex(inn.real,inn.imag)))
print(cmath.phase(complex(inn.real,inn.imag)))