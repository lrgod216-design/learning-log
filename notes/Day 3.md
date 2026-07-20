# Day 3 — [2026/7/20]

**Week:** 1 · **Focus today:** 

## What I did
- 
## What I actually understood (in my own words)
- Division in python always return float. If want integer, use ```// ``` instead of ```/```
### List:
```
    # Example 1
    
    fruits = ["apple", "banana", "orange"]
    fruits.append("grape") # ["apple", "banana", "orange", "grape"], append an item at last
    
    fruits.insert(0,"kiwi") # ["kiwi", "apple", "banana", "orange", "grape"], insert item at specified index

    fruits.remove("banana")     # Remove by value
    last = fruits.pop()        # Remove and return last
    del fruits[0]              # Remove by index
​


    # Example 2

    numbers = [3, 1, 4, 1, 5, 9]

    # Information
    print(len(numbers))         # 6 (length)
    print(numbers.count(1))     # 2 (count occurrences)
    print(numbers.index(4))     # 2 (find position)

    # Sorting
    numbers.sort()              # Sort in place
    print(numbers)              # [1, 1, 3, 4, 5, 9]

    numbers.reverse()           # Reverse order
    print(numbers)              # [9, 5, 4, 3, 1, 1]

    # Copy
    new_list = numbers.copy()   # Create a copy

```

### Dictionary:

```
    # Example

    person = {"name": "Alice", "age": 30, "city": "New York"}

    # Get values by key
    print(person["name"])       # "Alice"
    print(person["age"])        # 30

    # Safer with get()
    print(person.get("job"))    # None (no error)
    print(person.get("job", "Unknown"))  # "Unknown" (default)

    # Add or update
    person["email"] = "alice@email.com"  # Add new
    person["age"] = 31                   # Update existing

    # Remove items
    del person["email"]              # Remove by key
    age = person.pop("age")          # Remove and return
    person.clear()                   # Remove all items

    # Get all keys, values, or items
    print(person.keys())    # dict_keys(['name', 'age', 'city'])
    print(person.values())  # dict_values(['Alice', 30, 'New York'])
    print(person.items())   # dict_items([('name', 'Alice'), ...])

    # Check if key exists
    if "name" in person:
        print("Name found!")

    # Update multiple values
    person.update({"age": 31, "job": "Engineer"})

    # Dictionary of dictionaries
    students = {
        "alice": {"age": 20, "grade": "A"},
        "bob": {"age": 21, "grade": "B"},
        "charlie": {"age": 19, "grade": "A"}
    }

    # Access nested data
    print(students["alice"]["grade"])  # "A"
```
    - Keys have to be ** immutable **







## What confused me / still don't get
- 

## LeetCode today
- 

## Tomorrow's first task
- 
