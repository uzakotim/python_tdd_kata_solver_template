import sys
import unittest
from io import StringIO

def solve():
    """
    Implement your solution here.
    Use standard input() and print().
    """
    # take n as number of groups
    n = int(input())

    # take group sizes as input
    groups = list(map(int, input().split()))
    groups.sort(reverse=True)
    taxis = 0
    while groups:
        group = groups.pop(0)
        while group < 4:
            if groups:
                group += groups[-1]
                if group > 4:
                    break
                groups.pop(-1)
            else:
                break
        taxis+=1
        

    print(taxis)



class TestSolution(unittest.TestCase):
    def assertIO(self, input_data: str, expected_output: str):
        """
        Helper method to test the solve function.
        It redirects sys.stdin and sys.stdout.
        """
        sys.stdin = StringIO(input_data.strip('\n'))
        sys.stdout = StringIO()

        try:
            solve()
            output = sys.stdout.getvalue().strip('\n')
            self.assertEqual(output, expected_output.strip('\n'))
        finally:
            # Restore standard input and output
            sys.stdin = sys.__stdin__
            sys.stdout = sys.__stdout__

    def test_example_1(self):
        # Add your example input and expected output here
        input_data = """8\n2 3 4 4 2 1 3 1"""
        expected_output = "5"
        # Uncomment the line below to run the test
        self.assertIO(input_data, expected_output)
    
    def test_example_2(self):
        # Add your example input and expected output here
        input_data = """12\n1 1 1 1 1 1 1 1 1 1 1 1"""
        expected_output = "3"
        # Uncomment the line below to run the test
        self.assertIO(input_data, expected_output)
    
    def test_example_3(self):
        # Add your example input and expected output here
        input_data = """5\n1 2 4 3 3"""
        expected_output = "4"
        # Uncomment the line below to run the test
        self.assertIO(input_data, expected_output)

if __name__ == '__main__':
    if sys.stdin.isatty():
        # Running locally in a normal terminal - run tests
        unittest.main()
    else:
        # Redirected input (Codeforces, pipe, etc.) - run the solution
        solve()
