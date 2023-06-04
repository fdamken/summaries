for f in tmp-*.pdf; do
    convert -density 400 -colorspace RGB -channel RGB -negate -modulate 100,100,200 "$f" "$(basename "$f" .pdf)-dark.pdf"
done
