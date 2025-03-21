def gen_parenthesis(s, n, open, close, res):
    if open == close == n:
        res.append(s)
        return
    if open < n:
        gen_parenthesis(s+"(", n, open+1, close, res)
    if close < open:
        gen_parenthesis(s+")", n, open, close+1, res)


res = []
gen_parenthesis("", 3, 0, 0, res)
print(res)
