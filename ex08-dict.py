# %%

connection = dict(
    port=3306,
    host='localhost',
    db='northwind',
    is_admin=True,
    x=[12,14,56,78]
)

connection
# %%
connection['port']
# %%
connection2 = ['localhost', 'northwind', 3306, True]

# %%

user = {
    'first_name':'Anna',
    'last_name':'Smith',
    'age':30,
    'email':'anna@no.com'
}

user['last_name']
# %%
user.keys()

# %%
user.values()

# %%
user.items()
# %%

user['phone']
# %%

'phone' in user

# %%
user.get('phone','000-00-00')
# %%
