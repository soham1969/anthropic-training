def greeting():
    print("Hi there")


def calculate_pi_to_5th_digit():
    """
    Calculate the value of pi to the 5th digit using the Machin formula.
    Machin formula: pi/4 = 4*arctan(1/5) - arctan(1/239)
    Returns pi rounded to 5 decimal places: 3.14159
    """
    from decimal import Decimal, getcontext
    
    # Set precision high enough for accurate calculation
    getcontext().prec = 50
    
    # Using Machin formula: pi = 16*arctan(1/5) - 4*arctan(1/239)
    def arctan(x, num_terms=100):
        """Calculate arctan using Taylor series"""
        x = Decimal(x)
        power = x
        result = power
        for n in range(1, num_terms):
            power *= -x * x
            result += power / (2 * n + 1)
        return result
    
    pi = 4 * (4 * arctan(Decimal(1)/Decimal(5)) - arctan(Decimal(1)/Decimal(239)))
    
    # Round to 5 decimal places
    pi_rounded = float(round(pi, 5))
    return pi_rounded