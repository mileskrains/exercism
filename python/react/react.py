class Cell(object):
    def __init__(self):
        self.watchers = []
        self.value = None

    def set_value(self, value):
        if value == self.value:
            return
        self.value = value
        for w in self.watchers:
            if type(w) == tuple:
                cc, dependencies, updater_callback = w
                args = [c.value for c in dependencies]
                cc.set_value(updater_callback(args))
            else:
                w(self, self.value)

    def add_watcher(self, watcher_callback):
        if watcher_callback not in self.watchers:
            self.watchers.append(watcher_callback)

    def remove_watcher(self, watcher_callback):
        if watcher_callback in self.watchers:
            self.watchers.remove(watcher_callback)


class Reactor(object):
    def create_input_cell(self, value):
        ic = Cell()
        ic.set_value(value)
        return ic

    def create_compute_cell(self, dependencies, updater_callback):
        cc = Cell()
        for dep in dependencies:
            dep.add_watcher((cc, dependencies, updater_callback))
        args = [c.value for c in dependencies]
        cc.value = updater_callback(args)
        return cc