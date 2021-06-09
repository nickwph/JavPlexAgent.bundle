import os

directory = os.path.join('D:', 'OneDrive - Office', 'JAVs')
for filename in os.listdir(directory):
    if os.path.isfile(os.path.join(directory, filename)):
        name = os.path.splitext(filename)[0]
        try:
            os.mkdir(os.path.join(directory, name))
        except WindowsError:
            print '> path {} exists'.format(name)
        os.rename(os.path.join(directory, filename), os.path.join(directory, name, filename))
        print filename

