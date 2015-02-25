__author__ = 'Frank'
def permutations(word):
    if len(word) == 1:
        return [word]
    #get all permutations of length N-1
    p_results=permutations(word[1:])
    char = word[0]
    result = []
    #iterate over all permutations of length N-1
    for p in p_results:
        #insert the character into every possible location
            for i in range(len(p) + 1):
                result.append(p[:i] + char + p[i:])
    return result