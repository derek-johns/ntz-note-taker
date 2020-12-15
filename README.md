# ntz-py
ntz is a commandline notes taker

## What is ntz?

A command line note tool that doesn't involve terminal based editors, and does involve python and YAML.

## Why?

Keeping track of a small list of things to remember or stuff that needs doing is a pain. 
Remembering its location, manually accessing it, formatting it and all of the clicking that entails, 
is something many find unpleasant.

Other command line note tools out there are...clunky. 
They require interacting with vim or nano, and manual formatting. 
Yuck

ntz takes command line arguments and builds tidy todo/remember lists using the inherent 
neatness of YAML and a little python magic. 
The result is a notes system that is easily manipulated both in the command line 
using ntz' interface, or manually in the YAML file.

## What's it look like?

ntz has four commands.
* [-r]emember
* [-c] creates or appends to a category
* [-f]orget a note
* [-e]dit a note
* clear
