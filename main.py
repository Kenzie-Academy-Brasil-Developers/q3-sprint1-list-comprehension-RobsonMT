def list_comprehension_exercise_1() -> list[int]:
    return [num for num in range(11)]


def list_comprehension_exercise_2() -> list[int]:
    return [num for num in range(22) if num%2==0 or num%3==0]


def list_comprehension_exercise_3() -> list[int]:
    return [num for num in range(-5,32) if num%2!=0 and num%5!=0]


def list_comprehension_exercise_4() -> list[int]:
    return [num*num for num in range(11)]


def list_comprehension_exercise_5(sentence: str) -> list[str]:
    return [word for word in sentence if word.strip(' ') == word.upper()]


def list_comprehension_exercise_6(sentence: str) -> list[str]:
    return [w for w in sentence.split(' ') if w.startswith('r') and len(w) >= 4]

