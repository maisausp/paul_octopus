
import evaluate.evaluate as evaluator
from skopt import gp_minimize, forest_minimize
import validation.validation as validator
import constants.params as global_params

def get_dim_weight():

    default_parameters = [1, 1, 1, 3, 10]
    return default_parameters

def get_dim_network():

    default_parameters = [0.01, 2, 441, 'relu']

    return default_parameters

def print_result():
    print('x')
    print(search_result.x)
    print('fun')
    print(search_result.fun)
    print('iters')
    sorted(zip(search_result.func_vals, search_result.x_iters))
    print('best_accuracy')
    print(global_params.best_accuracy)

if __name__ == '__main__':

    default_parameters = get_dim_network()
    search_result = gp_minimize(func=evaluator.fitness_network, dimensions=evaluator.dimensions_network, acq_func='EI', n_calls=11, x0=default_parameters)
    print_result()
    validator.validate()

    print("Terminou")