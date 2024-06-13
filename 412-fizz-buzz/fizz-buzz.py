class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        return [("Fizz" * (1 if (i % 3 == 0) else 0) + "Buzz" * (1 if (i % 5 == 0) else 0)) if ("Fizz" * (1 if (i % 3 == 0) else 0) + "Buzz" * (1 if (i % 5 == 0) else 0)) != "" else str(i) for i in range(1, n+1)]        