import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

def create_fuzzy_system():
    income = ctrl.Antecedent(np.arange(0, 101, 1), 'income')
    spending = ctrl.Antecedent(np.arange(0, 101, 1), 'spending')
    strategy = ctrl.Consequent(np.arange(0, 101, 1), 'strategy')

    income['low'] = fuzz.trapmf(income.universe, [0, 0, 25, 45])
    income['medium'] = fuzz.trimf(income.universe, [30, 50, 70])
    income['high'] = fuzz.trapmf(income.universe, [55, 75, 100, 100])

    spending['low'] = fuzz.trapmf(spending.universe, [0, 0, 20, 40])
    spending['medium'] = fuzz.trimf(spending.universe, [30, 50, 70])
    spending['high'] = fuzz.trapmf(spending.universe, [60, 80, 100, 100])

    strategy['conservative'] = fuzz.trapmf(strategy.universe, [0, 0, 20, 40])
    strategy['balanced'] = fuzz.trimf(strategy.universe, [30, 50, 70])
    strategy['aggressive'] = fuzz.trapmf(strategy.universe, [60, 80, 100, 100])

    rule1 = ctrl.Rule(income['low'] & spending['high'], strategy['conservative'])
    rule2 = ctrl.Rule(income['low'] & spending['low'], strategy['balanced'])
    rule3 = ctrl.Rule(income['medium'] & spending['medium'], strategy['balanced'])
    rule4 = ctrl.Rule(income['high'] & spending['low'], strategy['aggressive'])
    rule5 = ctrl.Rule(income['high'] & spending['high'], strategy['balanced'])
    rule6 = ctrl.Rule(income['medium'] & spending['low'], strategy['aggressive'])
    rule7 = ctrl.Rule(income['low'] & spending['medium'], strategy['conservative'])

    finance_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7])
    return ctrl.ControlSystemSimulation(finance_ctrl)
