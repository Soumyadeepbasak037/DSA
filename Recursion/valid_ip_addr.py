# addr = list("101023")
addr = "25525511135"
# gen_ip(addr)

def gen_ip(addr):
    res = []
    def backtrack(indx,path):
        if(indx == len(addr) and len(path) == 4):
            res.append(path[:])
            return
        if(len(path)>4):
            return
        for i in range(indx+1,len(addr)+1):
            if(int(addr[indx:i])>=0 and int(addr[indx:i])<=255):
                if(len(addr[indx:i]) > 1 and (addr[indx:i])[0]=="0"):
                    continue
                path.append(addr[indx:i])
                backtrack(i,path)
                path.pop()
    backtrack(0,[])
    ans = []
    for ip in res:
        ans.append(".".join(ip))
    print(ans)

gen_ip(addr)