# Synthetic Python sample 29; intended focus: C2.

from functools import wraps


def announce(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        print('Running:', function.__name__)
        return function(*args, **kwargs)
    return wrapper


class ScorePolicy:
    def __init__(self, passing=60):
        self.passing = passing

    def evaluate(self, score):
        return 'pass' if score >= self.passing else 'retry'


class AdvancedScorePolicy(ScorePolicy):
    def evaluate(self, score):
        result = super().evaluate(score)
        return result.upper()


@announce
def build_report(names, scores, policy):
    doubled = list(map(lambda score: min(100, score * 2), scores))
    records = []
    for index, (name, score) in enumerate(zip(names, doubled), start=1):
        records.append({
            'rank': index,
            'name': name,
            'score': score,
            'status': policy.evaluate(score),
        })
    return sorted(records, key=lambda item: item['score'], reverse=True)


@announce
def display_report(records):
    for record in records:
        print(record['name'], record['score'], record['status'])


def main():
    names = ['Ada', 'Ben', 'Cleo', 'Dara']
    scores = [41, 28, 49, 35]
    policy = AdvancedScorePolicy(70)
    report = build_report(names, scores, policy)
    display_report(report)
    print('Number of students:', len(report))


if __name__ == '__main__':
    main()