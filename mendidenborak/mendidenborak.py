import json


class MendiDenborak:
    def __init__(self):
        self.ezaugarriak = {
            "bidea": "pista",
            "luzeera": 0,
            "igoera": 0,
            "jaitsiera": 0,
        }
        self.denbora = 0
        self.kalkuluak = {
            "pista": {"abiadura": 5500, "igoera": 600, "jaitsiera": 850},
            "bidexka": {"abiadura": 4500, "igoera": 500, "jaitsiera": 700},
            "bidexka-zaila": {"abiadura": 3600, "igoera": 400, "jaitsiera": 560},
            "bidez-kanpo": {"abiadura": 2900, "igoera": 320, "jaitsiera": 450},
        }

    def set(self, parametroa, balioa):
        self.ezaugarriak[parametroa] = balioa

    def kalkulatuDenbora(self):
        self.denbora = (
            self.ezaugarriak["luzeera"]
            / self.kalkuluak[self.ezaugarriak["bidea"]]["abiadura"]
            + self.ezaugarriak["igoera"]
            / self.kalkuluak[self.ezaugarriak["bidea"]]["igoera"]
            + self.ezaugarriak["jaitsiera"]
            / self.kalkuluak[self.ezaugarriak["bidea"]]["jaitsiera"]
        )

        return self.denbora
