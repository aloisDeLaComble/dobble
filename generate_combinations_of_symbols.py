import itertools
import numpy as np


space_dimension = 2 # space_dimension ** 2 + space_dimension + 1 = number_of_cards
highest_number_on_dimension = space_dimension
highest_number_on_dimension = 2 # equals number of card sharing the same symbol


def build_lines():
    lines = []
    for line_parameters in itertools.product(range(highest_number_on_dimension), repeat=space_dimension + 1):
        line_parameters = np.asarray(line_parameters)
        if are_all_coordinates_coefficients_zeros(line_parameters):
            continue
        print("line_parameters")
        print(line_parameters)
        line = get_points_in_line(line_parameters)
        print(line)
        print()

        lines.append(line)

def are_all_coordinates_coefficients_zeros(line_parameters):
    coordinates_coefficients = line_parameters[:-1]
    return np.sum(coordinates_coefficients) == 0


def get_points_in_line(line_parameters):
    return { point for point in itertools.product(range(highest_number_on_dimension), repeat=space_dimension) if is_solving_equation(line_parameters, point) }

def is_solving_equation(line_parameters, point):
    coordinates_coefficients = line_parameters[:-1]
    offset = line_parameters[-1]
    point = np.asarray(point)
    value_of_point_in_equation = (np.sum((coordinates_coefficients * point)) + offset)  % highest_number_on_dimension
    # print(line_parameters)
    # print(point)
    # print(value_of_point_in_equation)
    # print()
    return value_of_point_in_equation == 0

build_lines()
