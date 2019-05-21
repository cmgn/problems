from collections import defaultdict

n = int(input())

for i in range(n):
    street_name = input()
    address_line = input()
    num_addresses = int(address_line.split()[0])
    addresses = []
    while len(addresses) != num_addresses:
        line = input()
        if line[0] != "+":
            addresses.append(line)
        else:
            start, stop, step = map(int, line.split()[1:])
            addresses.extend(str(x) for x in range(start, stop + 1, step))
    counts = defaultdict(int)
    for address in addresses:
        for digit in address:
            counts[digit] += 1
    number_of_digits = sum(counts.values())
    print(street_name)
    print(address_line)
    for digit in "0123456789":
        print("Make", counts[digit], "digit", digit)
    if number_of_digits != 1:
        print("In total", number_of_digits, "digits")
    else:
        print("In total 1 digit")
