from itertools import product

from contract import ComputeOutput


def input_problem(v):
    if any(len(w) != 7 or any(c not in "01" for c in w) for w in v.codewords):
        return "seven binary digits required"
    return None


def expected(v):
    legal = []
    for d3, d5, d6, d7 in product(range(2), repeat=4):
        bits = [d3 ^ d5 ^ d7, d3 ^ d6 ^ d7, d3, d5 ^ d6 ^ d7, d5, d6, d7]
        legal.append(("".join(str(b) for b in bits), f"{d3}{d5}{d6}{d7}"))
    positions, corrected, payloads = [], [], []
    for word in v.codewords:
        for code, payload in legal:
            differences = [i for i in range(7) if word[i] != code[i]]
            if len(differences) <= 1:
                positions.append(differences[0] + 1 if differences else 0)
                corrected.append(code)
                payloads.append(payload)
                break
    return ComputeOutput(positions, positions, corrected, payloads)
