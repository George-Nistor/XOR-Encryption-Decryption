# Proiect 0x00 - Arhitectura Sistemelor de Calcul 


##### **G.E.T. team**
+ Dîrțu Ecaterina (142)
+ Mihăilescu Teodor (142)
+ Nistor Gheorghe (142)


## Etapa 1

### Descriere
Am creat un script care [criptează](https://github.com/George-Nistor/ASC-Project-0x00/blob/main/encrypt.py) un fișier text într-unul binar fară extensie cu ajutorul unei chei bit cu bit folosind metoda de **criptare xor**. Asemănător am realizat [decriptarea](https://github.com/George-Nistor/ASC-Project-0x00/blob/main/decrypt.py) unui fișier binar într-unul de tip text cu ajutorul cheii inițiale.

### Mod de folosire
**Criptare**
```
$ python3 encrypt.py <key> <input.txt> <output>
```
**Decriptare**
```
$ python3 decrypt.py <key> <input> <output.txt>
```

## Etapa 2

### Descriere

În această secțiune a proiectului am aflat cheia cu care a fost criptat fișierul output al echipei [**The Cyphers**](https://github.com/fredtux/ASC_Proiect_0x00).

Cheia folosită este **ASCemisto111**.

### Metoda 1

Știind faptul că parola poate avea între 10 și 15 caractere, am creat un script [find_key.py](https://github.com/George-Nistor/ASC-Project-0x00/blob/main/find_key.py) care aplică operația **xor** între primele 30 de caractere din input.txt și output, iar în felul acesta s-a putut remarca o secvență care se repetă în rezultat: cheia utilizată.

**Spargere cheie în funcție de input și output**
```
$ python3 find_key.py <text file> <binary file>
```


### Metoda 2

Scriptul folosit pentru a afla cheia folosindu-mă doar de fișierul binar output este [find_key_brute.py](https://github.com/George-Nistor/ASC-Project-0x00/blob/main/find_key_brute.py).

Primul pas a fost să aflu lungimea cheii, iar asta am făcut-o bazându-mă pe faptul că într-un text lung din limba română cele mai frecvente caractere sunt **' ', 'a', 'e' și 'i'**, iar ele reprezintă aproximativ **40%** din toate caracterele. Am verificat pe rând unde este respectată această regula, verificănd toate cele cinci lungimi posibile ale cheii (de la 10 la 15). Cu un contor care merge din 10 în 10 (11 în 11 șamd.) am memorat frecvența caracterelor peste care s-a aplicat operația xor și am calculat procentul de apariție al primelor 4 cele mai frecvente caractere din tot textul. Dacă procentul este în jur de 40% atunci înseamnă că am găsit lungimea cheii care a fost aplicată pe text prin operația **xor**.

Următorul pas a fost să aplic operația **xor** între caracterele din text (cu un indice în funcție de lungimea cheii) și toate caracterele alfanumerice pentru a afla cheia. Validarea caracterului alfanumeric (dacă e cel corespunzător cheii) a fost făcută identic, cum am prezentat mai sus, aflând procentul de apariție al celor 4 caractere: ' ', 'a', 'e', 'i' și verificând dominanța în text.

**Spargere cheie în funcție de output**
```
$ python3 find_key_brute.py
```
***
*<p align="center">FMI UniBuc 2021</p>*