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
    >>> md.kalkulatuDenbora("pista", 10000, 300, 200)
    >>> 2.553475935828877

Funtzioen azalpena
------------------

kalkulatuDenbora(bidea, luzeera, igoera, jaitsiera)
~~~~~~~~~~~~~~~~~~~~~

Ematen zaizkion balioen araberako kalkulua itzultzen du ordutan.

Balioak:
"bidea" aukerak: "pista", "bidexka", "bidexka-zaila", "bidez-kanpo"
"luzeera": ibilbidearen luzeera metrotan
"igoera": ibilbidearen igoera metatua metrotan
"jaitsiera": ibilbidearen jaitsiera metatua metrotan