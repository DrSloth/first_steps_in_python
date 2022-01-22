import super_list

class ListMapper(super_list.SuperList):
    def map(self,f):
        d = {}
        for i in self.list:
            d[i] = f(i)
        return d

# Test
l = ListMapper([1,2,3,4,5])
print(l.map(lambda x: x**2))
