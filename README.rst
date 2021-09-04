========
MendiDenborak
========

Mendian oinez ibilbide desberdinetan zenbat denbora beharko dugun kalkulatzeko paketea

* Free software: GNU General Public License v3


Erabilera eta instalazioa
-------------------------

Instalatu paketea pip erabiliz:

    $ pip install mendidenborak

Erabiltzeko inportatu paketea eta deitu metodoei:

    >>> from mendidenborak import MendiDenborak
    >>> md = MendiDenborak()
    ...
    >>>
    >>> md.set("bidea", "pista")
    >>> md.set("luzeera", 10000)
    >>> md.set("igoera", 300)
    >>> md.set("jaitsiera", 200)
    >>> md.kalkulatuDenbora()
    ...
    >>> 2.553475935828877

Funtzioen azalpena
------------------

set(izena, balioa)
~~~~~~~~~~~~~~~~~

gure ibilbidearen ezaugarriak ezartzeko metodoa. "bidea", "luzeera", "igoera" eta "jaitsiera" daude erabilgarri.

"bidea" aukerak: "pista", "bidexka", "bidexka-zaila", "bidez-kanpo"
"luzeera": ibilbidearen luzeera metrotan
"igoera": ibilbidearen igoera metatua metrotan
"jaitsiera": ibilbidearen jaitsiera metatua metrotan


kalkulatuDenbora()
~~~~~~~~~~~~~~~~~~~~~

Ezarri diren parametroen araberako kalkulua itzultzen du ordutan.
