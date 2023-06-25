#!/bin/sh
# this script is posix compliant, so we can use /bin/sh
# 
# a rather hacky solution written in shell

TASK_FOLDER="${TASK_FOLDER:-./material/Aufgabe1}"

echo "-------------------------------------------------"
for file in $(ls "$TASK_FOLDER/stoerung"*".txt"); do
    echo "Matches for '${file##*/}':"
    sed \
	-e '/\n/d; s/\(.*\)/\L\1/g; s/[[:space:]]\+/ /g; s/[^(a-zäöüß )]//g;' \
	"$TASK_FOLDER/Alice_im_Wunderland.txt" \
        | grep -Eo "$(sed 's/_/\\S+/g' "$file")" \
        | uniq
    echo "-------------------------------------------------"
done

