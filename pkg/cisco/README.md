# Cisco Graphics
These Graphics were inverted with the following bash script:
```sh
for f in *.eps; do    
    convert -density 1000 -colorspace RGB -channel RGB -negate "$f" "$(basename "$f" .eps)-inverted.eps"
done
for f in *-eps-converted-to.pdf; do    
    convert -density 1000 -colorspace RGB -channel RGB -negate "$f" "$(basename "$f" -eps-converted-to.pdf)-inverted-eps-converted-to.pdf"
done
```
