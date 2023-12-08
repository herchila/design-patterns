from typing import List

class SortingStrategy:
    def sort(self, dataset: List[int]) -> List[int]: pass

class QuickSort(SortingStrategy):
    def sort(self, dataset: List[int]) -> List[int]:
        print("Sorting using quick sort")
        return sorted(dataset)  # Simplification for demonstration

class MergeSort(SortingStrategy):
    def sort(self, dataset: List[int]) -> List[int]:
        print("Sorting using merge sort")
        return sorted(dataset)  # Simplification for demonstration

class Sorter:
    def __init__(self, strategy: SortingStrategy):
        self._strategy = strategy

    def sort(self, dataset: List[int]) -> List[int]:
        return self._strategy.sort(dataset)

# Usage
dataset = [1, 5, 3, 4, 2]

sorter = Sorter(QuickSort())
sorter.sort(dataset)  # Sorting using quick sort

sorter = Sorter(MergeSort())
sorter.sort(dataset)  # Sorting using merge sort
