import textwrap
import markdown
import html2text
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup

# todo: read xml file from this line 'ET.parse('here will be the file name.xml')'
mytree = ET.parse('Nuance Project.xml')
root = mytree.getroot()
total_str = ''
for data in root.findall('note'):
    content = data.find('content').text
    # print('\t' + html2text.html2text(content).strip())
    soup = BeautifulSoup(content)
    print(soup.get_text())

    content2 = html2text.html2text(content)
    content3 = '\t'.join(soup.get_text().splitlines(True))
    # content3 = textwrap.indent(content2, '    ')

    title = '##' + data.find('title').text + '\n'
    data_ins = title + content3 + '\n'
    total_str += data_ins

# todo: the below line for creating markdown files 'open('your new markdown file name will be here.md', 'a', encoding='utf-8')'
with open('demo.md', 'a', encoding='utf-8') as f:
    f.write(total_str)


# title = myroot[-1].findtext('title')# note title
# content = myroot[-1].findtext('content')# note title
# html_str_content = content.strip().split('after-white-space;">')[1].strip().split('</en-note>')[0]
# # print(html2text.html2text(html_str_content))
# with open('demo.md', 'w', encoding='utf-8') as f:
# temp = html.escape(content)
# gfg = html.unescape(temp)
# f.write(html2text.html2text(content).strip())

# markdown.markdownFromFile(input=gfg.strip(), output='demo2.md', encoding='utf-8')
