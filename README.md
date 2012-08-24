= get-dropbox-gallery
Download the images from a public Dropbox gallery you got a link for

== What it is about

I like Dropbox a lot. Lovely service with nice support for Linux based systems. Great software is software that just works and gets out of your way. Well done, you Dropbox guys!

The one problem quite many of my non-geek contacts have is what is the difference between making a gallery and sharing a folder. The latter has many advantages the most important one being that I can save the images as well. Not only as a backup for me, but also for them ;-). 

== Making things work
In Ubuntu Precise Pangolin (12.04) you install python3 and BeautifulSoup4 like so:
    sudo apt-get install python3 python3-bs4

Then get the current version of the code either via Git (if you know Git, you'll know your way) or in a terminal window:
    wget 
    chmod +x get-dropbox-gallery.py


If you have a gallery link, you can save the images contained in the gallery by issuing this command:
    ./get-dropbox-gallery.py -l https://www.dropbox.com/sh/9ilicasuj/0lpasdbZWlX#/ -o testfolder

== Future
* allow multiple downloads in parallel
* progress indicator (something like "downloaded 2 of 10 images")
* find and download sub-galleries

Feel free to try implementing those and send me a pull request!

