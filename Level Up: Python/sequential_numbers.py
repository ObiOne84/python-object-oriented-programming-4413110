#  http://699340.youcanlearnit.net/image001.jpg
#  http://699340.youcanlearnit.net/image050.jpg


import os
import re
import urllib.parse
import urllib.request


def download_files(first_url, output_dir):
  if not os.path.isdir(output_dir):
    os.mkdir(output_dir)
  
  url_head, url_tail = os.path.split(first_url)
  first_index = re.findall(r'[0-9]+', url_tail)[-1]
  index_count, error_count = 0, 0
  while error_count < 5:
    next_index = str(int(first_index) + index_count)
    if first_index[0] == '0':  # zero padded
      next_index = '0' * (len(first_index) - len(next_index)) + next_index
    next_url = urllib.parse.urljoin(url_head, re.sub(first_index, next_index, url_tail))
    try:
      output_file = os.path.join(output_dir, os.path.basename(next_url))
      urllib.request.urlretrieve(next_url, output_file)
      print(f'Successfully downloaded {os.path.basename(next_url)}')
    except IOError:
      print(f'Could not retrivew {next_url}')
      error_count += 1
    index_count += 1

download_files('http://699340.youcanlearnit.net/image001.jpg', 'my_stuff')

notes = """
My solution uses several modules from the Python Standard Library, including the OS module
for several file path operations, the regular expression module to identify numbers within
the URL, and then the urllib.parse and request modules to manipulate the URL and retrieve
the file. Within my download_files function, lines 7 and 8, check to see if the requested
output directory exists, and if not, create it. Line 9 uses the path.split function to break
apart the input URL into the head and tail. I then use the regular expressions findall function
on that tail component to identify the last group of digits in the URL, which I'll call the
first_index. On line 11, I initialized the index_count and error_count variables to 0.
error_count is used to track how many times I try to download a file that's not available.
It's possible there could be missing files in the overall sequence, so the while loop on
line 12 will keep progressing until I encounter at least five errors due to missing files
or some other problem. The while loop begins by calculating the next_index value as the
sum of the first_index plus the index_count value. If the first_index was zero padded,
then lines 14 and 15 append the appropriate number of zeros to the front of the next_index
string. Line 16 uses the urljoin function to combine the original URL head and a modified
URL tail with the next_index value substituted into it. Now it's time to actually try
downloading that file. Line 18 generates the file path for where to save the file, and then
the URL retrieve function on line 19 downloads and saves it to to that location. If there's
an error, the program will enter the except clause where it increments the error counter.
After all that, the index_count is incremented and the while loop attempts to download
the next file. Now, down in the terminal, I've already started an interactive Python
shell and imported my download_files function. So I'll call it. I'll pass in the URL
to the first image in the test sequence and then tell it to save the files to a folder
named images. When I press Enter, I get a series of messages that it's downloading the
files until it gets past the 50th one. It tries five more files unsuccessfully, and then
it exits. (gentle bouncy music) I'll admit my function is not a perfect solution. There are
lots of URL formats that could confuse it, but for this video, I wanted to keep it short.
"""