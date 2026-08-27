import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

def create_fuzzy_system():
    # 1. New Antecedent/Consequent objects
    # Income scale: 0 to 100 (e.g., in thousands or a normalized score)
    income = ctrl.Antecedent(np.arange(0, 101, 1), 'income')
    # Spending scale: 0 to 100 (Low to High spending relative to income)
    spending = ctrl.Antecedent(np.arange(0, 101, 1), 'spending')
    # Strategy scale: 0 to 100 (Conservative to Aggressive strategy)
    strategy = ctrl.Consequent(np.arange(0, 101, 1), 'strategy')

    # 2. Auto-membership functions / Custom Membership functions
    income['low'] = fuzz.trapmf(income.universe, [0, 0, 25, 45])
    income['medium'] = fuzz.trimf(income.universe, [30, 50, 70])
    income['high'] = fuzz.trapmf(income.universe, [55, 75, 100, 100])

    spending['low'] = fuzz.trapmf(spending.universe, [0, 0, 20, 40])
    spending['medium'] = fuzz.trimf(spending.universe, [30, 50, 70])
    spending['high'] = fuzz.trapmf(spending.universe, [60, 80, 100, 100])

    strategy['conservative'] = fuzz.trapmf(strategy.universe, [0, 0, 20, 40])
    strategy['balanced'] = fuzz.trimf(strategy.universe, [30, 50, 70])
    strategy['aggressive'] = fuzz.trapmf(strategy.universe, [60, 80, 100, 100])

    # 3. Define Fuzzy Rules
    rule1 = ctrl.Rule(income['low'] & spending['high'], strategy['conservative'])
    rule2 = ctrl.Rule(income['low'] & spending['low'], strategy['balanced'])
    rule3 = ctrl.Rule(income['medium'] & spending['medium'], strategy['balanced'])
    rule4 = ctrl.Rule(income['high'] & spending['low'], strategy['aggressive'])
    rule5 = ctrl.Rule(income['high'] & spending['high'], strategy['balanced'])
    rule6 = ctrl.Rule(income['medium'] & spending['low'], strategy['aggressive'])
    rule7 = ctrl.Rule(income['low'] & spending['medium'], strategy['conservative'])

    # 4. Control system creation
    finance_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7])
    finance_simulator = ctrl.ControlSystemSimulation(finance_ctrl)
    
    return finance_simulator
