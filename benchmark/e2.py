
def multiple(r, numbers):

    def _(x):
        for n in numbers:
            if x%n == 0:
                return True
        return False

    return sum(filter(_, range(1, r)))

print multiple(1000000, [3, 5])
