from playLA.Vector import Vector

if __name__ == '__main__':
    vec=Vector([5,2])
    print(vec)
    print(len(vec))
    print("vec[0]={},vec[1]={}".format(vec[0],vec[1]))
    vec2=Vector([3,1])
    print("{}+{}={}".format(vec, vec2,vec+vec2))
    xy=zip([5,3],[1,2])
    # print(list(xy))
    # for a,b in xy:
    #     print(a,b)
    #     print(a+b)
    zero2=Vector.zero(2)
    print(zero2)
    print("{}+{}={}".format(vec, zero2, vec + zero2))






