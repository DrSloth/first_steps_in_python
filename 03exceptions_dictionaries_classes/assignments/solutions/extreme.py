class IndexMap:
    def __init__(self):
        self.indices = {}
        self.values = []

    def insert(self,k,v):
        self.indices[k] = len(self.values)
        self.values.append(v)

    def get_by_index(self, idx):
        return self.values[idx]

    def get(self, k):
        return self.get_by_index(self.get_index(k))

    def get_index(self, k):
        return self.indices[k]

# Test:
idm = IndexMap()
idm.insert(1, "abc")
idm.insert("hello", "world")

print(idm.get_index(1))
print(idm.get_index("hello"))

print(idm.get(1))
print(idm.get("hello"))

print(idm.get_by_index(0))
print(idm.get_by_index(1))
