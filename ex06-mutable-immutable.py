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
p1.x = 100

print(f'id1={id(p1)}')
# %%
p1.x = 10

print(f'id x 1:{id(p1.x)} id x 2:{id(p2.x)}')


# %%
s1 = 'hello' * 1000
s2 = 'hello' * 1000


id(s1) == id(s2)

# %%
