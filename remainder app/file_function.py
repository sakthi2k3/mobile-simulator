def write(fname, tasks):
     with open(fname, "w") as fp:
         for x in tasks:
            fp.write("%s\n" % x)

def deleteContent(pfile):
    
        pfile.truncate()
        return pfile
    

def read(fname):
        tasks = []
        try:
            with open(fname, "r") as fp:
                t1 = fp.readlines()
                for x in t1:
                    tasks.append(x.rstrip('\n'))
        except:
            with open(fname, "w") as fp:
                fp.write("")
        return tasks
