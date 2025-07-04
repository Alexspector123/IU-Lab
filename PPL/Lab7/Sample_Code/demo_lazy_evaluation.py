def lazy_multiply(x, y):
    print("Multiplying now...")
    return x * y

def lazy_add(x, y):
    print("Adding now...")
    return x + y

def lazy_eval():
    print("Setting up lazy evaluation...")

    def generator():
        result1 = lazy_multiply(5, 3)  # Not evaluated yet
        result2 = lazy_add(result1, 4)  # Also delayed
        yield result2

    return generator()

# Nothing is computed yet!
lazy_result = lazy_eval()

# Now force evaluation
print("Accessing value:")
print(next(lazy_result))
