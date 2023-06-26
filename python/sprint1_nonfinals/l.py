from collections import Counter
from typing import Tuple


def get_excessive_letter(shorter: str, longer: str) -> str:
    shorter = Counter(shorter)
    longer = Counter(longer)
    result = longer - shorter
    return ''.join(result.keys())


def read_input() -> Tuple[str, str]:
    shorter = input().strip()
    longer = input().strip()
    return shorter, longer


shorter, longer = read_input()
print(get_excessive_letter(shorter, longer))
