# rl figures
These images were inverted with:
```sh
for f in *.png; do    
    convert -colorspace RGB -channel RGB -negate -modulate 100,100,200 "$f" "$(basename "$f" .png)-dark.png"
done
for f in *.pdf; do    
    convert -density 1000 -colorspace RGB -channel RGB -negate -modulate 100,100,200 "$f" "$(basename "$f" .pdf)-dark.pdf"
done
```