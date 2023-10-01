class LinearSearch:
    def __init__(self, arr: list, target: int) -> None:
        self.arr = arr
        self.target = target

    def algorithm(self) -> None:
        location = -1
        if self.target in self.arr:
            location = self.arr.index(self.target)

        if location < 0:
            print(f"{self.target} not found in the given list")
        else:
            print(f"{self.target} was found at {location} index in the list")
