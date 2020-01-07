import sys
from collections import namedtuple
from itertools import combinations, chain

sys.setrecursionlimit(100000)

Particle = namedtuple('Particle', 'position velocity acceleration')
Vector = namedtuple('Vector', 'x y z')

def parse_vector(vector_string):
    parts = [int(x) for x in vector_string.split(',')]
    return Vector(parts[0], parts[1], parts[2])

# Changed the format from the original as it was so hard to parse...
def parse_particle(particle_string):
    vectors = [parse_vector(x) for x in particle_string.split(';')]
    return Particle(vectors[0], vectors[1], vectors[2])

particles = [parse_particle(x.rstrip()) for x in open('input', 'r').readlines()]
total_acceleration = lambda p: abs(p.acceleration.x) + abs(p.acceleration.y) + abs(p.acceleration.z)
total_accelerations = [total_acceleration(p) for p in particles]
closest_particle = total_accelerations.index(min(total_accelerations))

print("Closest particle in the long run is particle {}".format(closest_particle))

def update(particle):
    p = particle.position
    v = particle.velocity
    a = particle.acceleration
    new_velocity = Vector(v.x + a.x, v.y + a.y, v.z + a.z)
    new_position = Vector(p.x + new_velocity.x, p.y + new_velocity.y, p.z + new_velocity.z)
    return Particle(new_position, new_velocity, a)

def remove_collided(particles):
    pairs = combinations(particles, 2)
    collided_pairs = [x for x in pairs if x[0].position == x[1].position]
    collided_particles = set(chain.from_iterable(collided_pairs))
    return [x for x in particles if x not in collided_particles]

def simulate(particles, t):
    # Just a guess, no fancy stopping condition for me this time...
    if t > 50:
        return particles

    particles = remove_collided(particles) 
    particles = [update(p) for p in particles]
    return simulate(particles, t + 1)

final_particles = simulate(particles, 0)

print("There was {} uncollided particles left zooming".format(len(final_particles)))
