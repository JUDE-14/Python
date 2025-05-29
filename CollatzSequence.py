print('Name: Jude Andrew \nUSN: 1AY24AI049 \nSection: M\n ')

def collatz_sequence(n):
    """Generates the Collatz sequence starting from n."""
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence

start_number = 12
result = collatz_sequence(start_number)
print(result)
