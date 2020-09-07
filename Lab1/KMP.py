class KmpMatcher(object):
    def __init__(self, pattern, string):
        self._pattern = pattern.upper()
        self._string = string.upper()
        self._prefix = []
        self._validChar = ['A', 'T', 'G', 'C', 'N']

    #Matches the motif pattern against itself.
    def computePrefix(self):
        #Initialize prefix array
        self.__fillPrefixList()
        k = 0

        for pos in range(1, len(self._pattern)):
            #Check valid nt
            if(self._pattern[pos] not in self._validChar):
                print("Error: pattern contains invalid DNA nucleotides")
                exit()
            #Unique base in pattern
            while(k > 0 and self._pattern[k] != self._pattern[pos]):
                k = self.prefix[k]
            #repeat in pattern
            if(self._pattern[k] == self._pattern[pos]):
                k += 1
            self._prefix[pos] = k
        print(self._prefix)
    #Initialize the prefix list and set first element to -1 and all the rest of elements are 0
    def __fillPrefixList(self):
        self._prefix = [0] * (len(self._pattern))

    #An implementation of the Knuth-Morris-Pratt algorithm for linear time string matching
    def kmpSearch(self):
        #Compute prefix array
        self.computePrefix()
        #Number of characters matched
        match = 0
        position=[]
        found = False

        for pos in range(0, len(self._string)):
            #Check valid nt
            if(self._string[pos] not in self._validChar):
                print("Error: string contains invalid DNA nucleotides")
                exit()

            #Next character is not a match
            while(match > 0 and self._pattern[match] != self._string[pos]):
                match = self._prefix[match-1]
            #A character match has been found
            if(self._pattern[match] == self._string[pos]):
                match += 1
            #Pattern found
            if(match == len(self._pattern)):
                #print("Match found at position: " + str(pos-match+2))
                position.append(pos-match+2)
                             
                found = True
                match = self._prefix[match-1]
        print("Match found at position: ")        
        print(' '.join(map(str, position)))
        if(found == False):
            print("Sorry '" + self._pattern + "'" + " was not found ")


s = "ACTACTACTACTACTACT"
p = "aa"

matcher = KmpMatcher(p,s)
matcher.computePrefix()
#matcher.kmpSearch()

"""
computePrefix(self):
    Args:
    self._pattern : pattern to build

    computePrefix = [0, 0]
    if self._prefix[pos] not in self._validChar
	exit()
    for pos=1, k=0;pos < len(self._pattern);++pos:----------------------pos, k: positions to KmpSearch
        while k > 0 and self._pattern[k] != self._pattern[pos]: ---------------fail then jump until a match or k == 0
        k = next[k]
        if p[pos] == p[k]: ++k
        self._prefix.append(k)
    return self._prefix



KmpSearch(s):

Args:
	self._string= s :input string 
	self._pattern[]= p :pattern to search 
	pos : position of s


position=[]--------------------------------------------------matched index             
next=computePrefix(p)-------------------------------------------build next table

for pos=0,match=0;pos<len(self._string);++pos:------------------------------------pos,match: position of s and p respectively
    while match>0 and s[pos] !=p[match]:-----------------------------fail then jump until a match or pos==0
        match=next[match]
    if s[pos]==p[match]:-----------------------------------------match then check next pair(match++,pos++)
        ++match
    if match==len(p):------------------------------------------find a full match 
        position.append(pos-match+2) -----------------------------------get ans lsit
        match=next[match-1]---------------------------------------------jump as it failed


"""

