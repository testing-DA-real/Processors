import math
import random
from typing import List, Tuple, Optional


def add(a: float, b: float) -> float:
    return a + b


def subtract(a: float, b: float) -> float:
    return a - b


def multiply(a: float, b: float) -> float:
    return a * b


def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Division by zero is not allowed")
    return a / b


def power(base: float, exp: float) -> float:
    return base ** exp


def sqrt(value: float) -> float:
    if value < 0:
        raise ValueError("Cannot compute square root of negative number")
    return math.sqrt(value)


def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def gcd(a: int, b: int) -> int:
    return math.gcd(a, b)


def lcm(a: int, b: int) -> int:
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // gcd(a, b)


def is_even(n: int) -> bool:
    return n % 2 == 0


def is_odd(n: int) -> bool:
    return n % 2 != 0


def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def fibonacci(n: int) -> List[int]:
    if n <= 0:
        return []
    if n == 1:
        return [0]
    seq = [0, 1]
    for i in range(2, n):
        seq.append(seq[i - 1] + seq[i - 2])
    return seq


def mean(values: List[float]) -> float:
    if not values:
        raise ValueError("Cannot compute mean of empty list")
    return sum(values) / len(values)


def median(values: List[float]) -> float:
    if not values:
        raise ValueError("Cannot compute median of empty list")
    sorted_vals = sorted(values)
    n = len(sorted_vals)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_vals[mid - 1] + sorted_vals[mid]) / 2
    return sorted_vals[mid]


def mode(values: List[float]) -> List[float]:
    if not values:
        raise ValueError("Cannot compute mode of empty list")
    freq = {}
    for v in values:
        freq[v] = freq.get(v, 0) + 1
    max_freq = max(freq.values())
    return [k for k, v in freq.items() if v == max_freq]


def variance(values: List[float]) -> float:
    if len(values) < 2:
        raise ValueError("Variance requires at least two values")
    m = mean(values)
    return sum((x - m) ** 2 for x in values) / (len(values) - 1)


def std_dev(values: List[float]) -> float:
    return math.sqrt(variance(values))


def clamp(value: float, low: float, high: float) -> float:
    return max(low, min(value, high))


def lerp(a: float, b: float, t: float) -> float:
    if t < 0 or t > 1:
        raise ValueError("Interpolation factor t must be between 0 and 1")
    return a + (b - a) * t


def map_range(value: float, in_low: float, in_high: float, out_low: float, out_high: float) -> float:
    if abs(in_high - in_low) < 1e-12:
        raise ValueError("Input range cannot be zero")
    ratio = (value - in_low) / (in_high - in_low)
    return out_low + ratio * (out_high - out_low)


def distance(x1: float, y1: float, x2: float, y2: float) -> float:
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def manhattan_distance(x1: float, y1: float, x2: float, y2: float) -> float:
    return abs(x2 - x1) + abs(y2 - y1)


def sigmoid(x: float) -> float:
    return 1 / (1 + math.exp(-x))


def softmax(values: List[float]) -> List[float]:
    exp_vals = [math.exp(v) for v in values]
    total = sum(exp_vals)
    return [v / total for v in exp_vals]


def random_matrix(rows: int, cols: int, low: float = 0.0, high: float = 1.0) -> List[List[float]]:
    return [[random.uniform(low, high) for _ in range(cols)] for _ in range(rows)]


def dot_product(a: List[float], b: List[float]) -> float:
    if len(a) != len(b):
        raise ValueError("Vectors must have same length")
    return sum(x * y for x, y in zip(a, b))


def matrix_multiply(a: List[List[float]], b: List[List[float]]) -> List[List[float]]:
    if not a or not b:
        raise ValueError("Matrices cannot be empty")
    if len(a[0]) != len(b):
        raise ValueError("Matrix dimensions incompatible")
    result = [[0.0 for _ in range(len(b[0]))] for _ in range(len(a))]
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                result[i][j] += a[i][k] * b[k][j]
    return result


def transpose(matrix: List[List[float]]) -> List[List[float]]:
    if not matrix:
        return []
    return [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))]


def is_power_of_two(n: int) -> bool:
    return n > 0 and (n & (n - 1)) == 0


def next_power_of_two(n: int) -> int:
    if n <= 0:
        return 1
    p = 1
    while p < n:
        p <<= 1
    return p


def binomial_coefficient(n: int, k: int) -> int:
    if k < 0 or k > n:
        return 0
    if k == 0 or k == n:
        return 1
    k = min(k, n - k)
    result = 1
    for i in range(1, k + 1):
        result = result * (n - i + 1) // i
    return result


def degrees_to_radians(degrees: float) -> float:
    return degrees * math.pi / 180


def radians_to_degrees(radians: float) -> float:
    return radians * 180 / math.pi


def normalize_angle(angle: float) -> float:
    return angle % 360


def circumferenece(radius: float) -> float:
    return 2 * math.pi * radius


def area_of_circle(radius: float) -> float:
    return math.pi * radius ** 2


def area_of_rectangle(length: float, width: float) -> float:
    return length * width


def area_of_triangle(base: float, height: float) -> float:
    return 0.5 * base * height


def distance_3d(x1: float, y1: float, z1: float, x2: float, y2: float, z2: float) -> float:
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)
