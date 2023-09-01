def find_pairs_with_sum(numbers, target_sum):
    num_set = set()  # To keep track of seen numbers
    result = []
    for num in numbers:
        complement = target_sum - num
        if complement in num_set:
            result.append((num, complement))
        num_set.add(num)
    return result
def main():
    import sys
    if len(sys.argv) < 3:
        print("Usage: python app.py <list_of_numbers> <target_sum>")
        return
    numbers = list(map(int, sys.argv[1].split(',')))
    target_sum = int(sys.argv[2])
    pairs = find_pairs_with_sum(numbers, target_sum)
    for pair in pairs:
        print("+", pair[0], ",", pair[1])
if __name__ == "__main__":
    main()