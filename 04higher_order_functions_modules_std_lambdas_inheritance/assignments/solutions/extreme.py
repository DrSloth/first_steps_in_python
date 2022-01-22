def super_list(l):
    return {"list": l}


def list_mapper(l):
    me = super_list(l)
    def map(f):
        d = {}
        for i in me["list"]:
            d[i] = f(i)
        return d

    me["map"] = map
    return me

# Test
mapper = list_mapper([1,2,3,4,5])
print(mapper["map"](lambda x: x**2))
