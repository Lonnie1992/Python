# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line


def greet(name, template='Hello, <name>!'):
    greet = template.replace('<name>', name)
    return greet


print(greet('bob', 'whats up'))


def force(mass, body='earth'):
    bodies = {
        'sun': 274,
        'jupiter': round(25, 1),
        'neptune': round(11.15, 1),
        'saturn': round(10.44, 1),
        'earth': round(9.798, 1),
        'uranus': round(8.87, 1),
        'venus': round(8.87, 1),
        'mars': round(3.71, 1),
        'mercury': round(3.7, 1),
        'moon': round(1.62, 1),
        'pluto': round(0.58, 1)
    }
    force = mass * bodies[body]
    return force


print(force(1, 'moon'))


def pull(m1, m2, d):
    g = 6.674 * 10 ** -11
    pull = g * ((m1 * m2) / d**2)
    return pull


print(pull(800, 1500, 3))
