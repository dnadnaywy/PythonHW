# Write a function that will order a list of string tuples based on the 3rd character of the
# 2nd element in the tuple. Example: ('abc', 'bcd'), ('abc', 'zza')] ==> [('abc', 'zza'), ('abc', 'bcd')]

def order(tuples: list) -> list:
    tuples.sort(key=lambda x: x[1][2])
    return tuples

print(order([('abc', 'bcd'), ('abc', 'zza'), ('abc', 'zzb')]))