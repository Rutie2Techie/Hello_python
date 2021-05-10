## insert a element into the below list
A = [41, 45, 89, 82, 'dg', 'kjh', 'gfhgf', '45h', '4hk', 54]

print("List A : ", A)
print('len(A): ', len(A))

print("------------------------------")

## insert "mac book M1" before 'dg'  ??

A.insert(A.index('dg'),"mac book m1")
print(A)