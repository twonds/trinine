trinine
=======

A tool to convert numbers from a phone key pad into suggested words.


Run it
------

```
make run
```

This will prebuild a data module for finding frequently used words.
It will then run unit tests. Finally, it will run the tool expecting
user input of a string of numbers.

You can also run it on the command line by sending numbers via stdin

```
make
 echo "4663"|.venv/bin/python ./trinine/t9.py ./data/
home
good
gone
hood
hoof
homepage
homes
goods
immediately
immediate
```

Run tests
---------

```
make check
```


Training
--------

Uses n-gram frequency words for training located at the following URL:

https://github.com/first20hours/google-10000-english

