import json


class MendiDenborak:
    def __init__(self):
        self.kalkuluak = {
            "pista": {"abiadura": 5500, "igoera": 600, "jaitsiera": 850},
            "bidexka": {"abiadura": 4500, "igoera": 500, "jaitsiera": 700},
            "bidexka-zaila": {"abiadura": 3600, "igoera": 400, "jaitsiera": 560},
            "bidez-kanpo": {"abiadura": 2900, "igoera": 320, "jaitsiera": 450},
        }


    def kalkulatuDenbora(self, bidea, luzeera, igoera, jaitsiera):
        denbora = (
            luzeera
            / self.kalkuluak[bidea]["abiadura"]
            + igoera
            / self.kalkuluak[bidea]["igoera"]
            + jaitsiera
            / self.kalkuluak[bidea]["jaitsiera"]
        )

        return denbora
