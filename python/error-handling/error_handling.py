def handle_error_by_throwing_exception():
    raise Exception('somthing is wrong')


def handle_error_by_returning_none(input_data):
    try:
        return int(input_data)
    except:
        return None


def handle_error_by_returning_tuple(input_data):
    try:
        return True, int(input_data)
    except:
        return False, None


def filelike_objects_are_closed_on_exception(filelike_object):
    try:
        filelike_object.do_something()
    except:
        raise
    finally:
        filelike_object.close()

