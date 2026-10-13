"""Illustrative 0D Wright coherence model; NOT a gravitational simulation."""
import math


def simulate(alpha=0.0, gamma=0.6, beta=0.2, dt=0.01, steps=1000, c0=0.0):
    """Euler integrate dC/dt=-gamma*C+alpha*I(t)-beta*C**3.

    I(t) is an arbitrary normalized periodic driver, not measured EM/GR data.
    """
    if dt <= 0 or steps < 1 or gamma < 0 or beta < 0:
        raise ValueError('invalid integration parameters')
    c = c0
    rows = []
    for i in range(steps + 1):
        t = i * dt
        driver = math.sin(2 * math.pi * 0.2 * t)
        rows.append((t, c, driver))
        if i < steps:
            c += dt * (-gamma*c + alpha*driver - beta*c**3)
    return rows


def fieldspace_counts():
    from itertools import combinations
    sectors = 'E M S F W T I R H P A'.split()
    triples = list(combinations(sectors, 3))
    return len(triples), sum('E' in x for x in triples), sum('E' in x and 'M' in x for x in triples)


if __name__ == '__main__':
    print('FieldSpace full / E / E+M:', fieldspace_counts())
    for label, a in [('no drive', 0.0), ('driven', 0.7)]:
        data = simulate(alpha=a)
        print(f'{label}: final C={data[-1][1]:.6f}; peak |C|={max(abs(x[1]) for x in data):.6f}')
