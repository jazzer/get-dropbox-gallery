#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from bs4 import BeautifulSoup # sudo apt-get install python3-bs4
import sys, os, subprocess
import urllib.request
import urllib.parse


def download(link, folder):
    dowloaded_files = set()    

    # download overview site
    print('Retrieving %s' % link)
    #print(overview_page)
    soup = BeautifulSoup(urllib.request.urlopen(link))
    if debug:
        print(soup.prettify())
        with open('test.out', 'w', encoding='utf-8') as a_file:
            a_character = a_file.write(soup.prettify())
    print('Searching image links...')
    # extract the image IDs
    links = soup.find_all("a") #, { "class" : "thumbnail" })
    base_link = '/'.join(link.split('/')[:5])
    for ref_link in soup.find_all('a'):
        href = ref_link.get('href')
        if href in dowloaded_files:
            continue
        if ref_link is None or ref_link.get('href') is None:
            continue
        if not href.startswith(base_link):
            continue
        if not href.split('.')[-1].lower() in ['jpg', 'jpeg', 'png', 'gif']:
            continue
        filename = urllib.parse.unquote(href.split('/')[-1])
        print('File: %s' % filename)

        # download the image 
        target_filename = '%s/%s' % (output_folder, filename)
        if os.path.exists(target_filename):
            print('Already exists.')
            dowloaded_files.add(href)
            continue
        wget_cmd = ['wget', '%s?dl=1' % href, '-O', target_filename]
        print('Downloading...')
        p = subprocess.Popen(wget_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = p.communicate()
        #print(retcode)
        dowloaded_files.add(href)


# parse parameters
source_link = None
output_folder = None
debug = False
help_string = './get-dropbox-gallery.py --debug --link [link] --output [folder]'
i = 1
while i < len(sys.argv):
    opt = sys.argv[i]
    if opt == '--debug' or opt == '-d':
        debug = True
    elif opt == '--source' or opt == '-s' or opt == '--link' or opt == '-l':
        source_link = sys.argv[i+1]
        i += 1
    elif opt == '--output' or opt == '-o':
        output_folder = sys.argv[i+1]
        i += 1
    elif opt == '-h' or opt == '--help':
        print(help_string)
        sys.exit(0)
    else:
        print('Unknown parameter %s' % opt)
        sys.exit(1)
    i += 1

# a little error handling
if source_link is None:
    print('No link given.')
    print('Call like this: %s' % help_string)
    sys.exit(1)
if output_folder is None:
    print('No output folder set.')
    print('Call like this: %s' % help_string)
    sys.exit(2)


# show which parameters we think we got
if debug:
    print('debugging: %s' % debug)
    print('source link: %s' % source_link)
    print('output directory: %s' % output_folder)


# make output folder
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

download(source_link, output_folder)

