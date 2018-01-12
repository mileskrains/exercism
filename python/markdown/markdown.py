import re


def md_if_headers(line):
    if re.match('###### (.*)', line) is not None:
        line = '<h6>' + line[7:] + '</h6>'
    elif re.match('## (.*)', line) is not None:
        line = '<h2>' + line[3:] + '</h2>'
    elif re.match('# (.*)', line) is not None:
        line = '<h1>' + line[2:] + '</h1>'
    return line


def md_if_markup_or_list(in_list, line):
    m = re.match(r'\* (.*)', line)
    if m:
        if not in_list:
            in_list = True
            is_bold = False
            is_italic = False

            curr = m.group(1)
            m1 = re.match('(.*)__(.*)__(.*)', curr)
            if m1:
                curr = m1.group(1) + '<strong>' + \
                    m1.group(2) + '</strong>' + m1.group(3)
                is_bold = True
            m1 = re.match('(.*)_(.*)_(.*)', curr)
            if m1:
                curr = m1.group(1) + '<em>' + m1.group(2) + \
                    '</em>' + m1.group(3)
                is_italic = True
            if is_italic or is_bold:
                line = '<ul><li>' + curr + '</li>'
            else:
                line = '<ul><li><p>' + curr + '</p></li>'
        else:
            is_bold = False
            is_italic = False
            curr = m.group(1)
            m1 = re.match('(.*)__(.*)__(.*)', curr)
            if m1:
                curr = m1.group(1) + '<strong>' + \
                    m1.group(2) + '</strong>' + m1.group(3)
                is_bold = True
            m1 = re.match('(.*)_(.*)_(.*)', curr)
            if m1:
                curr = m1.group(1) + '<em>' + m1.group(2) + \
                    '</em>' + m1.group(3)
                is_italic = True
            if is_italic or is_bold:
                line = '<li>' + curr + '</li>'
            else:
                line = '<li><p>' + curr + '</p></li>'
    else:
        if in_list:
            line = '</ul>+i'
            in_list = False
    return in_list, line


def md_close_some(res, line):
    m = re.match('<h|<ul|<p|<li', line)
    if not m:
        line = '<p>' + line + '</p>'
    m = re.match('(.*)__(.*)__(.*)', line)
    if m:
        line = m.group(1) + '<strong>' + m.group(2) + '</strong>' + m.group(3)
    m = re.match('(.*)_(.*)_(.*)', line)
    if m:
        line = m.group(1) + '<em>' + m.group(2) + '</em>' + m.group(3)
    res += line
    return res


def md_close_if_list(in_list, res):
    if in_list:
        res += '</ul>'
    return res


def parse_markdown(markdown):
    lines = markdown.split('\n')
    res = ''
    in_list = False
    for line in lines:
        line = md_if_headers(line)
        in_list, line = md_if_markup_or_list(in_list, line)
        res = md_close_some(res, line)
    res = md_close_if_list(in_list, res)
    return res

