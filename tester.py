# tester.py
import random
from week10AKA11 import bubble_sort, selection_sort, insertion_sort

def make_case(n):
    return random.sample(range(1, 2 * n + 2), n)

def do_tests(sort_function, test_count=5, case_size=10):
    for i in range(test_count):
        case = make_case(case_size)
        result = case[:]
        sort_function(result)
        correct = sorted(case)
        if correct != result:
            error_explanation = f"\u274C Sorting failed for sort <{sort_function.__name__}> (test {i+1} of {test_count}, size {case_size})"
            raise AssertionError(
                f"{error_explanation}\n   input: {case}\n  output: {result}\n  correct: {correct}"
            )

def import_and_test(sort_name, sort_func):
    try:
        for size in range(5, 51, 5):
            do_tests(sort_func, 20, size)
    except Exception as e:
        print(e)
        return
    print(f"\u2705 {sort_name} passed tests")

for sort_func_name, sort_func in [("bubble_sort", bubble_sort), ("selection_sort", selection_sort), ("insertion_sort", insertion_sort)]:
    import_and_test(sort_func_name, sort_func)