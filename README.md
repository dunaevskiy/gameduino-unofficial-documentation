# Gameduino Unofficial Documentation
[![license](https://img.shields.io/badge/license-(cc)_by--nc--sa-blue.svg?style=flat-square)]() [![license](https://img.shields.io/badge/platform-arduino-green.svg?style=flat-square)]() [![license](https://img.shields.io/badge/shield-gameduino-green.svg?style=flat-square)]()

## Barva
Každá definovaná barva zabírá 16b (2B) paměti. Nejvyšší bit (typ A) určuje, zda tato barva je průhledná. Pokud ano, tak zbytek hodnot je ignorován, tzn. nelze vytvořit poloprůhlednou barvu.

![](images/hex_color.png)

Bity 0-14 jsou určeny pro ukládání odstínu. Většinou jsme zvyklí určovat každou z RGB barev hodnotou 8b a mít `256 * 256 * 256 = 16 777 216` barevných odstínů. Zde je každá ze základních barev určena 5b. Při transformaci z normálního obrázkového formátu dochází k přemapování hodnoty z 0-255 na 0-31, což snižuje celkový počet barevných odstínů na `32 768`.

Pro uložení barvy se používá little endian. Příklad uložení zelené barvy:

| Formát                       | Hodnota                |
|:-----------------------------|:-----------------------|
| RGB                          | (0, 255, 0)            |
| Binární gameduino            | 0b 0000 0011 1110 0000 |
| Hexadecimální gameduino      | 0x0BE0                 |
| Hexadecimální little endian  | 0xE00B                 |


## Licence
Toto dílo podléhá licenci [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-nc-sa/4.0/).

[![Creative Commons License](https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png)](http://creativecommons.org/licenses/by-nc-sa/4.0/)