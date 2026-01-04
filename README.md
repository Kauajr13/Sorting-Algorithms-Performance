# Sorting Algorithms Performance Analysis

This project performs an empirical analysis of various sorting algorithms, measuring execution time across different input scenarios to validate theoretical time complexity notations.

## Overview

The study compares standard sorting algorithms by executing them against datasets of varying sizes ($N$) and pre-existing orders (Ascending, Descending, and Random). The goal is to observe the growth rate of execution time and compare $O(n^2)$ algorithms versus $O(n \log n)$ algorithms in practice.



## Algorithms Implemented

The following algorithms are analyzed:

* **Bubble Sort:** Simple comparison-based sorting algorithm with $O(n^2)$ complexity.
* **Insertion Sort:** Builds the final sorted array one item at a time. Efficient for small or nearly sorted data.
* **Merge Sort:** Divide and conquer algorithm with guaranteed $O(n \log n)$ complexity.
* **Quick Sort:** Divide and conquer algorithm. Efficient on average but sensitive to pivot selection.
* **Heap Sort:** Comparison-based sorting algorithm based on the Binary Heap data structure.

## Methodology

The analysis script (`main.py`) performs the following steps:

1.  **Data Generation:** Generates integer lists of sizes $N = [10, 100, 1000, 5000]$.
2.  **Scenarios:**
    * **Ascending:** Best-case scenario for some algorithms (e.g., Insertion Sort).
    * **Descending:** Worst-case scenario for others.
    * **Random:** Average-case scenario.
3.  **Measurement:** Uses `time.perf_counter()` for high-precision timing.
4.  **Isolation:** Uses `copy.deepcopy()` to ensure each algorithm operates on the original unsorted data without side effects.

## Usage

Ensure you have Python 3.x installed. Run the main analysis script:

```bash
python main.py

## Sample Output

The script outputs the execution time in seconds for each algorithm under tested conditions:

Tamanho do vetor: 1000

  Entrada: Aleatório
    Bubble Sort    : 0.123456 segundos
    Insertion Sort : 0.098765 segundos
    Merge Sort     : 0.004321 segundos
    Quick Sort     : 0.003210 segundos
    Heap Sort      : 0.003500 segundos

## Technologies

* Python 3 (Standard Library)
