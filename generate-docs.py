#!/usr/bin/env python

import sys
import re
import shutil
import os
import datetime
import getpass

import requests


def url_sub(matches):
    url = matches.group(1).lower()

    if url.endswith('wiki'):
        return 'projects' + url + '/home.html)'
    else:
        return 'projects' + url + '.html)'

if __name__ == "__main__":
    sys.stdout.write('user: ' + getpass.getuser() + '\n')
    sys.stdout.write('Building documentation\n')

    # required arguments: project name, full link to git repo (include .git)
    project_name, git_repo = sys.argv[1:3]

    github_page = git_repo[:len(git_repo) - 4]
    readme = github_page.replace(
        'github.com',
        'raw.githubusercontent.com'
    ) + '/master/README.md'
    wiki = github_page + '.wiki.git'
    api = github_page.replace(
        'github.com',
        'api.github.com/repos'
    )

    project_filename = ''.join(x for x in project_name if x.isalnum() or x in ["-", "_", "."]).lower()

    header = """---
name: "{0}"
github_project: "{1}"
description: "{2}"
wiki: "{3}"
---

""".format(project_name, github_page, requests.get(api).json()['description'], project_filename)

    with open('_projects/' + project_filename + '.md', 'w+') as main_page:
        main_page.write(header)
        main_page.write(re.sub(
            'https:\/\/github\.com\/compomics([^.]*)\)',
            url_sub,
            requests.get(readme).content)
        )

    sys.stdout.write('Building wiki\n')

    if os.path.isdir('temp_wiki'):
        shutil.rmtree('temp_wiki')

    if os.system('git ls-remote ' + wiki) == 0:
        os.system('git clone ' + wiki + ' temp_wiki')

        directory = project_filename + '/_posts/'

        if os.path.isdir(directory):
            for old_file in os.listdir(directory):
                os.remove(directory + '/' + old_file)
        else:
            os.makedirs(directory)

        for wiki_file in os.listdir('temp_wiki'):
            if not os.path.isdir('temp_wiki/' + wiki_file) and wiki_file.endswith('.md'):
                page_name = ''.join(
                    x for x in os.path.splitext(wiki_file)[0] if x.isalnum()
                )
                permalink = '/projects/{0}/wiki/{1}.html'.format(project_name, page_name).lower()
                filename = '{0}{1}-{2}.md'.format(
                    directory, 
                    datetime.datetime.today().strftime('%Y-%m-%d'), 
                    page_name
                ).lower()

                header = """---
name: {0}
project: {1}
layout: default
permalink: {2}
github_project: {3}
---

""".format(page_name, project_filename, permalink, github_page)

                content = ''

                with open('temp_wiki/' + wiki_file, 'r') as this_file:
                    # fix wiki links
                    content = re.sub(
                        'https:\/\/github\.com\/compomics([^.]*)\)',
                        url_sub,
                        this_file.read()
                    )

                with open(filename, 'w+') as wiki_page:
                    print(header)
                    wiki_page.write(header)
                    wiki_page.write(content)

        shutil.rmtree('temp_wiki')
    else:
        sys.stdout.write('Project has no wiki\n')

    os.system('git add .')
    os.system('git commit -m "updated %s project"' % project_name)
    os.system('git push origin master -f -q')
