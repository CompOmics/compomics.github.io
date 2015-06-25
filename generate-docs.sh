#!/bin/bash

echo "building project page"

project_name=$1
readme=$2
wiki=$3
api=$4

github_page="${wiki%."wiki.git"}"

project_filename="${project_name/ /_}"
project_filename=${project_filename,,}

description="$(curl -s $api | /bin/jq -r '.description')"

header="---\nname: \"$project_name\"\ngithub_project: \"$github_page\"\ndescription: \"$description\"\n---\n"

# sort out project filename

echo -e "$header" > "compomics-site/_projects/$project_filename.md"
echo "$(curl -s $readme | python wiki-url-sub.py)" >> "compomics-site/_projects/$project_filename.md"

rm -rf temp_wiki

git clone $wiki temp_wiki

echo "building wiki"

directory="compomics-site/$project_filename/_posts"
rm -rf $directory
mkdir -p $directory

for filename in temp_wiki/*.md; do
	page_name="$(basename $filename .md)"
	page_name=${page_name,,}

	header="---\nname: ${page_name^}\nproject: $project_name\nlayout: default\npermalink: /$project_name/wiki/$page_name.html\ngithub_project: $github_page\n---\n"

	echo -e "$header" > "$directory/$(date +%F)-$page_name.md"
	echo -e "$(cat -s $filename | python wiki-url-sub.py)" >> "$directory/$(date +%F)-$page_name.md"
done

rm -rf temp_wiki

# git it
cd compomics-site
git add .
git commit -m "updated $project_name project"
git push origin master -f