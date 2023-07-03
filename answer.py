#question-17
def get_even_numbers(numbers):
    return [num for num in numbers if num % 2 == 0]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = get_even_numbers(numbers)
print(even_numbers)


#question-18
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Execution time: {execution_time:.5f} seconds")
        return result
    return wrapper


#question-19
def calculate_mean(numbers):
    if not numbers:
        return None

    total_sum = sum(numbers)
    count = len(numbers)
    mean = total_sum / count
    return mean
data = [10, 15, 20, 25, 30]
mean_value = calculate_mean(data)
print("Mean:", mean_value)


#question-20
from scipy.stats import ttest_ind

def perform_hypothesis_test(sample1, sample2):
    t_statistic, p_value = ttest_ind(sample1, sample2)
    return p_value

sample1 = [5, 10, 15, 20, 25]
sample2 = [10, 20, 30, 40, 50]
p_value = perform_hypothesis_test(sample1, sample2)
print("P-value:", p_value)
