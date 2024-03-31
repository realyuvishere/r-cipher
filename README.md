# r-cipher

A numerical string reversal cipher which encrypts string data effectively

There are 2 levels of reversal in encryption:

- **Level 1**: It splits the string into groups and reverses the groups. It then combines and outputs the encrypted string with the same spacing as the original string
- **Level 2**: Splits and reverses the groups, same as the level 1. The combined string is then reversed again as a whole, and the output is this string split by the spaces similar to the original string

The following demonstrations will elaborate how the method works:

```
(LEVEL 1 REVERSAL ENCRYPTION)

Key = 3

S = HELP ME PLEASE

HELPMEPLEASE
HEL PME PLE ASE
LEH EMP ELP ESA
LEHEMPELPESA
LEHE MP ELPESA
```

```
(LEVEL 2 REVERSAL ENCRYPTION)

Key = 3

S = HELP ME PLEASE

HELPMEPLEASE
HEL PME PLE ASE
LEH EMP ELP ESA
LEHEMPELPESA
ASEPLEPMEHEL
ASEP LE PMEHEL
```

```
(LEVEL 1 REVERSAL DECRYPTION)

Key = 3

S = LEHE MP ELPESA

LEHEMPELPESA
LEH EMP ELP ESA
HEL PME PLE ASE
HELPMEPLEASE
HELP ME PLEASE
```

```
(LEVEL 2 REVERSAL ENCRYPTION)

Key = 3

S = ASEP LE PMEHEL

ASEPLEPMEHEL
LEHEMPELPESA
LEH EMP ELP ESA
HEL PME PLE ASE
HELPMEPLEASE
HELP ME PLEASE
```
