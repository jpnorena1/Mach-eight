  # Find Pairs with Sum Program

This Python program is designed to find pairs of integers from a list that sum up to a given target value. The program provides an efficient solution that works in better than O(n^2) time complexity.

## Usage

To use the program, you can follow these steps:

1. Ensure you have Python installed on your system.

2. Clone or download this repository to your local machine.

3. Open a terminal or command prompt and navigate to the directory where the program is located.

4. Run the program by executing the following command:

```bash
python app.py <list_of_numbers> <target_sum>
Replace <list_of_numbers> with a comma-separated list of integers, and <target_sum> with the integer you want to find pairs for.
For example:
python app.py 1,9,5,0,20,-4,12,16,7 12

Example Output

The program will output the pairs of integers that sum up to the target value, as shown below:
+ 5 , 7
+ 16 , -4
+ 12 , 0
Testing

Unit tests have been included to ensure the correctness of the find_pairs_with_sum function. You can run the tests using the following command:
python -m unittest test_find_pairs
Program Details

    The core functionality of finding pairs with the desired sum is provided by the find_pairs_with_sum function located in app.py.

    The program avoids using an O(n^2) algorithm by utilizing a set to keep track of the numbers it has encountered so far while iterating through the list.

    Each number is checked against its complement (the difference between the target sum and the current number). If the complement is found in the set of seen numbers, a valid pair is detected.

    The program then outputs the pairs it finds in the specified format.

Contributions

Contributions to this program are welcome. Feel free to fork this repository, make changes, and submit a pull request with your improvements.
License

This program is licensed under the MIT License - see the LICENSE file for details.