#!/usr/bin/env python3
"""Урок 2: логические выражения и побитовые операции."""

from itertools import product


def expressions(a: bool, b: bool, c: bool) -> tuple[bool, bool, bool]:
    return (
        not (a and b) or not (a or c),
        (a and b) or (not b and c),
        (a and b) or not c,
    )


print(" A B C | 1 2 3")
print("-------+------")
for a, b, c in product((False, True), repeat=3):
    first, second, third = expressions(a, b, c)
    assert first == (not a or not b)
    assert second == ((a or not b) and (b or c))
    assert third == (not c or (a and b))
    print(f" {int(a)} {int(b)} {int(c)} | {int(first)} {int(second)} {int(third)}")

x, y = 13, 6
mask = 0xff
print("\nПобитовые операции (8 младших битов):")
print(f"x       = {x:3} = {x:08b}")
print(f"y       = {y:3} = {y:08b}")
for label, value in (
    ("x & y", x & y),
    ("x | y", x | y),
    ("x ^ y", x ^ y),
    ("~x & 0xff", (~x) & mask),
    ("x << 1", x << 1),
    ("x >> 1", x >> 1),
):
    print(f"{label:9} = {value:3} = {value:08b}")

print(f"\nБез маски ~x = {~x}")
eight_bit_negative = ((~x & mask) ^ 0x80) - 0x80
assert eight_bit_negative == ~x
print(f"Восьмибитное 11110010₂ в дополнительном коде = {eight_bit_negative}")
