class BiMap:
    def __init__(self):
        self.kv = {}
        self.vk = {}

    def insert(self, k, v):
        self.kv[k] = v
        self.vk[v] = k

    def get(self,k):
        return self.kv[k]

    def get_key(self,v):
        return self.vk[v]

# Test:
b = BiMap()
b.insert("a", 10)
b.insert(20, "b")
print(b.get("a"))
print(b.get(20))
print(b.get_key(10))
print(b.get_key("b"))
