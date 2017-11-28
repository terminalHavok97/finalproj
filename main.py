#!/usr/bin/python
#Tom Vaughan - tv15461
try:
    from experiment import Experiment
except ImportError:
    raise ImportError('<Experiment import error>')

exp = Experiment(3, 5, 10)

#TODO Get cmd arguments in????
#TODO Work out how sample sizes and multiple participants will work
