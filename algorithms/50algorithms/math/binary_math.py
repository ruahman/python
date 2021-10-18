"""Add binarry numbers."""


def add_binary_numbers(a: str, b: str) -> str:
    """Add binary numbers."""
    result = []
    carry = 0
    i, j = len(a)-1, len(b)-1
    while i >= 0 or j >= 0 or carry:
        total = carry

        if i >= 0:
            total += int(a[i])
            i -= 1
        if j >= 0:
            total += int(a[j])
            j -= 1

        result.append(str(total % 2))
        carry = total // 2

    return ''.join(reversed(result))


res = add_binary_numbers("110", "010")
print(f"binarry: {res}")
