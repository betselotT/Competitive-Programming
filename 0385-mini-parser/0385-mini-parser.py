class Solution:
  def deserialize(self, s: str) -> NestedInteger:
    # If s doesn't start with a '[', it must be a single integer, so create a NestedInteger object with that value
    if s[0] != '[':
      return NestedInteger(int(s))

    # Create an empty stack to keep track of NestedInteger objects and sublists as we parse the input string
    stack = []

    # Loop through each character in the string
    for i, c in enumerate(s):
      if c == '[':
        # If we encounter an opening bracket, push a new empty NestedInteger object onto the stack and set the starting index for the next element
        stack.append(NestedInteger())
        start = i + 1
      elif c == ',':
        # If we encounter a comma, check if there was a number between the previous comma or opening bracket and this one.
        # If there was, create a new NestedInteger object with that value and add it to the NestedInteger object on the top of the stack
        if i > start:
          num = int(s[start:i])
          stack[-1].add(NestedInteger(num))
        # Update the starting index for the next element to be parsed
        start = i + 1
      elif c == ']':
        # If we encounter a closing bracket, pop the top NestedInteger object from the stack and check if there was a number between the previous comma or opening bracket and this one.
        # If there was, create a new NestedInteger object with that value and add it to the popped NestedInteger object
        popped = stack.pop()
        if i > start:
          num = int(s[start:i])
          popped.add(NestedInteger(num))
        # If there are still NestedInteger objects on the stack, add the popped NestedInteger to the one on top. Otherwise, return the popped NestedInteger
        if stack:
          stack[-1].add(popped)
        else:
          return popped
        # Update the starting index for the next element to be parsed
        start = i + 1