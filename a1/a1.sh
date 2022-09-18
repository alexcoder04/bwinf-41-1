#!/bin/sh

echo "-------------------------------------------------"
for file in $(ls "./material/Aufgabe1/stoerung"*".txt"); do
    echo "Matches for '${file##*/}':"
    cat "./material/Aufgabe1/Alice_im_Wunderland.txt" \
        | tr "\\n" " " \
        | tr '[:upper:]' '[:lower:]' \
        | sed -e 's/[[:space:]]\+/ /g; s/[^(a-zäöüß )]//g;' \
        | grep -Eo "$(sed 's/_/\\S+/g' "$file")" \
        | uniq
    echo "-------------------------------------------------"
done
