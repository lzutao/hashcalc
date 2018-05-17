# hashcalc

Print MD5 (128-bit) or SHA1 (160-bit) checksum.

## Dependencies
hashcalc currently needs following libraries:
- python2 (>= 2.7) or python3 (>= 3.5)
- python future
- python six

On Ubuntu 16.04 you can easily install them like this:
```bash
sudo apt-get update
sudo apt-get install python{,3}-{future,six}
```

## Usage

The latest version can be downloaded via GitHub.
```bash
git clone https://github.com/lzutao/hashcalc --depth 1
cd hashcalc
```

To print MD5 checksum from stdin:
```bash
echo input | python main.py
```

To print MD5 checksum from file:
```bash
python main.py <inputfile>
```

If input is encoded in hex:
```bash
echo CAFEBABE | python main.py -x
```

Add `-m sha1` to get SHA1 checksum in above examples. Example:
```bash
echo CAFEBABE | python main.py -x -m sha1
```
to print SHA1 checksum where input from stdin and encoded in hex.

## License
Licensed under [MIT](COPYING).

## TODO

Read more in [TODO](https://github.com/lzutao/hashcalc/projects) at GitHub's Projects.

[how-to-clone]: https://help.github.com/articles/cloning-a-repository/
[release]: https://github.com/lzutao/hashcalc/releases
