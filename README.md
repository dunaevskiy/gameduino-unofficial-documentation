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


## Kodér obrázků a (de)komprese
Téměř určitě vznikne potřeba použít vlastní grafiku pro zobrazení na monitoru. Převod do hexadecimální podoby zajistí [Gameduino Background Encoder](http://gameduino.com/tools/).

### Background
Při standardním spuštění je vytvořen soubor `image.h`, jenž zabírá víc místa, ale popisuje všechny hodnoty v přesně zadaném pořadí. Takový soubor se do paměti gameduina ukládá jako:

```c
// Nahrát pořadová čísla znaků do paměti, počátek v RAM_PIC (0x0000)
for (byte y = 0; y < 1; y++)
   GD.copy(RAM_PIC + y * 64, image_pic + y * 1, 1);
// Nahrát znaky do paměti, počátek v RAM_CHR (0x1000)
GD.copy(RAM_CHR, image_chr, sizeof(image_chr));
// Nahrát barvy znaků do paměti, počátek v RAM_PAL (0x2000)
GD.copy(RAM_PAL, image_pal, sizeof(image_pal));
```

Pokud je potřeba šetřit pamětí arduina, tak existuje možnost komprese obrázku (`compress`). Pak se do paměti gameduina musí nahrávat s dekompresí:

```c
for (byte y = 0; y < 1; y++)
   GD.copy(RAM_PIC + y * 64, image_pic + y * 1, 1);
GD.uncompress(RAM_CHR, image_chr);
GD.uncompress(RAM_PAL, image_pal);
```

Pokud je počátek každé z pamětí již vyplněn daty, tak je potřeba posunout ukazatelé na vhodné místo.

## Licence
Toto dílo podléhá licenci [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-nc-sa/4.0/).

[![Creative Commons License](https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png)](http://creativecommons.org/licenses/by-nc-sa/4.0/)