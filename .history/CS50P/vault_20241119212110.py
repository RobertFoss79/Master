class Vault:
    def __init__ (self, galleons=0, sickles=0, knuts=0):
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts

potter = Vault(100, 50, 25)
print(potter)