# Summaries

These are the TeX files of my summaries published [here](https://fabian.damken.net/summaries).

If you found any issues, having suggestions, etc., please [create an issue](https://github.com/fdamken/summaries/issues/new).

## How to Build
Add the pkg content to yout TeX-Path (see [pkg](pkg/README.md))
### Using the build script
- navigate a terminal to the folder of a summary you want to compile
- Execute the [compile-summary](bin/compile-summary) script
- If you want to enable dark-Mode, set `DARK_MODE=1` before executing the script  

Example:
```sh
summary_root=$PWD
cd summaries/cs/mandatory/fs4/cnuvs  
DARK_MODE=1 $summary_root/bin/compile-summary
```
