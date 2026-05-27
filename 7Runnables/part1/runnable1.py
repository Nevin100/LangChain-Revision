# Runnables in Langchain
# Runnables are a powerful abstraction in Langchain that allow you to define and execute a sequence of operations in a flexible and modular way. They can be used to create complex workflows, automate tasks, and integrate various components of your application seamlessly.

# In this example, we will create a simple Runnable that takes a list of numbers, processes them, and returns the results. We will define a Runnable that squares each number in the list and then sums the squared values. 

from langchain import Runnable
class SquareAndSumRunnable(Runnable):
    def __init__(self, numbers):
        self.numbers = numbers

    def run(self):
        # Step 1: Square each number
        squared_numbers = [x ** 2 for x in self.numbers]
        
        # Step 2: Sum the squared numbers
        result = sum(squared_numbers)
        
        return result
    
# Example usage
if __name__ == "__main__":
    numbers = [1, 2, 3, 4]
    runnable = SquareAndSumRunnable(numbers)
    result = runnable.run()
    print(f"The sum of squares of {numbers} is: {result}")
    
# In this code, we define a class `SquareAndSumRunnable` that inherits from `Runnable`. The constructor takes a list of numbers as input. The `run` method performs the operations: it first squares each number in the list and then sums the squared values. Finally, we create an instance of the Runnable with a sample list of numbers and execute it to get the result.