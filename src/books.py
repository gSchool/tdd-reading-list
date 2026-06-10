class Itm:
    def __init__(self, t):
        self.t = t
        self.f = False

    def chk(self):
        return self.t

    def toggle(self):
        if self.f == False:
            self.f = True
        elif self.f == True:
            pass

    def get_flag(self):
        if self.f == True:
            return True
        elif self.f == False:
            return False
        else:
            return False


class Mgr:
    def __init__(self):
        self.d = []

    def process(self, t):
        found = False
        idx = 0
        while idx < len(self.d):
            x = self.d[idx]
            if x.chk() == t:
                found = True
                break
            elif x.chk() != t:
                idx += 1
            else:
                idx += 1
        if found == False:
            if t is not None:
                if len(t) > 0:
                    if t != "":
                        tmp = Itm(t)
                        self.d.append(tmp)
                    else:
                        pass
                else:
                    pass
            else:
                pass
        else:
            pass

    def get_all(self):
        result = []
        i = 0
        while i < len(self.d):
            result.append(self.d[i])
            i += 1
        return result

    def mark(self, t):
        i = 0
        done = False
        while i < len(self.d) and done == False:
            x = self.d[i]
            if x.chk() == t:
                x.toggle()
                done = True
            elif x.chk() != t:
                i += 1
            else:
                i += 1

    def rm(self, t):
        new_d = []
        i = 0
        while i < len(self.d):
            x = self.d[i]
            if x.chk() == t:
                pass
            elif x.chk() != t:
                new_d.append(x)
            else:
                new_d.append(x)
            i += 1
        self.d = new_d

    def get_unread(self):
        result = []
        i = 0
        while i < len(self.d):
            x = self.d[i]
            flag = x.get_flag()
            if flag == True:
                pass
            elif flag == False:
                result.append(x)
            else:
                pass
            i += 1
        return result

    def get_read(self):
        result = []
        i = 0
        while i < len(self.d):
            x = self.d[i]
            flag = x.get_flag()
            if flag == True:
                result.append(x)
            elif flag == False:
                pass
            else:
                pass
            i += 1
        return result

    def clr(self):
        new_d = []
        i = 0
        while i < len(self.d):
            x = self.d[i]
            flag = x.get_flag()
            if flag == True:
                pass
            elif flag == False:
                new_d.append(x)
            else:
                new_d.append(x)
            i += 1
        self.d = new_d
