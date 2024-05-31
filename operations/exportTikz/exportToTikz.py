from math import cos, sin, radians

def export_to_tikz(self, filename):
     tikz_code = [
         "\\documentclass{standalone}",
         "\\usepackage{tikz}",
         "\\begin{document}",
         "\\begin{tikzpicture}[scale=1.5,auto=left,every node/.style={circle,fill=blue!20}]"
     ]
     
     positions = {}
     angle = 360 / self.n
     
     for i in range(self.n):
         x = 3 * cos(radians(i * angle))
         y = 3 * sin(radians(i * angle))
         positions[i] = (x, y)
         tikz_code.append(f"\\node ({i}) at ({x:.2f},{y:.2f}) {{{i}}};")
     
     for u in range(self.n):
         for v in self.adj_list[u]:
             if u < v:
                 tikz_code.append(f"\\draw ({u}) -- ({v});")
     
     tikz_code.append("\\end{tikzpicture}")
     tikz_code.append("\\end{document}")
     
     with open(f'./exportedGraphs/{filename}', 'w') as f:
         f.write("\n".join(tikz_code))
     print(f"Graph exported correctly")