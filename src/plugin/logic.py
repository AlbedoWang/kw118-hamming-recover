from contract import ComputeOutput


def compute(v, workspace):
    if any(len(w) != 7 or set(w) - set("01") for w in v.codewords):
        raise ValueError("each codeword must contain seven binary digits")
    syndromes, positions, corrected, payloads = [], [], [], []
    for word in v.codewords:
        bits = [int(b) for b in word]
        syndrome = 0
        for i, bit in enumerate(bits, 1):
            if bit:
                syndrome ^= i
        if syndrome:
            bits[syndrome - 1] ^= 1
        syndromes.append(syndrome)
        positions.append(syndrome)
        corrected.append("".join(str(b) for b in bits))
        payloads.append("".join(str(bits[i]) for i in [2, 4, 5, 6]))
    return ComputeOutput(syndromes, positions, corrected, payloads)
