import cotegen

# http://codeforces.com/problemset/problem/734/A

from typing import List

class CF734A(cotegen.Task):
    input_parameters = \
        {
            'a': cotegen.types.IntegerSequence(1, 20, 0, 1),
        }

    output_type = str

    def solve(a: List[int]):
        win_diff = 0
        for x in a:
            if x == 0:
                win_diff += 1
            if x == 1:
                win_diff -= 1
        if win_diff > 0:
            return 'Anton'
        elif win_diff < 0:
            return 'Danik'
        else:
            return 'Friendship'

    def compare(user_answer: str, jury_answer: str) -> bool:
        return user_answer == jury_answer

    @staticmethod
    def convert_input_to_string(a: List[int]):
        return ("%d\n" % len(a)) + "".join(map(lambda x: "AD"[x], a)) + "\n"


if __name__ == '__main__':
    CF734A.generate_test_files("~/Downloads/CS453/CF734A")
