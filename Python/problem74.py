from math import factorial as fact

def fact_sum(num): return sum([fact(int(digit)) for digit in str(num)])

def fact_chain_count(num):
    traversed = set([num]); new_num = num
    while True:
        new_num = fact_sum(new_num)
        if new_num in traversed:
            return len(traversed)
        traversed.add(new_num)

def test():
    # Test cases from the description
    assert(fact_sum(145) == 145)
    assert(fact_chain_count(69) == 5)

if __name__ == "__main__":
    print([fact_chain_count(num) for num in range(1, int(1e6))].count(60))
