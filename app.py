import unittest

# Define a test class that inherits from unittest.TestCase.
class TestFindPairsWithSum(unittest.TestCase):
    def test_find_pairs_with_sum(self):
        # Test case 1: Basic test case
        numbers = [1, 9, 5, 0, 20, -4, 12, 16, 7]
        target_sum = 12
        expected_result = [(5, 7), (16, -4), (12, 0)]
        
        # Check if the function find_pairs_with_sum produces the expected result.
        self.assertEqual(find_pairs_with_sum(numbers, target_sum), expected_result)

        # Test case 2: No pairs that sum up to the target
        numbers = [1, 2, 3, 4, 5]
        target_sum = 20
        expected_result = []
        
        # Check if the function handles the case when there are no pairs that sum up to the target.
        self.assertEqual(find_pairs_with_sum(numbers, target_sum), expected_result)

        # Test case 3: Negative numbers
        numbers = [-1, -2, -3, -4, -5]
        target_sum = -5
        expected_result = [(-1, -4), (-2, -3)]
        
        # Check if the function handles negative numbers and produces the correct result.
        self.assertEqual(find_pairs_with_sum(numbers, target_sum), expected_result)

if __name__ == '__main__':
    # Run the unit tests.
    unittest.main()
