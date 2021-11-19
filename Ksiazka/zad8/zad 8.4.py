# prune a dictionary

def dict_take(dict_a, dict_b):
    try:
        return {n : dict_b[y] for n in dict_a for y in dict_b if n == y }
    except Exception:
        pass


dict_a = {1: "one", 2: "two", 3: "three", 5: "five", 6: "six"}
dict_b = {1: "one", 3: "three", 4: "four", 6: "six"}

print(dict_take(dict_a, dict_b))