# ntz-py
ntz is a commandline notes taker

## What is ntz?

A command line note tool that doesn't involve terminal based editors, and does involve python and (SQLite or YAML).
Your choice.

This lab requires you to figure out how to take things from the command line and manipulate a SQLite3 database to
store text notes.

## Why?

Keeping track of a small list of things to remember or stuff that needs doing is a pain. 
Remembering its location, manually accessing it, formatting it and all of the clicking that entails, 
is something many find unpleasant.

Other command line note tools out there are...clunky. 
They require interacting with vim or nano, and manual formatting. 
Yuck

ntz takes command line arguments and builds tidy todo/remember lists using the inherent 
neatness of SQLite (or YAML) and a little python magic. 
The result is a notes system that is easily manipulated both in the command line 
using ntz' interface, or manually in the SQLite database (or YAML file).

## What's it look like?

ntz has four commands.
* [r]emember
 * [-c] creates or appends to a category
* [f]orget a note
* [e]dit a note
* clear

## Installation (Once you have it written)
1. Grab ntz.py
2. Place it somewhere that's in your bash's $PATH. Either /bin, /usr/bin or ~/bin
3. Add this line to your .bashrc alias section (which is probably in ~/) -> alias ntz='ntz.py'

ntz should use python3.x and pysqlite OR PyYAML.
That's your choice.

That should do it. To make ntx executable in a shell, just `chmod +x ntz.py` and it'll probably do the trick.

## Usage

### Showing notes.
Typing `ntz` with no arguments should display all your notes. (Can you figure out how to send them to `more` or 
`less` so you can see them one screen at a time?)

