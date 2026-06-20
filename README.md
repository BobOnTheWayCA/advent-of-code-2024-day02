# Advent of Code 2024 - Day 2: Red-Nosed Reports

Python solution for Advent of Code 2024 Day 2.

## Summary

The solution checks whether each report is safe based on two rules:

1. The levels must be strictly increasing or strictly decreasing.
2. Each adjacent difference must be between 1 and 3 inclusive.

Part 2 adds the Problem Dampener rule, where a report is also safe if removing one level makes it safe.

## Run

```bash
python solution.py
```

The script reads from `input.txt` and prints the answers for Part 1 and Part 2.

## Note

The puzzle input is not included in this repository.
