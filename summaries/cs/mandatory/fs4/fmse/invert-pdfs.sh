for f in tmp-*.pdf; do
    convert -density 1000 -colorspace RGB -channel RGB -negate "$f" "$(basename "$f" .pdf)-inverted.pdf"
done
