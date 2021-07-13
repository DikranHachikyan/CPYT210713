# %%
a = 5
b = 5

id(a) == id(b)

# %%

class Point:
    def __init__(self, x):
        self.x = x

# %%
p1 = Point(x = 10)
p2 = Point(x = 10)

id(p1) == id(p2)
# %%
print(f'id1={id(p1)} id2={id(p2)}')
# %%
