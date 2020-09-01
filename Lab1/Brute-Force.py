import time
def searchIndex(S, T):
    s, t, pos, loop = 0, 0, 0, 0
    S_len = len(S)
    T_len = len(T)
    while (s < S_len and t < T_len):
        loop = loop + 1
        if S[s] == T[t]:
            s += 1
            t += 1
        else:
            pos += 1
            s = pos
            t = 0

    if t == T_len:
        return pos, loop
    else:
        return -1, loop
content = ""
with open('./Testing/GCF_000006645.1_ASM664v1_genomic.fna', 'r') as fna:
    content = fna.read()

# s = input("Enter the main string: ")
# t = input("Enter the substring: ")
# testingStr = "AACACACATGTCTATGAGTGTGAAATG"
testingStr = "AAAAAAAAAAAAAAAAAAAAAA"
tic = time.perf_counter()
result = searchIndex(content, testingStr)
toc = time.perf_counter()
print(f"Time spent {toc - tic} seconds")
print(f"Loop times: {result[1]} pos: {result[0]}")
