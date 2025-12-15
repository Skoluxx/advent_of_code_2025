class Curcuit:    
    def __init__(self, jb):
        self._junction_boxes = [jb]
        jb.set_curcuit(self)

    def get_jbs(self):
        return self._junction_boxes

    def append_curcuit(self, other):
        self._junction_boxes += other.get_jbs()
        for jb in self._junction_boxes:
            jb.set_curcuit(self)

    def get_curcuit_length(self):
        return len(self._junction_boxes)

    