"""This python script holds the website generator formats."""

import re

"""This script is kind of hacky and not completely generalized
Some things I should change: use _repl_str to actually
keep track of the replacement params, design a new function
to construct regex., ability for parser to have blank name fields,
construct a carousel for the first page, allow for more generalized
importing of pages"""

# merely for keeping track of what string parsers are used
_repl_str = (r'{{', r'<<')


def _parse_url(parse: str):
    """Try to parse url from parse. Returns parsed string."""
    base = r'<a href="-LOC-" src="-LOC-" target="_blank">-NAME-</a>'
    name, loc = None, None
    # matches <<url>>
    if (r'<<' in parse) and (r'>>' in parse):
        regex = r"(?<=\<\<)(.*?)(?=\>\>)"
        match = re.finditer(regex, parse, re.MULTILINE)
        if match:
            loc = match.__next__().group()
            name = loc
        else:
            return parse
    # matches ||name||
    if (r'||' in parse) and (r'||' in parse):
        regex = r"(?<=\|\|)(.*?)(?=\|\|)"
        match = re.finditer(regex, parse, re.MULTILINE)
        if match:
            name = match.__next__().group()
            parse.replace(r'||' + "{}".format(name) + r'||', '')
    if not name:
        name = loc
    if name and loc:
        base = base.replace(r'-LOC-', loc).replace(r'-NAME-', name)
        return parse.replace(r'<<' + "{}".format(loc) + r'>>', base)\
            .replace(r'||' + "{}".format(name) + r'||', '')
    else:
        return parse


def _parse_images(parse: str, geometry: str = '300px x 300px'):
    """Try to parse image from parse. Returns parsed string."""
    # matches --SIZE--
    width, height = None, None

    if r'--' in parse:
        regex = r"(?<=\-\-)(.*?)(?=\-\-)"
        match = re.finditer(regex, parse, re.MULTILINE)
        if match:
            try:
                width, height = match.__next__().group().lower().split(' x ')
                parse.replace(r'--' + "{}".format(width + ' x ' + height) +
                              r'--', '')
            except:
                width, height = geometry.lower().split(' x ')
    if (not width) or (not height):
        width, height = geometry.lower().split(' x ')

    base = '</p><a href="-LOC-" target="_blank"><img src="-LOC-" ' +\
           'alt="-NAME-" width="{}" height="{}"></a><p>'.format(width, height)
    name, loc = None, None
    # matches {{image url}}
    if (r'{{' in parse) and (r'}}' in parse):
        regex = r"(?<=\{\{)(.*?)(?=\}\})"
        match = re.finditer(regex, parse, re.MULTILINE)
        if match:
            loc = match.__next__().group()
            name = loc
        else:
            return parse

    # matches [[name]]
    if (r'[[' in parse) and (r']]' in parse):
        regex = r"(?<=\[\[)(.*?)(?=\]\])"
        match = re.finditer(regex, parse, re.MULTILINE)
        if match:
            name = match.__next__().group()
            parse.replace(r'[[' + "{}".format(name) + r']]', '')
    if name and loc:
        base = base.replace(r'-LOC-', loc).replace(r'-NAME-', name)
        return parse.replace(r'{{' + "{}".format(loc) + r'}}', base)\
                    .replace(r'[[' + "{}".format(name) + r']]', '')\
                    .replace(r'--' + "{}".format(width + ' x ' + height) +
                             r'--', '')
    else:
        return parse


def _std_section(sec_content: dict, geometry: str = '300px x 300px'):
    """Construct the standard sections used in `#main`."""
    """Careful,there is an infinite loop in here that can get stuck."""

    toreturn = []

    section_base = '<h3>-SEC-</h3>'

    content_base = '<p>-CON-<p>'

    for i, section in enumerate(sec_content):
        # build section title with section
        # build section content with sec_content[section]
        raw_content = sec_content[section]
        parsed = raw_content
        count = 0
        while any(_repl in parsed for _repl in _repl_str) and (count < 1000):
            count += 1
            parsed = _parse_url(_parse_images(parsed, geometry))

        if count >= 1000:
            parsed = raw_content
            print('There was an error in parsing your script.')
            import datetime
            with open('gen_website.' +
                      str(datetime.datetime.now()) + '.log', 'a') as l:
                l.write('Tried: ' + str(count) + ' times...')
                l.write('Error parsing:\n<' + raw_content + '>')
                l.write('\nTo:\n<' + parsed + '>')

        _tmp_s = section_base.replace(r'-SEC-', section) + '\n'
        _tmp_c = content_base.replace(r'-CON-', parsed) + '\n'
        toreturn.append(_tmp_s + _tmp_c)

    return ''.join(toreturn)

# end of file
