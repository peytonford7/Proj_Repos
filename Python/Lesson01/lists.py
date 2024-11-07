# Lists

users = ['Peyton']
print(users)

users.append('Kamryn')
print(users)

users += ['Jackie']
print(users)

users.extend(['Jessica', 'Lindsey'])
print(users)

users.insert(1, 'Victoria')
print(users)

# Insert without deletion
users[2:2] = ['Jenna', 'Sophia']

# Insert with deletion
users[1:3] = ['Sophie', 'Avery']
print(users)

del users[1]
print(users)

users.sort()
print(users)

print("\n")

# Nums list

nums = [9, 90, 1, 2, 3, 6, 23]
print(nums)

nums.reverse()
print(nums)

nums.sort()
print(nums)

print(sorted(nums, reverse=True))

# Copy nums list
numscopy = nums.copy()
mynums = list(nums)
mycopy = nums[:]

print(numscopy)
print(mynums)
print(mycopy)

print(type(nums))

# Tuples

mytuple = tuple(('Peyton', 23, True))

anothertuple = (1, 4, 2, 8)

print(mytuple)
print(type(mytuple))
print(type(anothertuple))

# Change tuple
newlist = list(mytuple)
newlist.append('Kam')
newtuple = tuple(newlist)
print(newtuple)
print(type(newtuple))

# hey stores remaining values
(one, two, *hey) = anothertuple
print(one)
print(two)
print(hey)

# two stores middle values
(one, *two, hey) = anothertuple
print(one)
print(two)
print(hey)

print(anothertuple.count(2))
