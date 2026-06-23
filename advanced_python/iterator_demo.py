class InternIDGenerator:

    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):
        value = f"TES{self.num:03d}"
        self.num += 1
        return value


obj = InternIDGenerator()

for i in range(5):
    print(next(obj))