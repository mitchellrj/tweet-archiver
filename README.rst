Tweet Archiver
==============

Based on the code and example given by Alex Muller on his blog_.

.. _blog: http://alex.mullr.net/blog/2012/08/twitter-tweet-nest-dpa/

Usage
-----

 1. Install the egg.
    
 2. Run the tweet-archiver script now found in your Python's bin
    directory like so::

      ./bin/tweet-archiver infile.txt outfile.json

    replacing infile.txt with the path to the USERNAME-tweets.txt
    file sent to you by Twitter and outfile.json with the path to
    the JSON file in which you want to collate the tweet data.
    
 3. The script will ask for your username and password. This is not
    stored anywhere and is only used for API access.
