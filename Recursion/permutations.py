arr = "abcdef"

def permutations(arr):
    results = []
    arr = [0 for i in range(len(arr))]
    def backtrack(path,arr):
        