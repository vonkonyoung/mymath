class Vector:
    def __init__(self,lst):
        self._values=lst

    def __getitem__(self, index):
        return self._values[index]

    @classmethod
    def  zero(cls,dim):
        return cls([0]*dim)

    def __add__(self, other):
        """向量加法，返回结果向量"""
        assert len(self)==len(other),\
        "Error in adding.Length of vectors must be same"
        """啥意思？"""
        return Vector([a+b for a,b in zip(self,other)])

    def __sub__(self, other):
        assert len(self)==len(other),"Error in adding.Length of vectors must be same"
        return Vector([a-b for a,b in zip(self,other)])

    def __mul__(self, k):
        return Vector([k*e for e in self])

    def __rmul__(self, k):
        return self*k


    def __len__(self):
        """返回向量的维度(有多少个元素)"""
        return len(self._values)

    def __repr__(self):
        return "Vector({})".format(self._values)

    def __str__(self):
        return "({})".format(",".join(str(e) for e in self._values))