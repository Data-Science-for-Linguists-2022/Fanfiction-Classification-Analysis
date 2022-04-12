Progress report 1, 2/13/2022 - Github repository created, beginning markdown descriptor files committed to repository

# 1st Progress Report - 2/26/2022

I am almost finished with my data collection and cleaning process, with a few small things left to finish up. 

To collect my data, I utilized the scrapy python library and created a spider (code that can crawl webpages and download their
html). The spider I wrote can be found [here](https://github.com/Data-Science-for-Linguists-2022/Fanfiction-Classification-Analysis/blob/main/fanfic_spider.py) under the name fanfic_spider.py. Please note that it will not
do anything if you try to run it! Spiders need to be run within dedicated scrapy projects, and while I will probably share
my entire scrapy project eventually, it is currently stored in a git-ignored directory (see notes on data sharing below).
Using this spider, I collected over 6000 html pages, each representing a single page (often a chapter) of a fanfic from 
https://archiveofourown.org/. 300 of those pages are saved in a directory called data_samples in my main project, and you
are free to peruse them. I originally downloaded over 4000 pages, but after data cleaning, I realized that since I was crawling
such a huge website (Archive of Our Own contains, by my guess, several million individual works), I needed a larger sample. 
My current goal is to get 10000 html pages, but web crawling takes time, even with my spider turned up to optimize speed. It
takes several hours with the program actively running to download even 1000 html pages, let alone the 6000 I needed, so I
decided to focus on cleaning what I had for now, and collecting my final 4000 pages of data slightly later.

The cleaning process was fairly straightforward. Scrapy allows you to clean data to some extent within its program, but given
the massive scale of my data I thought it would be better to use a library dedicated to data cleaning and organizing, so I 
utilized the BeautifulSoup library. Thankfully, the html pages I downloaded were very well organized, and Archive of Our Own
has a rigorous tagging system that is built into the core of the website, which I used to search the data for categories I 
could add to the DataFrame I made using pandas. You can see my work in the Jupyter Notebook fanfiction_data_parsing.ipynb,
which can be found [here](https://github.com/Data-Science-for-Linguists-2022/Fanfiction-Classification-Analysis/blob/main/fanfiction_data_parsing.ipynb).

## Data Sharing Plan

The data I used is html code from the https://archiveofourown.org/ website. This website uses the GPL-2.0 license (or the
General Public License), which requires that data be made freely available by anyone making a project that derives from the
program (I might be a little off about this, I plan to go over the license a few more times before finializing my project). 
Therefore, by the end of this project, I plan to make available all of the data I used. However, at the moment I am not 
finished compiling my data, so I have provided samples and stored the rest in a git-ignored directory until I have everything
I need. (UPDATE: My data_samples directory won't upload to github, I'm working on it and it will be up as soon as possible.)

# Second Progress Report - 3/24/2022

My data has all been collected and cleaned, and I'm looking forward to moving on to analysis and classification! Most of what
I've done for this progress report has been organizing everything a little better and getting things in better shape, especially
my data sharing plan. UPDATE: My Jupyter Notebook may not be finished running by my final commit, I will update it as soon as
it finishes.

## Data Sharing

I finally got my data samples directory to work, and in it you will find five html pages that I collected, as well as the 
entire scrapy project I used to collect them, so you can recreate my work if you so desire. I will warn you, results may vary,
as it takes hours for the spider to run and my spider has very few restrictions on what fanfics it downloads. If you would
like to use and/or edit the code I've provided here, I highly suggest you take a look at the scrapy documentation [here](https://doc.scrapy.org/en/latest/index.html).
It's very helpful for anyone looking to use scrapy. I did think about uploading all of my data, but with slightly over 10000
files, it seemed unreasonable to expect anyone to sort through that much data when I've provided all the tools to obtain and
clean a similar sample yourself.

## License

After a lot of consideration, I decided to use the GPL 3.0 license. It's the same license my dataset uses, which makes it easy
for anyone looking to use this project in the future, and it fits with my desire to make my work available to the public, 
especially since I'm using data that I collected myself, and thus almost everything in my project is my own personal work.
I do want this work to be replicable, so the General Public License was the best option for me.

# Third Progress Report - 4/12/2022

I've finally moved on to analysis, and I'm beginning to realize my original goals may not be attainable (or at least, not 
attainable with the amount of time and effort I have available). Building a working, reasonably effective classifier on this
dataset is a lot more difficult than I was expecting, and although I will continue to put in a little more work to seeing if
I'm missing something, I think I'd like to move my focus to clustering. Seeing what groups these fanfics fall into on a larger
level would be an achievement, if not quite the same thing I was hoping to achieve when I started out. I have updated my 
Jupyter Notebook with the analysis I've been able to complete at this point in time, and gone into a little more detail on my
thoughts on next steps. Given the limited capability of my PC to run machine learning processes on this large dataset, I'm 
thinking I might have to move to the CRC and supercomputing. If so, I will be working in a separate Jupyter notebook for the
conclusion of my analysis, and I have taken appropriate measures to save the data cleaning I've done. All the work for this
progress report was done on the same Jupyter Notebook linked in Progress Report 1.

## Final Thoughts on Data

My data is in its final shareable form as of the last progress report, as samples stored in the data samples directory. Anyone
looking to replicate my project can access the spider I used to collect my data and see a small sample of the data I collected,
so I didn't feel the need to share my data in its entirety. I have carefully documented my collection and cleaning process so 
that anyone who wishes can do something similar.