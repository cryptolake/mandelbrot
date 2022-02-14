import math
WIDTH = 512
HEIGHT = 512
MAX_COLOR = 255

HEADER = f'P3 {WIDTH} {HEIGHT}\n{MAX_COLOR}'


MAX_ITER = 200


def mandelbrot(c: complex) -> (int, int, int):
    f = 0
    idx = 0
    for idx in range(MAX_ITER):
        f = f**2 + c
        if abs(f) >= 2:
            r = min(int(abs(idx**2)), MAX_COLOR)
            g = min(int(math.exp(idx)), MAX_COLOR)
#            b = min(int(math.cosh(idx)), MAX_COLOR)
            b = 0
            return (r, g, b)
    return (0, 0, 0)


def main():
    with open('mandelbrot.ppm', 'w') as f:
        f.write(HEADER)
        for j in range(HEIGHT):
            for i in range(WIDTH):
                c = 2*(i/(WIDTH) - 0.5) + 2*1j*(j/(HEIGHT) - 0.5)
                r, g, b = mandelbrot(c)
                f.write(f' {r} {g} {b}\n')


if __name__ == '__main__':
    main()
