def answer(n):
    n = int(n)
    steps = []

    def recursive_transform(n, steps):
        if n == 1:
            steps.append(1)
            return 0  # No more operations needed when n is 1

        steps.append(n)

        if n % 2 == 0:
            return 1 + recursive_transform(n // 2, steps)
        else:
            add_steps = []
            remove_steps = []

            add_count = 1 + recursive_transform(n + 1, add_steps)
            remove_count = 1 + recursive_transform(n - 1, remove_steps)

            if add_count <= remove_count:
                steps.extend(add_steps)
                return add_count
            else:
                steps.extend(remove_steps)
                return remove_count

    recursive_transform(n, steps)
    return steps


def validate_answer(n, provided_steps):
    calculated_steps = answer(n)
    return "Yes" if calculated_steps == provided_steps else "No"


# Test with n = 15
n = "15"
result = answer(n)
print(result)  # Output the sequence of steps

# Expected steps for adding 1 first
provided_steps_add = [15, 16, 8, 4, 2, 1]
print(validate_answer(n, provided_steps_add))  # Should print "Yes"

# Expected steps for subtracting 1 first
provided_steps_subtract = [15, 14, 7, 8, 4, 2, 1]
print(validate_answer(n, provided_steps_subtract))  # Should print "Yes"
