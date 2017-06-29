from typing import List

from jmetal.algorithm.multiobjective.nsgaii import NSGAII
from jmetal.algorithm.singleobjective.evolutionaryalgorithm import GenerationalGeneticAlgorithm
from jmetal.core.solution import BinarySolution, FloatSolution
from jmetal.operator.crossover import SinglePoint, SBX
from jmetal.operator.mutation import BitFlip, Polynomial
from jmetal.operator.selection import BinaryTournament
from jmetal.problem.multiobjectiveproblem import Fonseca, Kursawe
from jmetal.problem.singleobjectiveproblem import OneMax, Sphere

import logging

from jmetal.util.solution_list_output import SolutionListOutput

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main():
    #binary_example()
    float_example()
    #run_as_a_thread_example()
    #float_example_changing_the_stopping_condition()

def float_example() -> None:
    problem = Kursawe(3)
    algorithm = NSGAII[FloatSolution, List[FloatSolution]](
        problem,
        population_size = 100,
        max_evaluations = 25000,
        mutation = Polynomial(1.0/problem.number_of_variables, distribution_index=20),
        crossover = SBX(1.0, distribution_index=20),
        selection = BinaryTournament())

    algorithm.run()
    result = algorithm.get_result()
    logger.info("Algorithm (continuous problem): " + algorithm.get_name())
    logger.info("Problem: " + problem.get_name())
    logger.info("Computing time: " + str(algorithm.total_computing_time))

    #SolutionListOutput[FloatSolution].print_function_values_to_screen(result)
    SolutionListOutput[FloatSolution].print_function_values_to_file("FUN", result)

if __name__ == '__main__':
    main()