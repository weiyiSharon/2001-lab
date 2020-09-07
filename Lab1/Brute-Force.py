class BFMatcher(object):
    def __init__(self, pattern, string):
        self._pattern = pattern.upper()
        self._string = string.upper()
        self._validChar = ['A', 'T', 'G', 'C', 'N']
        for char in self._pattern:
            if(char not in self._validChar):
                print("Error: pattern contains invalid DNA nucleotides")
                exit()
    #An implementation of the Knuth-Morris-Pratt algorithm for linear time string matching
    def bfSearch(self):
        found = False
        for pos in range(0, len(self._string)):
            s_ptr = pos
            p_ptr = 0
            while p_ptr < len(self._pattern):
                if(self._string[s_ptr] == self._pattern[p_ptr]):
                    s_ptr += 1
                    p_ptr += 1
                else:
                    break
                if p_ptr == len(self._pattern):
                    print("Match found at position: " + str(pos+1))
        
            

content = ""
with open('./Testing/GCF_000006645.1_ASM664v1_genomic.fna', 'r') as fna:
    content = fna.read()

testingStr = "ACCCCT"
matcher = BFMatcher(testingStr , content)
matcher.bfSearch()

