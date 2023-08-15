# Model: Solow Growth Model
class SolowGrowthModel:
    """
    A class for the Solow Growth Model, a macroeconomic model of growth that
    evaluates the impact of capital accumulation, labor growth, and technological 
    progress on an economy's output per worker and steady-state equilibrium.
    """
    def __init__(self, alpha, s, n, g, k_initial):
        """
        Parameters:
            alpha (float): Capital share in production.
            s (float): Savings rate.
            n (float): Population growth rate.
            g (float): Technological progress rate.
            k_initial (float): Initial capital stock.
        """
        self.alpha = alpha
        self.s = s
        self.n = n
        self.g = g
        self.k = k_initial
    
    def production_function(self):
        """
        Calculate the output based on the production function.
        Returns: float: The output in the economy.
        """
        output = self.k**self.alpha
        return output
    
    def capital_accumulation(self):
        """
        Calculate the change in capital stock due to investment and depreciation.
        Returns: float: The change in capital stock.
        """
        investment = self.s * self.production_function()
        depreciation = (self.n + self.g) * self.k
        delta_k = investment - depreciation
        return delta_k
    
    def update_capital_stock(self):
        """
        Update the capital stock based on capital accumulation.
        Returns: None
        """
        delta_k = self.capital_accumulation()
        self.k += delta_k
    
    def run_growth_model(self, num_periods):
        """
        Run the Solow growth model for a specified number of periods.
        Parameters:
            num_periods (int): Number of periods to simulate.
        Returns: list: List of capital stock values over time.
        """
        capital_stock_over_time = [self.k]
        for _ in range(num_periods):
            self.update_capital_stock()
            capital_stock_over_time.append(self.k)
        return capital_stock_over_time