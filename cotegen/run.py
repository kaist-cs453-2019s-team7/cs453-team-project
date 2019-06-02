from typing import List, Tuple

from .mutate import Mutator
from .task import Task
from .context import Status
from .test import TestSuite

import cotegen.ast_utils as ast_utils
import cotegen


class MutationRunner():
    def __init__(self, file_location):
        target_file = ast_utils.code_to_ast(file_location)
        Task.input_parameters = ast_utils.get_input_parameters(target_file)
        self.target_function = ast_utils.get_solve_function(target_file)
        self.compare_function = ast_utils.get_compare_function(target_file)
        self.convert = ast_utils.find_function(target_file, 'convert_input_parameters_to_test')

        self.mutations = []

        self.test_suite = None

        self.survived = []

    def generate_mutations(self):
        mutator = Mutator(self.target_function)
        mutator.apply_mutations()
        mutator.print_mutations()
        self.mutations = mutator.mutations

    def generate_initial_tests(self):
        inputs = Task.generate_tests()

        self.test_suite = TestSuite(self.target_function,
                               inputs, self.compare_function, self.convert)

    def execute_mutations(self):
        for mutation in self.mutations:
            mutation.execute(self.test_suite)

    def print_survived_mutants(self):
        for mutation in self.mutations:
            if mutation.status == Status.SURVIVED:
                mutation.print(verbose=True)

    def print_all_mutants(self):
        for mutation in self.mutations:
            mutation.print(verbose=False)


if __name__ == "__main__":
    runner = MutationRunner('examples/references/integers/996A.py')

    runner.generate_mutations()
    runner.generate_initial_tests()
    runner.execute_mutations()

    runner.print_all_mutants()
