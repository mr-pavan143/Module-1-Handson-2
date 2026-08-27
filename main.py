import os

# --- FILE GENERATION CODE ---
# Dictionary defining file paths and their respective contents
project_files = {
    "config/__init__.py": "",
    "utils/__init__.py": "",
    "config/fuzzy_system.py": '''import numpy as np
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
''',
    "utils/data_processor.py": '''def map_strategy_to_text(strategy_score):
    if strategy_score < 35:
        return {
            "Classification": "Conservative / High Risk Profile",
            "Strategy": "Capital Preservation & Debt Relief",
            "Actions": [
                "Build an emergency fund covering 6 months of expenses.",
                "Prioritise paying off high-interest debts.",
                "Focus on low-risk allocations like fixed deposits or government bonds."
            ]
        }
    elif 35 <= strategy_score < 65:
        return {
            "Classification": "Balanced / Moderate Risk Profile",
            "Strategy": "Wealth Growth & Moderate Security",
            "Actions": [
                "Maintain a diversified portfolio (50% Equities, 50% Fixed Income).",
                "Automate monthly savings into index funds.",
                "Review insurance coverage and mid-term financial goals."
            ]
        }
    else:
        return {
            "Classification": "Aggressive / High Growth Profile",
            "Strategy": "Wealth Maximisation & Investment",
            "Actions": [
                "Allocate a larger portion (70%+) to growth equities or mutual funds.",
                "Explore alternative investments or real estate vehicles.",
                "Optimise tax-saving investment instruments."
            ]
        }
'''
}

def build_structure():
    """Creates the files and directories listed in project_files."""
    print("Initializing fuzzy logic project directory configuration...")
    for path, content in project_files.items():
        folder = os.path.dirname(path)
        if folder and not os.path.exists(folder):
            os.makedirs(folder)
            print(f"Created folder: {folder}")
        
        with open(path, "w") as f:
            f.write(content)
            print(f"Created file: {path}")

# --- EXECUTION ENGINE ---
if __name__ == "__main__":
    # 1. Build the system architecture
    build_structure()
    print("-" * 50)

    # 2. Dynamic Local Imports (After generation)
    from config.fuzzy_system import create_fuzzy_system
    from utils.data_processor import map_strategy_to_text

    # 3. Test Case Evaluation
    # Example User Profile: High Income (85/100), Low relative Spending (25/100)
    user_income = 85
    user_spending = 25

    print(f"\nProcessing behavioral profile -> Income: {user_income}, Spending Habits: {user_spending}")
    
    try:
        simulator = create_fuzzy_system()
        simulator.input['income'] = user_income
        simulator.input['spending'] = user_spending
        
        # Crunch the numbers / Defuzzify
        simulator.compute()
        crisp_output = simulator.output['strategy']
        
        # Parse strategy mapping
        recommendation = map_strategy_to_text(crisp_output)
        
        print("\n=== SYSTEM ANALYSIS RESULTS ===")
        print(f"Computed Strategy Score: {crisp_output:.2f}/100")
        print(f"Behavior Category:       {recommendation['Classification']}")
        print(f"Recommended Strategy:    {recommendation['Strategy']}")
        print("\nAction Items:")
        for action in recommendation['Actions']:
            print(f" - {action}")
            
    except ImportError:
        print("\nError: Please make sure 'scikit-fuzzy' and 'numpy' are installed.")
        print("Run: pip install numpy scikit-fuzzy")
