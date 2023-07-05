#Name: Ajani Levere
#Date: 06/06/23
#Purpose: Creates derived class of charm that has an instance-specific attribute, symbol

from charm import Charm

class CharacterCharm(Charm):
    
    #Instantiate object like:
    #charm3 = CharacterCharm("Peter Griffin", "Man with white shirt and green pants", 100000, Charm.condition.PRISTINE, "Family Guy")
    def __init__(self, name, description, retailPrice, condition, series):
        super().__init__(name, description, retailPrice, condition)
        #series attribute describes what franchise/series character comes from
        self.__series = series
    
    #getter for series
    def getSeries(self):
        return self.__series
    
    #because these charms are of such high value, they will be calculated similarly to the collectible charm:
        #retail price * (condition's value * 0.1) - condition has a significant impact on charm's value
        #condition can make $50 charm be the same as its retail price with a pristine condition, but $5 with a poor condition
    def getMarketValue(self):
        marketValue = float(f"{(self.getRetailPrice())*(self.getCondition().value * 0.1):.2f}")
        return marketValue
    
    #String representation: A PRISTINE charm of Peter Griffin from Family Guy
    def __str__(self):
        return f"A {str(self.getCondition())[10:]} charm of {str(self.getName())} from {str(self.getSeries())}"

    #comparison overloaded methods - except for eq and ne, they just compare market value
    def __lt__(self, other):
        if self.getMarketValue() < other.getMarketValue():
            return True
        else:
            return False
    
    def __le__(self, other):
        if self.getMarketValue() <= other.getMarketValue():
            return True
        else:
            return False
    
    def __gt__(self, other):
        if self.getMarketValue() > other.getMarketValue():
            return True
        else:
            return False
    
    def __ge__(self, other):
        if self.getMarketValue() >= other.getMarketValue():
            return True
        else:
            return False
        
    #equal only if name, series, and condition are equal
    def __eq__(self, other):
        n = self.getName() == other.getName()
        c = self.getCondition() == other.getCondition()
        s = self.getSeries() == other.getSeries()
        
        return (n and c and s)
    
    #not equal if any of the attributes are not exactly the same
    def __ne__(self, other):
        n = self.getName() != other.getName()
        c = self.getCondition() != other.getCondition()
        s = self.getSeries() != other.getSeries()
        
        return (n or c or s)

# Write code below that tests your new class
if __name__ == "__main__":
    pgCharm = CharacterCharm("Peter Griffin", "Man with white shirt and green pants", 100000, Charm.Condition.PRISTINE, "Family Guy")
    print(pgCharm)