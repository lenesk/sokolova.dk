import sys

from markdown import markdown


template = open('TEMPLATE.html').read()

for file in sys.argv[1:]:
    new_file = file.rstrip('.md') + '.html'
    print '%s -> %s' % (file, new_file)
    html = markdown(open(file).read())
    html = template.replace('{{body}}', html)
    open(new_file, 'w').write(html.encode('utf8'))
