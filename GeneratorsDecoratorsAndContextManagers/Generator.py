
def __init__(self,start,end):
        self.value = start
        self.end = end

def __iter__(self):
        return self

def __next__(self):
        if self.value >= self.end:
            raise StopIteration

        current = self.value
        self.value += 1
        return current

def my_generator(start, end):
    current = start
    while current < end:
        yield current
        current +=1

nums = my_generator(1,10)

for num in nums:
    print(num)

