
def override1(a):
    print(a)

def override1(a,c):
    print(a,c)

if __name__=="__main__":
    override1(34,23)
    override1(23)# so python dpoesnt support overriding but can be mad eby 