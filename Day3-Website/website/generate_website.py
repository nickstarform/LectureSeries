"""This file generates a static website."""

import os
import re


def _replace(al, inst_reg, inst_str, repl):
    if type(inst_reg) != tuple:
        for i, line in enumerate(al):
            if inst_str in line:
                al[i] = re.sub(inst_reg, repl, line)
    else:
        for i, line in enumerate(al):
            for j in range(len(inst_reg)):
                if inst_str[j] in line:
                    al[i] = re.sub(inst_reg[j], repl[j], line)


def _append(al, repl, loc):
    count = 0
    for i, line in enumerate(al):
        if loc in line:
            if count < i:
                count = i
    al[count] = al[count].replace(loc, loc + '\n  ' + repl + '\n')
    return al


def _fmt(inst):
    """Take string inst, split _ and capitalize every word."""
    raw = inst
    splitted = raw.split('_')
    for i, word in enumerate(splitted):
        splitted[i] = word[0].upper() + word[1:]
    return ' '.join(splitted)

if __name__ == '__main__':

    try:
        import config as c
    except ModuleNotFoundError as e:
        print('Please fill out the configuration file and give it' +
              ' the name `config.py`.')
        exit()
    try:
        import webformat as wf
    except ModuleNotFoundError as e:
        print('Must run this in the default directory when git pulled.')
        exit()

    src = './src/'
    dest = './build/'

    if not os.path.isdir(dest):
        os.mkdir(dest)
    else:
        os.system('rm -f ' + dest + '/*')

    count = 0
    for dirname, dirnames, filenames in os.walk(src):
        if count == 0:  # gets first level of subdirs
            for subdirs in dirnames:
                os.symlink('.' + src + subdirs, dest + subdirs)
        count += 1

    print('Will generate these pages: ',
          [x + '.html' for x in c.pages if c.pages[x]])

    for file in ['research.html', 'teaching.html', 'projects.html',
                 'header.html', 'contact.html', 'index.html', 'banner.html',
                 'about_me.html']:

        with open(src + file, 'r') as f:
            al = f.readlines()

        # no better way I can see.
        # Go through each file and replace needed times
        if 'header' in file:
            _replace(al,
                     (r'(\$EMAIL\$)', r'(\$PFP\$)',
                      r'(\$CV\$)', r'(\$GROUP\$)'),
                     ('$EMAIL$', '$PFP$', '$CV$', '$GROUP$'),
                     (c.gs_name[1], c.gs_pict, c.cv, c.group))
            if c.phone:
                base = r'<li><p>Phone: $PHONE$</p></li>'
                repl = base.replace(r'$PHONE$', c.phone)
                _append(al, repl, r'<!-- Contact -->')
            if c.advisor:
                base = r"<li><p>Advisor: <a href='$ADVW$' " +\
                    r"target='_blank'>$ADVN$</a></p></li>"
                repl = base.replace(r'$ADVN$', c.advisor[0])\
                           .replace(r'$ADVW$', c.advisor[1])
                _append(al, repl, r'<!-- Contact -->')
            if c.lab:
                base = r'<li><p>Lab: $LAB$</p></li>'
                repl = base.replace(r'$LAB$', c.lab)
                _append(al, repl, r'<!-- Contact -->')
            if c.office:
                base = r'<li><p>Office: $OFFICE$</p></li>'
                repl = base.replace(r'$OFFICE$', c.office)
                _append(al, repl, r'<!-- Contact -->')
            for page in c.pages:
                if c.pages[page] and (page.lower() not in ('home', 'index')):
                    base = "<li><a href='./{}.html'>{}</a></li>"\
                        .format(page, _fmt(page))
                    _append(al, base, r'<!-- Pages -->')

        elif 'contact' in file:
            _tmp = wf._std_section(c.pages['contact'], '100px x 100px')
            _replace(al, r'(\$CONTACT\$)', '$CONTACT$', _tmp)
        elif 'about_me' in file:
            _tmp = wf._std_section(c.pages['about_me'], '100px x 100px')
            _replace(al, r'(\$ABOUTME\$)', '$ABOUTME$', _tmp)
        elif 'banner' in file:
            _replace(al, r'(\$BANNER\$)', '$BANNER$', c.bg_banner)
        elif 'teach' in file:
            _tmp = wf._std_section(c.pages['teaching'], '100px x 100px')
            _replace(al, r'(\$TEACHING\$)', '$TEACHING$', _tmp)
        elif 'projects' in file:
            _tmp = wf._std_section(c.pages['projects'], '100px x 100px')
            _replace(al, r'(\$PROJECTS\$)', '$RESEARCH$', _tmp)
        elif 'index' in file:
            _tmp = wf._std_section(c.pages['home'], '100px x 100px')
            _replace(al, r'(\$HOME\$)', '$HOME$', _tmp)
        elif 'research' in file:
            _tmp = wf._std_section(c.pages['research'], '100px x 100px')
            _replace(al, r'(\$RESEARCH\$)', '$RESEARCH$', _tmp)

        # replace all Grad Student Name instances
        _replace(al, r'(\$GRADNAME\$)', '$GRADNAME$', c.gs_name[0])

        with open(dest + file, 'w') as f:
            for line in al:
                f.write(line)

# end of file
