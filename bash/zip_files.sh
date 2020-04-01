# zip all folders present in given directory

for file in $1/*; do
	zip -r "$file.zip" "$file"
done
