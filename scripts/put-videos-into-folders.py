import os

# directory = os.path.join('D:', 'OneDrive - Office', 'JAVs')
directory = os.path.join('F:', 'Media', 'JAVs-VR')
for filename in os.listdir(directory):
    if os.path.isfile(os.path.join(directory, filename)):
        name = os.path.splitext(filename)[0]
        if name[-1].isalpha() and name[-2] == '-':
            name = name[:-2]
        try:
            os.mkdir(os.path.join(directory, name))
        except WindowsError:
            print '> path {} exists'.format(name)
        os.rename(os.path.join(directory, filename), os.path.join(directory, name, filename))
        print filename

