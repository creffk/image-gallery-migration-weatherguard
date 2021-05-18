# image-gallery-migration-weatherguard

Extract Photo Gallery Image Filepaths for Migration to New Website

I had a client that wanted us to migrate ~50 images from a webpage on his old site into a gallery on the new site we were building. The motivation for this project was instead of spending time clicking through the images to save their filepath, I wanted to write a nice little python program that would extract the URL's from the gallery on the old site for me. In principle, I would much rather spend time making a simple and useful program insetad of spending the same time on a mind numbing task.

I mostly learned the mechanics of sourcing some example code from stackoverflow discussions that looked pretty good, and then trouble shooting to modify it to work for my version of Python and the matching libraries. 

I executed the program in PyCharm. I learned how to setup pip, how to install libraries, learned that to use them in PyCharm I need to use the correct Python Interpreter, and I learned how to install librarires to my Python Interpreter.

I borrowed this example https://stackoverflow.com/questions/43982002/extract-src-attribute-from-img-tag-using-beautifulsoup, but modified it for my own use case. 

After I created my list of URL's, I pasted them into Excel, completed a Find/Replace to remove the thumbnail dimensions from the url (-230x200) so that I could have the filepath to the direct file to download and then import into media of the new site.
