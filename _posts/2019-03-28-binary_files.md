---
title: "Editing Binary Data : Gran Turismo 2"
layout : post
author : Adam Henderson
category : Fun
use_math : true
---

Topics:
----- 
* Tools for analyzing and modifying binary files. (`cmp`, `dd`, `xxd`)
* Inferring the format of binary files.

When sitting down to play through Gran Turismo 2 with a young child I faced a conflict. I wanted to field frequent requests to purchase and race new cars while not dedicating play time to grind for credits (together or on my own). Despite owning the physical game and console(s) capable of playing it - I prefer emulating to use of the ability to save anywhere and fast forward. Playing on a emulator also raised the possibility of accessing and modifying save states. Thus began a detour into the feasibility of editing the GT2 save files.

Challenge 1 : Where are save files? 
-----
In my case I was running on Mac OS X using OpenEmu, which under the hood is running Playstation via Mednafen. Checking “Library/Application Support/OpenEmu/Mednafen/Battery Saves” we can find save states for this particular back-end.

Challenge 2 : Where is the number of credits encoded in the files?
-----
Plan of attack - generate 3 different save states
* base save : `gt2_base.mcr`
* base save after buying hubcap : `gt2_less_1.mcr`
* base save after buying car : `gt2_less_2.mcr`

We then want to compare the data in these 3 files to isolate which bytes encode `credits`. A quick Google reveals `cmp` to be a useful tool for a binary diff.

Nice way to diff binary files to figure out what bytes do what in a binary file

```
cmp -l gt2_base.mcr gt2_less_1.mcr > diff_1
cmp -l gt2_base.mcr gt2_less_2.mcr > diff_2
```

For each diff we get an output of the bytes that are different with (byte number, value in octal for file_1, value in octal for file_2) - for example
```  
 37961   0 230  
 37962   0  10  
 37963   0 166 
 37964   0  35 
 37965   0  64 
 37970   0   1 
 37973   0 202

 40585 121 315
 40586  32 321 
 40587   7   6 
 40589 123 124
 40605 323 126
 40606 316 223
 40607  20 303
 40608 215  40 
```

The following bytes were common between `diff_1` and `diff_2`

```
40585
40586
40587
40605
40606
40607
40608
```

Some or all of these bytes must be the `credits` . This is an awful lot of bytes to store the `credits` , but we’ll see what happens.
With hindsight `cmp` is 1 indexed, so 0 indexed the relevant bytes are (40584, 40585, 40586, 40604, 40605, 40606, 40607) 

Challenge 3 :  Changing the bytes
-----

A quick python utility for changing byte in a file.
```
#!/usr/bin/env python3

import sys

fileName = sys.argv[1]
offset = int(sys.argv[2], 0)
byte = int(sys.argv[3], 0)

with open(fileName, “r+b”) as fh:
    fh.seek(offset)
    fh.write(bytes([byte]))
```

We can use this to modify bytes in our save.

```
python3 byte_change.py gt2_base.mcr 40584 255
```

Ok we changed the value - let’s put this data back in the appropriate directory with the appropriate name and see if it loads. 

```
Error
```

Challenge 4 : Invalid Save State
-----

A few possibilities come to mind
* The resulting `credit` amount was invalid : Possible - worth checking, but even smaller changes to these bytes results in `error`.
* There is some redundant encoding of `credits`   : Would be weird.
* More likely : There is some error correction on the save file.

A search for information on Gran Turismo 2 saves does reveal a page mentioning a `CRC32` [Cyclic redundancy check - Wikipedia](https://en.wikipedia.org/wiki/Cyclic_redundancy_check) at the end of the file.

Inspecting the data with `xxd` - a great tool for inspecting binary data.

```
xxd gt2_base 
```

Which gives output like …

```
000053e0: 462a ffff bc60 0000 2837 0000 ffff ffff  F*...`..(7......
000053f0: ffff ffff 652a ffff 4144 4800 0000 0000  ....e*..ADH.....
00005400: 0000 0000 4144 4800 0000 0000 0000 0000  ....ADH.........
00005410: 4144 4800 0000 0000 0000 0000 4144 4800  ADH.........ADH.
00005420: 0000 0000 0000 0000 4144 4800 0000 0000  ........ADH.....
00005430: 0000 0000 0004 0000 4b5d 0000 db34 0000  ........K]...4..
00005440: ffff ffff ffff ffff 802b ffff 015e 0000  .........+...^..
00005450: 7d35 0000 ffff ffff ffff ffff 6b2b ffff  }5..........k+..
00005460: 225e 0000 ba35 0000 ffff ffff ffff ffff  "^...5..........
00005470: e42a ffff 5d5e 0000 4035 0000 ffff ffff  .*..]^..@5......
```

Scrolling down to 40604 -> 00009e96 we can clearly see that the bytes 40604 to 40607 are the final non-zero bytes in the file, so are a natural candidate.

```
dd skip=40604 count=4 if=gt2_base.mcr of=gt2_crc bs=1 
```

For the particular save we find :

`ef63 776c `

Lets try!

```
> dd skip=0 count=40604 if=gt2_base.mcr of=gt2_data bs=1
> crc32 gt2_data 
890a3d26
```

Hm that has nothing to in common with the bytes. It is curious though how much of the save file is empty - leading to realization that this save represents an entire playstation memory card and it is possible that not all the first 40604 bytes are for GT2. A memory card had 1Mb or 128 kilobyte of storage  ([[Sony Playstation Memory Card - HwB](http://www.hardwarebook.info/Sony_Playstation_Memory_Card)]) with 15 `blocks`  and a GT2 took up 4 blocks. Each block then was likely 8 kilobytes or 8092 bytes. We have a total of 40604 bytes an extra 8092 over the expected 4*8092. So perhaps the memory card has an extra file

```
> dd skip=8092 count=32412 if=gt2_base.mcr of=gt2_data bs=1
> crc32 gt2_data 

32412+0 records in
32412+0 records out
32412 bytes transferred in 0.333104 secs (97303 bytes/sec)
6c7763ef
```

Oh! This is the CRC we expected, but flipped! 

```
6c7763ef -> ef63776c
```

To put everything together we need to get the output of `crc32` as bytes, reverse it, and overwrite
the crc bytes in the modified safe file. `xxd` is also helpful for converting back to binary - piping the
hex output of `crc32` to `xxd` with the flags `-p -r` will convert the hex to binary. (From `man xxd : 
"reverse operation: convert (or patch) hexdump into binary.  If not writing to stdout, xxd writes into
its output file without truncating it. Use the combination -r -p to read plain hexadecimal dumps  with-
out  line  number  information  and without a particular column layout. Additional Whitespace and line-
breaks are allowed anywhere.)"

```
crc32 gt2_data | xxd -p -r > gt2_crc
```

Inverting the bytes in the `gt2_crc` file using minimal new tools

* Read `gt2_crc` with `xxd` using `-c1` to place one byte per line.
* Pipe in `tac` to reverse lines
* `xxd` to convert back to binary.

```
< gt2_crc xxd -p -c1 | tac | xxd -p -r > gt2_crc_invert
```

All together

```
gt2_save=<path_to_save>
# Store off bytes we want to write into the save
echo ffffff0a | xxd -p -r > new_bytes
# Use dd to overwrite bytes in gt2_save at specific offset.
dd if=new_bytes bs=1 seek=40584 of=gt2_save conv=notrunc
# Calculate the new CRC
dd skip=8192 count=32412 if=gt2_save of=gt2_data bs=1
# Write out as binary
crc32 gt2_data | xxd -p -r > gt2_crc
# Invert those bytes
< gt2_crc xxd -p -c1 | tac | xxd -p -r > gt2_crc_invert
# Overwrite the original crc with those bytes
dd if=gt2_crc_invert bs=1 seek=40604 of=gt2_save conv=notrunc
```

Result is a valid save file with an absurd amount of credit,
a more enjoyable GT2 experience for all, and new experience
manipulating binary data.
