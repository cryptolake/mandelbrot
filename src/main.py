import math

WIDTH = 512
HEIGHT = 512
MAX_COLOR = 255
MAX_ITER = 200


def colorize(idx: int) -> (int, int, int):
    if idx == MAX_ITER:
        return (0, 0, 0)
    else:
        r = min(int(abs(idx**2)), MAX_COLOR)
        g = min(int(math.exp(idx)), MAX_COLOR)
        b = min(int(math.cosh(idx)), MAX_COLOR)
        return (r, g, b)


def mandelbrot(c: complex) -> int:
    f = 0
    for idx in range(MAX_ITER):
        f = f**2 + c
        if abs(f) >= 2:
            return idx
    return MAX_ITER


def pixel_to_plane(i: int, j: int) -> complex:
    k = 2.5
    xo, yo = -1, 0

    x = k * (i/WIDTH - 0.5) + xo
    y = k * (j/HEIGHT - 0.5) + yo
    return x + 1j*y


def main():
    header = f'P3 {WIDTH} {HEIGHT}\n{MAX_COLOR}'
    with open('mandelbrot.ppm', 'w') as f:
        f.write(header)
        for j in range(HEIGHT):
            for i in range(WIDTH):
                c = pixel_to_plane(i, j)
                r, g, b = colorize(mandelbrot(c))
                f.write(f' {r} {g} {b}\n')


if __name__ == '__main__':
    main()
