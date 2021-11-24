import math
import cmath
RGB=[128,0,128]
R=RGB[0]
G=RGB[1]
B=RGB[2]
def RGBtoHSV(R,G,B):
    R_prim=R/255
    G_prim=G/255
    B_prim=B/255
    Cmax=max(R_prim,G_prim,B_prim)
    Cmin=min(R_prim,G_prim,B_prim)
    delta=Cmax-Cmin
    if delta==0:
        H=0
    elif Cmax==R_prim:
        H=60*(((G_prim-B_prim)/delta)%6)
    elif Cmax==G_prim:
        H=60*(((B_prim-R_prim)/delta)+2)
    elif Cmax==B_prim:
        H=60*(((R_prim-G_prim)/delta)+4)
    if Cmax==0:
        S=0
    elif Cmax!=0:
        S=(delta/Cmax)
    V=Cmax
    return H,S,V
print(RGBtoHSV(R,G,B))