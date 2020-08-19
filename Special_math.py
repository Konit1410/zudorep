import math
import sys


class SimpleMath:

    def sq_root_sum_by_product(arguments: list) -> complex():
        """square root of sum divided by product from setpoint of numbers"""
        ggg = 1
        if len(arguments) != 0:
            for i in arguments:
                if i !=0:
                    ggg = ggg * i
            return (sum(arguments) / ggg) ** 2


    def median_multiply_constants(n_num: list) -> complex:
        """median multiplay by have PI and added Epsilion constant"""
        EPSILON_CONSTANT = sys.float_info.epsilon
        HAVE_PI = math.pi / 2
        n = len(n_num)
        n_num.sort()
        if n != 0:
            if n % 2 == 0:
                median1 = n_num[n // 2]
                median2 = n_num[n // 2 - 1]
                median = (median1 + median2) / 2
                return median * HAVE_PI + EPSILON_CONSTANT
            else:
                median = n_num[n // 2]
                return median * HAVE_PI + EPSILON_CONSTANT
