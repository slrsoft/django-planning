from django.db.models import signals

_colors = """Cyan  
Blue  
Orange  
Magenta  
Brown  
Green  
Fuchsia  
Purple  
Red  
Violet  
AliceBlue  
AntiqueWhite  
Aqua  
Aquamarine  
Azure  
Beige  
Bisque  
Black  
BlanchedAlmond  
BlueViolet  
BurlyWood  
CadetBlue  
Chartreuse  
Chocolate  
Coral  
CornflowerBlue  
Cornsilk  
Crimson  
DarkBlue  
DarkCyan  
DarkGoldenRod  
DarkGray  
DarkGreen  
DarkKhaki  
DarkMagenta  
DarkOliveGreen  
Darkorange  
DarkOrchid  
DarkRed  
DarkSalmon  
DarkSeaGreen  
DarkSlateBlue  
DarkSlateGray  
DarkTurquoise  
DarkViolet  
DeepPink  
DeepSkyBlue  
DimGray  
DodgerBlue  
FireBrick  
FloralWhite  
ForestGreen  
Gainsboro  
GhostWhite  
Gold  
GoldenRod  
Gray  
GreenYellow  
HoneyDew  
HotPink  
IndianRed   
Indigo   
Ivory  
Khaki  
Lavender  
LavenderBlush  
LawnGreen  
LemonChiffon  
LightBlue  
LightCoral  
LightCyan  
LightGoldenRodYellow  
LightGrey  
LightGreen  
LightPink  
LightSalmon  
LightSeaGreen  
LightSkyBlue  
LightSlateGray  
LightSteelBlue  
LightYellow  
Lime  
LimeGreen  
Linen  
Maroon  
MediumAquaMarine  
MediumBlue  
MediumOrchid  
MediumPurple  
MediumSeaGreen  
MediumSlateBlue  
MediumSpringGreen  
MediumTurquoise  
MediumVioletRed  
MidnightBlue  
MintCream  
MistyRose  
Moccasin  
NavajoWhite  
Navy  
OldLace  
Olive  
OliveDrab  
OrangeRed  
Orchid  
PaleGoldenRod  
PaleGreen  
PaleTurquoise  
PaleVioletRed  
PapayaWhip  
PeachPuff  
Peru  
Pink  
Plum  
PowderBlue  
RosyBrown  
RoyalBlue  
SaddleBrown  
Salmon  
SandyBrown  
SeaGreen  
SeaShell  
Sienna  
Silver  
SkyBlue  
SlateBlue  
SlateGray  
Snow  
SpringGreen  
SteelBlue  
Tan  
Teal  
Thistle  
Tomato  
Turquoise  
Wheat  
White  
WhiteSmoke  
Yellow  
YellowGreen"""

def build_colors(sender, **kwargs):
    try:
        sender.POST_SYNC_CREATE_COLORS
    except Exception:
        return
    
    print "rebuild colors ..."
    print " delete color-name:*"
    sender.Param.objects.filter(name__startswith='color-name:').delete()
    for name in _colors.splitlines():
        name = name.strip()
        try:
            p, created = sender.Param.objects.get_or_create(name='color-name:%s' % name, value=name)
            if created:
                print " %s created" % name
        except Exception:
            pass
    print "colors created."

signals.post_syncdb.connect(build_colors)
