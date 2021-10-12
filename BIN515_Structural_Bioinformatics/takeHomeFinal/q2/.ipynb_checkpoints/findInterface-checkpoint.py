table = []
with open("3HIZ.pdb.txt") as tb:              
     for l in tb:
         if l.startswith("<td><pre>"):
             l = l.strip()
             l = l.replace("<td><pre>","")
             l = l.replace("</pre></td>","")
             l = l.split()
             if len(l) > 0 and l[0].startswith("--"):
                 break
             table.append(l)

