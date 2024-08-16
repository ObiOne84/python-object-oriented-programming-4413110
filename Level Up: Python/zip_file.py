import os
from zipfile import ZipFile


def zip_all(search_dir, extension_list, output_path):
  with ZipFile(output_path, 'w') as output_zip:
    for root, _, files in os.walk(search_dir):
      rel_path = os.path.relpath(root, search_dir)
      for file in files:
        _, ext = os.path.splitext(file)
        if ext.lower() in extension_list:
          output_zip.write(os.path.join(root, file),
                            arcname=os.path.join(rel_path, file))

# for testing zip_all('my_stuff', ['.jpg', 'txt'], 'my_stuff.zip')
notes = """
My zip_all function starts by opening the output ZipFile using a context manager on line 5. On the next line, I used the OS module's walk function to explore the search directory and all of its subdirectories. As it walks through the folder tree, it yields a three element tuple. The first element, named root, will be the path to a directory. The second element is a list of all these subdirectories within that root directory, and since I don't need that for my function, I capture it with an underscore to indicate that it's an unused variable. The third element is a list of all the files in the root directory. I need to maintain the relative folder structure for the files in the output archive, but if the users call these zip_all function using an absolute path, the root path I get from the walk function will also be absolute. So on line 7, I use the OS path.relpath function to convert root into a relative path compared to the search directory, which I'll need later when building the archive. The next line uses another for loop to iterate through all the files in each directory and then split them apart using the os.path.splittext function to separate the file name from its extension. If the extension matches one of the items in the extension list parameter, I add it to the output_zip file. The write method's first argument is the path to the original file which I rebuild using the join function on the root path and file name, and the second argument, arcname, determines how this file will be named within the ZIP archive. So I build that path using the relative path that I captured on line 7. To test my solution, I filled a folder named, my_stuff, with several images in different file formats along with the .txt file. And there's also a subdirectory named animals with even more images. Now, down in the terminal, I've already started an interactive Python shell and imported my zip_all function. So I'll call it and pass in the my_stuff folder as the search directory. I'll tell it to search for jpg and txt files, and I'll save everything it finds to my_stuff.zip. I'll run that command. And then in my working directory, I can see a newly created ZIP file which will contain all of my .jpg and .txt files organized into the same relative folders. (bells dinging) My solution is just one way to solve this challenge, and I'm curious to see different approaches, so I encourage you to leave comments and share your own
"""