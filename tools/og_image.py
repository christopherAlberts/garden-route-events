"""Builds images/og.jpg (1200x630) for link previews: brand gradient + a collage of real Garden Route event photos."""
import json,os
from PIL import Image,ImageDraw,ImageFont,ImageFilter
H=os.path.dirname(os.path.abspath(__file__)); R=os.path.join(H,"..")
G="/usr/share/fonts/truetype/sand-box/google/"
def font(path,size,wght):
    f=ImageFont.truetype(G+path,size)
    try: f.set_variation_by_axes([min(32,size),wght] if "Inter" in path else [144,wght,0,0])
    except Exception:
        try: f.set_variation_by_name("Bold")
        except Exception: pass
    return f
W,Hh=1200,630
im=Image.new("RGB",(W,Hh))
px=im.load()
for y in range(Hh):
    for x in range(W):
        t=(x/W*0.6+y/Hh*0.4)
        a=(11,47,37); b=(29,111,122)
        px[x,y]=tuple(int(a[i]+(b[i]-a[i])*t) for i in range(3))
D=json.load(open(os.path.join(R,"data","events.json")))
pics=[e["image"] for e in D if e["garden_route"] and e["image"] and e["status"]=="scheduled"]
pref=[e["image"] for e in D if e["garden_route"] and e["image"] and e["category"] in("festival","market","concert","funrun") and e["status"]=="scheduled"]
seen=[];[seen.append(p) for p in pref+pics if p not in seen]
tiles=seen[:9]
x0,y0,ts,gap=640,40,176,10
for i,p in enumerate(tiles):
    t=Image.open(os.path.join(R,p)).convert("RGB"); s=min(t.size)
    t=t.crop(((t.width-s)//2,(t.height-s)//2,(t.width-s)//2+s,(t.height-s)//2+s)).resize((ts,ts),Image.LANCZOS)
    m=Image.new("L",(ts,ts),0); ImageDraw.Draw(m).rounded_rectangle((0,0,ts-1,ts-1),18,fill=255)
    im.paste(t,(x0+(i%3)*(ts+gap),y0+(i//3)*(ts+gap)),m)
# soft fade over collage edge
fade=Image.new("L",(W,Hh),0); fd=ImageDraw.Draw(fade)
for x in range(560,700): fd.line([(x,0),(x,Hh)],fill=int(150*(1-(x-560)/140)))
for x in range(0,560): fd.line([(x,0),(x,Hh)],fill=150)
base=Image.new("RGB",(W,Hh),(10,40,32)); im=Image.composite(base,im,fade)
d=ImageDraw.Draw(im)
d.text((60,70),"MOSSEL BAY · GEORGE · KNYSNA · PLETT",font=font("Inter/Inter-VariableFont_opsz,wght.ttf",22,600),fill=(200,230,222))
F=font("Fraunces/Fraunces-VariableFont_SOFT,WONK,opsz,wght.ttf",74,800)
d.text((58,115),"What's on",font=F,fill="white"); d.text((58,195),"along the",font=F,fill="white")
d.text((58,275),"Garden Route",font=font("Fraunces/Fraunces-Italic-VariableFont_SOFT,WONK,opsz,wght.ttf",74,700),fill=(233,196,106))
d.text((60,385),"Concerts · festivals · markets · fun runs\ntheatre · community events",font=font("Inter/Inter-VariableFont_opsz,wght.ttf",28,500),fill=(225,240,235),spacing=10)
d.text((60,500),"6 Oct 2026 – 28 Feb 2027  ·  list, calendar & map",font=font("Inter/Inter-VariableFont_opsz,wght.ttf",24,600),fill=(160,215,205))
d.rounded_rectangle((60,548,420,590),12,fill=(233,196,106)); d.text((78,556),"christopheralberts.github.io",font=font("Inter/Inter-VariableFont_opsz,wght.ttf",22,700),fill=(13,59,46))
im.save(os.path.join(R,"images","og.jpg"),"JPEG",quality=82,optimize=True,progressive=True)
print("ok",len(tiles))
