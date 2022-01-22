class DictCreator:
    def __init__(self, keys):
        self.keys = keys

    def make_dict(self, values):
        if len(values) != len(self.keys):
            e = "len(values) != len(keys) (" + str(len(values)) + " != " + str(len(self.keys)) +")"
            raise Exception(e)
        
        d = {}
        for i in range(0, len(values)):
            d[self.keys[i]] = values[i]
        return d


# Test:
dc = DictCreator(["hello", 4, True])
di = dc.make_dict(["world", 2, False])

print(di)

dc.make_dict([2])
