import random

random_set={random.randint (1,100) for _ in range(10)}

subset_even={num for num in random_set if num%2==0}

print(subset_even)