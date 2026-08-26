## Heltall - unsigned
* 8 bit kan holde 256 ulike verdier
* Unsigned int 8bit: 0 ... 255
* Unsigned int 16bit: 0 ... 65536


## Heltall - signed
* 8 bit kan holde 256 ulike verdier
* Valg: første bit holder fortegn: 
    * 0 = +
    * 1 = -
* 0 .. 127 som vanlig, men hvilket negativt tall nå?

* Vanlig valg: -128, -127, ... (Two's complement)
* signed int 8bit: -128 .. 127
* signed int 16 bit . -32768 .. 32767


## Tekst:
* ASCII - 7 bit, nok til A-Z a-Z 0-9 .,;:"()!? osv.
* Ingen rom til tegn fra andre språk
* ASCII bruker bare 0x00 - 0x7F, kan bruke 0x80 - 0xff til andre ten, om vi fortsetter med 1 byte per tegn
* => codepages, trenger ulike til vest-eur., øst-eur., thai, gresk, kyrillisk,...
* samme byte blir brukt til ulike tegn på ulike codepages
* cp1252 (Windows code page) == ISO8859-1 

## Unicode
* mange flere enn 256 symboler er i bruk
* Unicode-prosjekt: et codepoint til hver glyph som finnes
* 0x000000 - 0x10FFFF: rom til litt over 1 million glyphs
* ![unicode.org](https://www.unicode.org)

* Enkel koding: UTF-32: bruk 4 bytes til hver glyph
* Inneholdet til bytes tilsvarer codepoint-nummer

## UTF-32 vs UTF-8
* Enkel koding: UTF-32: bruk 4 bytes til hver glyph
* Ulempe: 4x større filer enn ASCII
* ikke kompatibel med ASCII-filer
* Løsning: variable length coding
    * bruk de første bit-posisjonene som metadata.

UTF-8:
* Beholder de 128 bytes som ASCII
* 110X XXYY 10YY ZZZZ

| glyph | unicode point | name                 | utf-8   |
|-------|---------------|----------------------|---------|
| æ     | U+00e6        | Latin Small letter Æ | "c3 a6" |


## Unicode
* er hele problemet med ulike språk løst ved bruk av Unicode?
* med utf-8 snakker vi bare om datalagring
* Input? Presentasjon?

* Homoglyphs? Combining Characters?
Cyrillic small letter O:   o    U+043E
Latin small letter O:      о    U+006F


## Tilbake til tall
* Fixed point numbers
* Fast posisjon til desimalen. F.eks. 8bit signed 5/3 010111,011
* Hvilke tall kan vi representere?
* 32 helftall fra -16 .. 15, med 8 steg av 1/8 mellom tallene
* Fra 0x00 til 0xFF:
    * 0, 0.125, 0.25, 0.375, ... 15.875, -16, -15.875 ..., -0.25, 0

## Fixed point
* Fordel: alltid sammen *precision* (her: 1/8)
* Ulempe: avkortet range (fra -128..127 til -16..15)

## Floating point
* Høy *precision* nær 0, mindre *precision* jo større tallene blir

**\[+-\] 1.\[mantisse\] × 2<sup>\[eksponent\] - shift</sup>**


