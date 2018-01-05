def grep(pattern, files, flags=''):
    print_line_numbers = '-n' in flags
    print_matching_filename_only = '-l' in flags
    case_insensitive = '-i' in flags
    invert_match = '-v' in flags
    match_entire_line = '-x' in flags
    greport = ''
    if case_insensitive:
        pattern = pattern.lower()
    for file in files:
        with open(file) as f:
            line_ct = 0
            for line in f:
                line_ct += 1
                target = line.strip()
                if case_insensitive:
                    target = target.lower()
                match = pattern in target
                if match_entire_line:
                    match = pattern == target
                if invert_match:
                    match = not match
                if match:
                    if print_matching_filename_only:
                        greport += file + '\n'
                        break
                    else:
                        if len(files) > 1:
                            greport += f'{file}:'
                        if print_line_numbers:
                            greport += f'{line_ct}:'
                        greport += line.strip() + '\n'
    return greport