import math

def velocity(distance, time):
    return distance / time


def acceleration(v_initial, v_final, time):
    return (v_final - v_initial) / time

print("Second Law")
def force(mass, acceleration):
    return mass * acceleration

def kinetic_energy(mass, velocity):
    return 0.5 * mass * velocity ** 2

def gravitational_force(m1, m2, r):
    G = 6.674 * 10**-11
    return (G * m1 * m2) / r**2




v = velocity(100, 10)
a = acceleration(0, 20, 5)
f = force(10, a)
ke = kinetic_energy(5, v)
gf = gravitational_force(10, 20, 2)

print("Velocity:", v, "m/s")
print("Acceleration:", a, "m/s²")
print("Force:", f, "N")
print("Kinetic Energy:", ke, "J")
print("Gravitational Force:", gf, "N")