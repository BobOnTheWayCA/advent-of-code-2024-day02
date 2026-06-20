from pathlib import Path


def is_safe(report: list[int]) -> bool:

    if len(report) < 2:
        return True

    differences = [b - a for a, b in zip(report, report[1:])]

    all_increasing = all(diff > 0 for diff in differences)
    all_decreasing = all(diff < 0 for diff in differences)

    if not (all_increasing or all_decreasing):
        return False

    return all(1 <= abs(diff) <= 3 for diff in differences)


def is_safe_with_problem_dampener(report: list[int]) -> bool:

    if is_safe(report):
        return True

    for index in range(len(report)):
        reduced_report = report[:index] + report[index + 1:]
        if is_safe(reduced_report):
            return True

    return False


def parse_input(path: str = "input.txt") -> list[list[int]]:
    lines = Path(path).read_text().strip().splitlines()
    return [[int(value) for value in line.split()] for line in lines]


def main() -> None:
    reports = parse_input()

    part_1 = sum(is_safe(report) for report in reports)
    part_2 = sum(is_safe_with_problem_dampener(report) for report in reports)

    print(f"Part 1: {part_1}")
    print(f"Part 2: {part_2}")


if __name__ == "__main__":
    main()