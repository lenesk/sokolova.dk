import sys

from markdown import markdown


for file in sys.argv[1:]:
    new_file = file.rstrip('.md') + '.html'
    print '%s -> %s' % (file, new_file)
    html = markdown(open(file).read())
    open(new_file, 'w').write(html.encode('utf8'))
