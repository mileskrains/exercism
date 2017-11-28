def handshake(number):
    if type(number)==int:
        number = bin(number)[2:]
    try:
        as_int = int(number, 2)
    except ValueError:
        return []
    if not 1 <= as_int <= 31:
        return []
    sh_mask = [bd=='1' for bd in number.rjust(5, '0')]
    reverse = sh_mask.pop(0)
    sh_steps = ['jump', 'close your eyes', 'double blink', 'wink']
    actions = [a for a, b in zip(sh_steps, sh_mask) if b]
    if not reverse:
        actions.reverse()
    return actions


def code(secret_code):
    sh_step_vals = {'jump': 8, 'close your eyes': 4, 'double blink': 2, 'wink': 1}
    action_vals = [sh_step_vals.get(step, 0) for step in secret_code]
    if 0 in action_vals:
        return '0'
    sh_int = sum(action_vals)
    if action_vals != sorted(action_vals):
        sh_int += 16
    return bin(sh_int)[2:]
