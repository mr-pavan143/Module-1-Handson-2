def map_strategy_to_text(strategy_score):
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
