"""
Portfolio Project Thumbnails Generator
Design Philosophy: "Digital Cartography" — mapping the invisible territories of code
Each thumbnail is a window into a different digital world, rendered as a precise
cartographic artifact. UI mockups treated like scientific diagrams.
"""

from PIL import Image, ImageDraw, ImageFont
import math, os, random

FONTS = r"C:\Users\Doaa Eladly\.claude\skills\canvas-design\canvas-fonts"
OUT   = r"C:\Users\Doaa Eladly\eslam-portfolio\images"
W, H  = 800, 400

def rgb(h):
    h = h.lstrip('#')
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))

def font(name, size):
    try:    return ImageFont.truetype(os.path.join(FONTS, name), size)
    except: return ImageFont.load_default()

def gradient_bg(draw, c1, c2, w=W, h=H, mode='135'):
    r1,g1,b1 = rgb(c1); r2,g2,b2 = rgb(c2)
    for y in range(h):
        t = y / h if mode == 'v' else 0
        for x in range(w):
            if mode == '135': t = (x/w*0.4 + y/h*0.6)
            elif mode == 'h':  t = x/w
            elif mode == 'v':  pass
            else:              t = (x/w + y/h)/2
            r=int(r1+(r2-r1)*t); g=int(g1+(g2-g1)*t); b=int(b1+(b2-b1)*t)
            draw.point((x,y),(r,g,b))

def alpha_rect(img, xy, color, alpha=180):
    overlay = Image.new('RGBA', img.size, (0,0,0,0))
    d = ImageDraw.Draw(overlay)
    x0,y0,x1,y1 = xy
    d.rectangle([x0,y0,x1,y1], fill=(*rgb(color), alpha) if isinstance(color,str) else (*color,alpha))
    img.paste(Image.alpha_composite(img.convert('RGBA'), overlay).convert('RGB'), (0,0))

def rounded_rect(draw, xy, radius, fill, outline=None, width=1):
    x0,y0,x1,y1 = xy
    draw.rounded_rectangle([x0,y0,x1,y1], radius=radius, fill=fill, outline=outline, width=width)

# ─────────────────────────────────────────────────────────────────
# 1. SHO8LANA — Student Marketplace  (green)
# ─────────────────────────────────────────────────────────────────
def sho8lana():
    img = Image.new('RGB',(W,H))
    d = ImageDraw.Draw(img)
    gradient_bg(d,'#0a3d2e','#10b981')

    # Nav bar
    d.rectangle([0,0,W,52], fill=(7,46,34))
    f_bold = font('BricolageGrotesque-Bold.ttf',18)
    f_reg  = font('BricolageGrotesque-Regular.ttf',13)
    f_sm   = font('InstrumentSans-Regular.ttf',11)
    d.text((24,16),'Sho8lana', font=font('BricolageGrotesque-Bold.ttf',22), fill='#10b981')
    for i,(lbl,x) in enumerate([('Jobs',280),('Students',360),('Companies',450)]):
        d.text((x,18), lbl, font=f_reg, fill=(180,220,200))
    # Search bar
    rounded_rect(d,[550,12,770,40],8,fill=(20,80,60))
    d.text((560,18),'🔍  Search opportunities', font=f_sm, fill=(150,200,170))

    # 3 profile cards
    cards = [
        ('AY','Ahmed Yasser','React Developer','Cairo University',(16,185,129)),
        ('SF','Sara Farouk','UX Designer','AUC',(5,150,105)),
        ('MH','Mohamed Hassan','Data Analyst','GIU',(4,120,87)),
    ]
    for i,(init,name,role,univ,c) in enumerate(cards):
        x = 24 + i*258
        rounded_rect(d,[x,72,x+240,210],12,fill=(255,255,255,220) if False else (10,60,45),outline=(20,120,80),width=1)
        # Avatar circle
        d.ellipse([x+16,84,x+60,128], fill=c)
        d.text((x+28,95), init, font=font('BricolageGrotesque-Bold.ttf',20), fill='white')
        d.text((x+68,88), name, font=font('BricolageGrotesque-Bold.ttf',13), fill=(220,255,240))
        d.text((x+68,106), role, font=f_sm, fill=(100,200,160))
        d.text((x+68,122), univ, font=f_sm, fill=(80,160,130))
        # Skills pills
        for j,skill in enumerate(['React','Python','Design'][:2+i%2]):
            px = x+16+j*62
            rounded_rect(d,[px,138,px+56,154],8,fill=(16,185,129,80) if False else (20,100,70))
            d.text((px+8,140), skill, font=font('InstrumentSans-Regular.ttf',10), fill='#a7f3d0')

    # Job listings on right panel
    rounded_rect(d,[520,72,776,360],12,fill=(8,50,38))
    d.text((536,84),'Latest Opportunities', font=font('BricolageGrotesque-Bold.ttf',14), fill='#10b981')
    jobs=[('Frontend Engineer','Paymob · Cairo'),('Data Intern','Vodafone · Remote'),
          ('UI/UX Designer','SWVL · Cairo'),('Backend Dev','Instabug · Hybrid')]
    for i,(title,company) in enumerate(jobs):
        y = 110 + i*58
        d.line([536,y,760,y],fill=(20,80,60),width=1)
        rounded_rect(d,[536,y+6,556,y+22],4,fill=(16,185,129))
        d.text((560,y+8), title, font=font('BricolageGrotesque-Bold.ttf',12), fill=(220,255,240))
        d.text((560,y+24), company, font=f_sm, fill=(100,180,150))
        rounded_rect(d,[700,y+10,758,y+26],10,fill=(20,100,70))
        d.text((714,y+12),'Apply →', font=f_sm, fill='#a7f3d0')

    # Stats strip
    d.rectangle([0,330,W,H],fill=(7,46,34))
    for i,(num,lbl) in enumerate([('2.4K','Students'),('180+','Companies'),('920','Placements'),('94%','Match Rate')]):
        x = 60 + i*185
        d.text((x,340), num, font=font('BricolageGrotesque-Bold.ttf',20), fill='#10b981')
        d.text((x,364), lbl, font=f_sm, fill=(120,180,150))

    img.save(os.path.join(OUT,'sho8lana.png'))
    print('✓ sho8lana.png')

# ─────────────────────────────────────────────────────────────────
# 2. CIPHER CASE — Cyber Detective  (dark indigo)
# ─────────────────────────────────────────────────────────────────
def cipher_case():
    img = Image.new('RGB',(W,H))
    d = ImageDraw.Draw(img)
    gradient_bg(d,'#0d0b2b','#1e1b4b')
    mono = font('JetBrainsMono-Regular.ttf',11)
    mono_b = font('JetBrainsMono-Bold.ttf',13)
    title_f = font('Tektur-Regular.ttf',15)

    # Grid overlay
    for x in range(0,W,40):
        d.line([x,0,x,H],fill=(50,40,120,60) if False else (30,25,70),width=1)
    for y in range(0,H,40):
        d.line([0,y,W,y],fill=(30,25,70),width=1)

    # Terminal window left
    rounded_rect(d,[24,24,440,330],10,fill=(12,10,30))
    d.rectangle([24,24,440,52],fill=(25,20,60))
    for i,c in enumerate([(255,90,90),(255,180,50),(80,200,80)]):
        d.ellipse([36+i*20,34,48+i*20,46],fill=c)
    d.text((200,31),'cipher_terminal_v2.sh', font=title_f, fill=(130,120,200))

    # Terminal text lines
    lines = [
        ('$','decrypt --key=██████ --file=case_001.enc','#7c6fc4'),
        ('>','Analyzing cipher pattern...','#a5b4fc'),
        ('>','ROT-13 fingerprint: DETECTED','#818cf8'),
        ('!','Substitution cipher: ACTIVE','#f87171'),
        ('>','Cross-ref: █████ CONFIDENTIAL','#a5b4fc'),
        ('>','Pattern match: 73.4%','#34d399'),
        ('$','decode --method=vigenere ████████','#7c6fc4'),
        ('>','KEY RECOVERED: ████████████','#fbbf24'),
        ('>','File unlocked: confession.txt','#34d399'),
        ('■','CASE SOLVED','#a5b4fc'),
    ]
    for i,(sym,txt,col) in enumerate(lines):
        y = 62 + i*25
        d.text((36,y), sym, font=mono_b, fill=col)
        d.text((56,y), txt, font=mono, fill=col)
        if i == len(lines)-1:  # blink cursor
            d.rectangle([56+len(txt)*6.6,y,56+len(txt)*6.6+8,y+14],fill='#818cf8')

    # Cipher wheel right panel
    cx, cy, cr = 618, 185, 110
    for r in [cr, cr-22, cr-44, cr-66]:
        d.ellipse([cx-r,cy-r,cx+r,cy+r], outline=(80,60,160), width=1)
    # Tick marks on outer circle
    for i in range(26):
        angle = math.radians(i*360/26 - 90)
        x0 = cx + (cr-8)*math.cos(angle); y0 = cy + (cr-8)*math.sin(angle)
        x1 = cx + cr*math.cos(angle);      y1 = cy + cr*math.sin(angle)
        d.line([x0,y0,x1,y1], fill=(120,90,220), width=2)
        lx = cx + (cr+14)*math.cos(angle); ly = cy + (cr+14)*math.sin(angle)
        letter = chr(65+i)
        d.text((lx-5,ly-6), letter, font=font('GeistMono-Regular.ttf',9), fill=(160,130,240))
    # Inner filled circle
    d.ellipse([cx-44,cy-44,cx+44,cy+44],fill=(25,20,60),outline=(100,80,200),width=2)
    d.text((cx-18,cy-12),'🔍', font=font('InstrumentSans-Regular.ttf',28), fill=(160,130,240))

    # Evidence panel
    rounded_rect(d,[458,24,776,130],8,fill=(18,14,45))
    d.text((472,32),'CASE #0x3A7F', font=font('Tektur-Medium.ttf',14), fill='#818cf8')
    for i,(k,v) in enumerate([('Status','ACTIVE'),('Suspect','Unknown'),('Files','12 encrypted')]):
        y=54+i*24; d.text((472,y),f'{k}:', font=mono, fill=(100,90,170)); d.text((570,y),v,font=mono_b,fill=(160,140,240))

    # Bottom accent bar
    d.rectangle([0,345,W,H],fill=(10,8,28))
    glyphs = 'αβγδεζηθικλμνξοπρστυφχψω∆∑∏∫√∂≠≈∞'
    for i in range(40):
        x = i*20+4; d.text((x,355), random.choice(glyphs), font=font('GeistMono-Regular.ttf',12), fill=(60,50,120))
    d.text((300,360),'THE CIPHER CASE — FOLLOW THE BREADCRUMBS', font=font('Tektur-Regular.ttf',13), fill=(130,110,220))

    img.save(os.path.join(OUT,'cipher-case.png'))
    print('✓ cipher-case.png')

# ─────────────────────────────────────────────────────────────────
# 3. DEEP DATA DIVE — Ocean Data  (ocean blue)
# ─────────────────────────────────────────────────────────────────
def deep_data_dive():
    img = Image.new('RGB',(W,H))
    d = ImageDraw.Draw(img)
    # Layered ocean gradient
    layers = [('#0c4a6e',0),('#0e5a80',60),('#0369a1',120),('#0284c7',180),('#0ea5e9',260),('#38bdf8',320)]
    for i in range(len(layers)-1):
        c1,y1 = layers[i]; c2,y2 = layers[i+1]
        r1,g1,b1=rgb(c1); r2,g2,b2=rgb(c2)
        for y in range(y1,y2):
            t=(y-y1)/(y2-y1)
            d.rectangle([0,y,W,y+1],fill=(int(r1+(r2-r1)*t),int(g1+(g2-g1)*t),int(b1+(b2-b1)*t)))
    for y in range(320,H):
        d.rectangle([0,y,W,y+1],fill=rgb('#38bdf8'))

    f_mono = font('DMMono-Regular.ttf',11)
    f_jura = font('Jura-Light.ttf',12)
    f_bold = font('InstrumentSans-Bold.ttf',16)

    # Depth zone labels (left)
    zones = [('0m','SURFACE ZONE',40),('200m','TWILIGHT ZONE',110),('1000m','MIDNIGHT ZONE',185),('4000m','ABYSSAL ZONE',260),('6000m','HADAL ZONE',320)]
    for depth,name,y in zones:
        d.line([0,y,W,y],fill=(255,255,255,30) if False else (255,255,255),width=1)
        d.text((12,y+4), depth, font=f_mono, fill=(200,240,255))
        d.text((12,y+18), name, font=font('Jura-Light.ttf',9), fill=(150,210,240))

    # Wavy data line (main)
    pts_main = [(x, 160+int(35*math.sin(x/50+0.5))+int(15*math.sin(x/22))) for x in range(80,W-80)]
    for i in range(len(pts_main)-1):
        d.line([pts_main[i],pts_main[i+1]],fill=(56,189,248),width=2)
    # Secondary line
    pts2 = [(x, 240+int(25*math.sin(x/60+2))+int(10*math.sin(x/18+1))) for x in range(80,W-80)]
    for i in range(len(pts2)-1):
        d.line([pts2[i],pts2[i+1]],fill=(14,165,233,150) if False else (14,165,233),width=2)

    # Data scatter dots
    random.seed(42)
    for _ in range(80):
        x=random.randint(80,W-80); y=random.randint(30,360)
        r=random.randint(2,6)
        alpha_val = max(60, 200-y//2)
        d.ellipse([x-r,y-r,x+r,y+r],fill=(100,220,255))

    # Right panel: stats
    rounded_rect(d,[640,30,780,260],10,fill=(5,30,50))
    d.text((652,40),'METRICS', font=font('Jura-Medium.ttf',12), fill=(100,200,240))
    for i,(val,lbl) in enumerate([('3,847m','Max Depth'),('14.2°C','Temp'),('34.8‰','Salinity'),('6.2pH','Acidity')]):
        y=64+i*48; d.text((652,y),val,font=font('InstrumentSans-Bold.ttf',18),fill=(56,189,248))
        d.text((652,y+22),lbl,font=f_jura,fill=(100,180,220))

    # Bottom label
    d.rectangle([0,360,W,H],fill=(4,20,40))
    d.text((W//2-140,368),'DEEP DATA DIVE  —  OCEAN AS DATASET', font=font('Jura-Medium.ttf',14),fill=(56,189,248))

    img.save(os.path.join(OUT,'deep-data-dive.png'))
    print('✓ deep-data-dive.png')

# ─────────────────────────────────────────────────────────────────
# 4. PAWKICKS — Sneaker + Dog Brand  (pink-red)
# ─────────────────────────────────────────────────────────────────
def pawkicks():
    img = Image.new('RGB',(W,H))
    d = ImageDraw.Draw(img)
    gradient_bg(d,'#4a0010','#f43f5e')

    f_bold  = font('BigShoulders-Bold.ttf',18)
    f_reg   = font('Outfit-Regular.ttf',12)
    f_price = font('BigShoulders-Bold.ttf',36)
    f_brand = font('Boldonse-Regular.ttf',42)

    # Paw print pattern background (subtle)
    random.seed(7)
    for _ in range(20):
        px,py = random.randint(0,W),random.randint(0,H)
        size=random.randint(8,24)
        d.ellipse([px,py,px+size,py+size*0.8],fill=(255,255,255,15) if False else (200,20,50))
        for dot_x,dot_y in [(-size*0.4,-size*0.4),(size*0.1,-size*0.5),(size*0.55,-size*0.35)]:
            dx,dy=int(px+size//2+dot_x),int(py+dot_y)
            s=size//4
            d.ellipse([dx,dy,dx+s,dy+s],fill=(180,15,45))

    # Main product card
    rounded_rect(d,[80,40,480,360],20,fill=(255,255,255))
    # Left: product visual (geometric sneaker)
    d.rectangle([100,60,280,340],fill=(250,240,245))
    # Sneaker body (simplified geometric)
    # Sole
    d.ellipse([110,280,270,340],fill=(30,30,30))
    # Upper body
    pts_upper = [(130,280),(120,220),(160,180),(220,170),(260,185),(270,250),(260,280)]
    d.polygon(pts_upper, fill=(244,63,94))
    # Toe box
    d.ellipse([115,255,190,295],fill=(220,30,70))
    # Laces (lines)
    for i in range(5):
        y=210+i*14
        d.line([160+i*6,y,220-i*6,y],fill='white',width=2)
    # Swoosh-like shape
    pts_swoosh=[(140,240),(200,230),(255,245),(250,255),(190,245),(138,252)]
    d.polygon(pts_swoosh,fill=(255,255,255,180) if False else (255,255,255))
    # Dog paw on sneaker
    d.ellipse([215,200,235,220],fill='white')
    for tx,ty in [(208,193),(222,191),(235,193)]:
        d.ellipse([tx,ty,tx+8,ty+8],fill='white')

    # Right: product info
    d.text((295,70),'PAWKICKS', font=font('BigShoulders-Bold.ttf',28), fill=(30,30,30))
    d.text((295,102),'Air Paw Pro Max', font=font('BigShoulders-Regular.ttf',16), fill=(100,100,100))
    d.line([295,125,465,125],fill=(230,230,230),width=1)
    # Stars
    d.text((295,135),'★★★★★', font=f_reg, fill=(244,63,94))
    d.text((365,137),'(128)', font=f_reg, fill=(150,150,150))
    # Colors
    d.text((295,165),'COLOR', font=font('InstrumentSans-Bold.ttf',10), fill=(120,120,120))
    for i,c in enumerate([(244,63,94),(30,30,30),(255,200,200),(255,255,255)]):
        cx=295+i*30
        d.ellipse([cx,180,cx+20,200],fill=c,outline=(200,200,200),width=1)
    d.ellipse([295,180,315,200],outline=(30,30,30),width=2)
    # Size
    d.text((295,215),'SIZE', font=font('InstrumentSans-Bold.ttf',10), fill=(120,120,120))
    for i,s in enumerate(['40','41','42','43','44']):
        sx=295+i*36
        col=(244,63,94) if i==2 else (240,240,240)
        tc=(255,255,255) if i==2 else (80,80,80)
        rounded_rect(d,[sx,230,sx+30,252],6,fill=col)
        d.text((sx+8,234),s,font=font('InstrumentSans-Regular.ttf',11),fill=tc)
    # Price
    d.text((295,270),'$', font=f_bold, fill=(244,63,94))
    d.text((310,260),'289', font=f_price, fill=(30,30,30))
    # CTA
    rounded_rect(d,[295,310,460,342],12,fill=(244,63,94))
    d.text((345,318),'ADD TO CART', font=font('BigShoulders-Bold.ttf',14), fill='white')

    # Brand name floating
    d.text((510,130),'PAW', font=font('Boldonse-Regular.ttf',60), fill=(255,255,255))
    d.text((510,195),'KICKS', font=font('Boldonse-Regular.ttf',60), fill=(255,255,255))
    d.text((514,270),'Where every step', font=font('NothingYouCouldDo-Regular.ttf',18), fill=(255,180,190))
    d.text((514,294),'tells a story.', font=font('NothingYouCouldDo-Regular.ttf',18), fill=(255,180,190))

    img.save(os.path.join(OUT,'pawkicks.png'))
    print('✓ pawkicks.png')

# ─────────────────────────────────────────────────────────────────
# 5. AERO PULSE — Analytics Dashboard  (purple)
# ─────────────────────────────────────────────────────────────────
def aero_pulse():
    img = Image.new('RGB',(W,H))
    d = ImageDraw.Draw(img)
    gradient_bg(d,'#1e1040','#3730a3')

    f_bold = font('BricolageGrotesque-Bold.ttf',14)
    f_reg  = font('BricolageGrotesque-Regular.ttf',11)
    f_num  = font('BricolageGrotesque-Bold.ttf',28)
    f_sm   = font('InstrumentSans-Regular.ttf',10)

    # Top nav
    d.rectangle([0,0,W,48],fill=(15,8,40))
    d.text((20,14),'AeroPulse', font=font('BricolageGrotesque-Bold.ttf',20), fill='#a78bfa')
    for i,lbl in enumerate(['Overview','Analytics','Reports','Settings']):
        d.text((200+i*110,18), lbl, font=f_reg, fill=(160,140,210) if i>0 else (220,200,255))
        if i==0: d.line([200,42,200+len(lbl)*7,42],fill='#8b5cf6',width=2)
    # Profile circle
    d.ellipse([754,10,784,40],fill=(99,102,241))
    d.text((762,16),'EY', font=font('InstrumentSans-Bold.ttf',13), fill='white')

    # KPI Cards row
    kpis=[('$2.84M','Total Revenue','+12.4%','#10b981'),
          ('48.2K','Active Users','+8.7%','#a78bfa'),
          ('$94.20','Avg. Order','+3.1%','#38bdf8'),
          ('96.3%','Uptime','−0.2%','#f87171')]
    for i,(val,lbl,chg,c) in enumerate(kpis):
        x=16+i*194
        rounded_rect(d,[x,58,x+186,136],10,fill=(25,15,55))
        d.text((x+12,68),val,font=f_num,fill='white')
        d.text((x+12,102),lbl,font=f_sm,fill=(150,130,200))
        rounded_rect(d,[x+12,116,x+12+len(chg)*7+8,130],8,fill=(c+'22') if False else (30,20,60))
        d.text((x+16,117),chg,font=f_sm,fill=c)

    # Main line chart
    rounded_rect(d,[16,146,540,320],10,fill=(20,12,50))
    d.text((28,156),'Revenue Trend', font=f_bold, fill=(200,180,255))
    d.text((28,172),'Last 12 months', font=f_sm, fill=(100,80,160))
    # Grid lines
    for i in range(4):
        y=306-i*36; d.line([28,y,530,y],fill=(40,30,80),width=1)
        d.text((4,y-6),f'{(i+1)*25}K',font=font('DMMono-Regular.ttf',8),fill=(80,60,130))
    # Chart bars
    months=['J','F','M','A','M','J','J','A','S','O','N','D']
    vals=[42,58,45,70,85,78,92,88,96,102,88,115]
    for i,(m,v) in enumerate(zip(months,vals)):
        x=40+i*40; bh=int(v*1.5); by=306-bh
        rounded_rect(d,[x,by,x+28,306],4,fill=(99,102,241,200) if False else (60,50,140))
        if i in [6,10,11]:  # highlight peaks
            rounded_rect(d,[x,by,x+28,306],4,fill=(139,92,246))
            d.ellipse([x+10,by-5,x+18,by+3],fill=(167,139,250))
        d.text((x+6,312),m,font=f_sm,fill=(100,80,160))
    # Trend line overlay
    pts=[(40+i*40+14, 306-int(v*1.5)) for i,v in enumerate(vals)]
    for i in range(len(pts)-1):
        d.line([pts[i],pts[i+1]],fill=(167,139,250),width=2)

    # Right sidebar
    rounded_rect(d,[552,146,784,320],10,fill=(20,12,50))
    d.text((564,156),'Top Sources', font=f_bold, fill=(200,180,255))
    sources=[('Organic','38%',0.38,(99,102,241)),('Direct','29%',0.29,(139,92,246)),
             ('Referral','21%',0.21,(167,139,250)),('Social','12%',0.12,(196,181,253))]
    for i,(name,pct,frac,c) in enumerate(sources):
        y=180+i*32
        d.text((564,y),name,font=f_sm,fill=(160,140,210))
        d.text((700,y),pct,font=f_sm,fill='white')
        d.rectangle([564,y+14,760,y+20],fill=(40,30,80))
        d.rectangle([564,y+14,564+int(196*frac),y+20],fill=c)

    # Bottom strip
    d.rectangle([0,335,W,H],fill=(12,6,35))
    for i,(lbl,val) in enumerate([('Sessions','124,847'),('Bounce Rate','23.4%'),('Pages/Visit','4.7'),('Duration','3m 42s')]):
        x=40+i*185
        d.text((x,345),lbl,font=f_sm,fill=(100,80,160))
        d.text((x,360),val,font=font('BricolageGrotesque-Bold.ttf',16),fill=(180,160,240))

    img.save(os.path.join(OUT,'aero-pulse.png'))
    print('✓ aero-pulse.png')

# ─────────────────────────────────────────────────────────────────
# 6. AI SPACE MISSION — Space Interface  (dark purple/space)
# ─────────────────────────────────────────────────────────────────
def ai_space():
    img = Image.new('RGB',(W,H))
    d = ImageDraw.Draw(img)
    gradient_bg(d,'#05030f','#1e1b4b', mode='v')

    f_mono = font('GeistMono-Regular.ttf',10)
    f_mono_b = font('GeistMono-Bold.ttf',12)
    f_tech = font('Tektur-Regular.ttf',13)

    # Stars
    random.seed(99)
    for _ in range(200):
        x,y=random.randint(0,W),random.randint(0,H)
        br=random.randint(120,255); r=random.randint(1,3)
        d.ellipse([x-r,y-r,x+r,y+r],fill=(br,br,min(255,br+30)))

    # Galaxy map (concentric circles + grid)
    cx,cy=580,195
    for r in [20,45,75,110,145]:
        d.ellipse([cx-r,cy-r,cx+r,cy+r],outline=(80,60,160),width=1)
    # Radial lines
    for angle in range(0,360,30):
        a=math.radians(angle)
        d.line([cx,cy,cx+145*math.cos(a),cy+145*math.sin(a)],fill=(50,40,100),width=1)
    # Planets
    planet_data=[(45,210,(99,102,241)),(90,100,(167,139,250)),(130,290,(79,70,229)),(70,350,(124,58,237))]
    for r_orbit,angle,c in planet_data:
        a=math.radians(angle)
        px,py=cx+r_orbit*math.cos(a),cy+r_orbit*math.sin(a)
        s=6
        d.ellipse([px-s,py-s,px+s,py+s],fill=c)
    # Center star
    d.ellipse([cx-10,cy-10,cx+10,cy+10],fill=(255,220,100))
    for a in range(0,360,45):
        angle=math.radians(a)
        d.line([cx+10*math.cos(angle),cy+10*math.sin(angle),
                cx+20*math.cos(angle),cy+20*math.sin(angle)],fill=(255,200,80),width=1)

    # Terminal panel left
    rounded_rect(d,[20,20,440,280],10,fill=(8,6,20))
    d.rectangle([20,20,440,44],fill=(20,15,50))
    d.text((180,28),'MISSION CONTROL — ODYSSEY-7', font=f_tech, fill=(120,100,200))
    terminal_lines=[
        '[SYS]  Initializing AI core...',
        '[AI ]  Neural matrix online ████████ 100%',
        '[NAV]  Course plotted: Sector 7-Gamma',
        '[SCI]  Anomaly detected at coordinates',
        '       47.3°N 221.8°E — classifying...',
        '[AI ]  Classification: UNKNOWN ENTITY',
        '[COM]  Transmitting to Earth base...',
        '[SYS]  Signal delay: 23.4 minutes',
        '[AI ]  Autonomous decision: INVESTIGATE',
        '[NAV]  Adjusting trajectory... DONE',
        '[!!! ]  Hull temperature: 2,847°C',
        '[AI ]  Shields at 94% — NOMINAL',
    ]
    for i,line in enumerate(terminal_lines):
        col=(100,240,100) if '[AI ]' in line else (200,200,200) if '[SYS]' in line else (255,200,50) if '[!!!]' in line else (150,140,220)
        d.text((30,52+i*18), line, font=f_mono, fill=col)

    # Coordinates panel bottom
    rounded_rect(d,[20,290,440,375],10,fill=(8,6,20))
    for i,(lbl,val) in enumerate([('MISSION DAY','847'),('DIST FROM SUN','1.2 AU'),('SPEED','32,400 km/h'),('CREW STATUS','OPTIMAL')]):
        x=28+i*104
        d.text((x,298),lbl,font=font('DMMono-Regular.ttf',7),fill=(80,70,140))
        d.text((x,312),val,font=f_mono_b,fill=(160,140,230))

    # Stars cluster (right side atmosphere)
    d.text((455,30),'ODYSSEY', font=font('Tektur-Medium.ttf',20), fill=(100,80,200))
    d.text((455,55),' MISSION 7', font=font('Tektur-Regular.ttf',16), fill=(80,60,180))

    img.save(os.path.join(OUT,'ai-space.png'))
    print('✓ ai-space.png')

# ─────────────────────────────────────────────────────────────────
# 7. HYBRID ATHLETE — Training Platform  (orange)
# ─────────────────────────────────────────────────────────────────
def hybrid_athlete():
    img = Image.new('RGB',(W,H))
    d = ImageDraw.Draw(img)
    gradient_bg(d,'#431407','#f97316')

    f_bold = font('BigShoulders-Bold.ttf',18)
    f_reg  = font('Outfit-Regular.ttf',11)
    f_num  = font('BigShoulders-Bold.ttf',32)
    f_sm   = font('InstrumentSans-Regular.ttf',10)

    # Left: circular progress rings
    def ring(cx,cy,r,pct,c,label,val):
        # Background ring
        d.arc([cx-r,cy-r,cx+r,cy+r],0,360,fill=(80,40,15),width=12)
        # Progress arc
        end_angle=-90+int(360*pct)
        d.arc([cx-r,cy-r,cx+r,cy+r],-90,end_angle,fill=c,width=12)
        d.text((cx-15,cy-20),val,font=font('BigShoulders-Bold.ttf',20),fill='white')
        d.text((cx-20,cy+4),label,font=f_sm,fill=(255,200,150))

    ring(100,130,70,0.82,(249,115,22),'STRENGTH','82%')
    ring(100,130,50,0.68,(251,146,60),'CARDIO','68%')
    ring(100,130,30,0.91,(253,186,116),'RECOVERY','91%')

    # Week calendar grid
    rounded_rect(d,[200,24,560,200],12,fill=(40,15,5))
    d.text((212,32),'WEEK 34 — TRAINING PLAN', font=font('BigShoulders-Bold.ttf',14), fill='#fb923c')
    days=['MON','TUE','WED','THU','FRI','SAT','SUN']
    types=['STR','RUN','REST','HIIT','CYC','REST','LNG']
    colors=[(249,115,22),(251,146,60),(60,40,20),(239,68,68),(249,115,22),(60,40,20),(234,88,12)]
    for i,(day,typ,c) in enumerate(zip(days,types,colors)):
        x=212+i*48; is_today=(i==2)
        rounded_rect(d,[x,54,x+42,172],8,fill=(60,25,5) if not is_today else (249,115,22))
        d.text((x+8,60),day,font=f_sm,fill='white')
        d.line([x+4,76,x+38,76],fill=(80,40,10),width=1)
        d.text((x+6,82),typ,font=font('BigShoulders-Bold.ttf',13),fill=c if not is_today else 'white')
        # Mini bar
        h_bar=int(50*[0.8,0.6,0.1,0.9,0.7,0.1,0.95][i])
        d.rectangle([x+8,162-h_bar,x+34,162],fill=c if not is_today else 'white')

    # Metrics right panel
    rounded_rect(d,[572,24,784,200],12,fill=(40,15,5))
    d.text((584,32),'TODAY\'S STATS', font=font('BigShoulders-Bold.ttf',14), fill='#fb923c')
    metrics=[('8,423','Steps'),('647','Calories'),('62','BPM avg'),('5.2km','Distance')]
    for i,(val,lbl) in enumerate(metrics):
        y=58+i*36
        d.text((584,y),val,font=font('BigShoulders-Bold.ttf',22),fill='white')
        d.text((584,y+22),lbl,font=f_sm,fill=(200,120,60))

    # Bottom performance chart
    rounded_rect(d,[16,220,784,365],12,fill=(35,12,3))
    d.text((28,228),'PERFORMANCE TIMELINE — 12 WEEKS', font=font('BigShoulders-Bold.ttf',13), fill='#fb923c')
    weeks=[65,70,68,75,80,78,82,79,85,88,90,94]
    for i,v in enumerate(weeks):
        x=40+i*60; h=int(v*0.95)
        col=(249,115,22) if i==11 else (180,80,20)
        rounded_rect(d,[x,340-h,x+44,340],6,fill=col)
        d.text((x+10,345),f'W{i+1}',font=f_sm,fill=(200,120,60))
        if i==11: d.text((x+4,335-h),f'{v}%',font=f_sm,fill='white')

    d.rectangle([0,375,W,H],fill=(30,10,2))
    d.text((W//2-120,380),'HYBRID ATHLETE — TRAIN SMARTER', font=font('BigShoulders-Bold.ttf',15), fill='#fb923c')

    img.save(os.path.join(OUT,'hybrid-athlete.png'))
    print('✓ hybrid-athlete.png')

# ─────────────────────────────────────────────────────────────────
# 8. MASR LEDGER — Arabic Accounting  (blue)
# ─────────────────────────────────────────────────────────────────
def masr_ledger():
    img = Image.new('RGB',(W,H))
    d = ImageDraw.Draw(img)
    gradient_bg(d,'#0c1a3a','#2563eb')

    f_mono = font('IBMPlexMono-Regular.ttf',10)
    f_bold = font('IBMPlexSerif-Bold.ttf',16)
    f_reg  = font('IBMPlexSerif-Regular.ttf',12)
    f_sm   = font('InstrumentSans-Regular.ttf',10)
    f_num  = font('IBMPlexMono-Bold.ttf',13)

    # Geometric border pattern (Islamic-inspired)
    for i in range(0,W,30):
        d.line([i,0,i,4],fill=(59,130,246),width=2)
        d.line([i,H-4,i,H],fill=(59,130,246),width=2)
    for i in range(0,H,30):
        d.line([0,i,4,i],fill=(59,130,246),width=2)
        d.line([W-4,i,W,i],fill=(59,130,246),width=2)
    # Diamond pattern corners
    for cx,cy in [(0,0),(W,0),(0,H),(W,H)]:
        for r in [20,40,60]:
            d.line([cx,cy-r,cx+r,cy],fill=(59,130,246,60) if False else (30,60,140),width=1)

    # Invoice card
    rounded_rect(d,[40,30,760,370],16,fill=(255,255,255))

    # Invoice header
    d.rectangle([40,30,760,100],fill=(37,99,235))
    d.text((60,44),'MasrLedger', font=font('IBMPlexSerif-Bold.ttf',24), fill='white')
    d.text((60,74),'مصر ليدجر — نظام المحاسبة', font=font('IBMPlexSerif-Regular.ttf',13), fill=(147,197,253))
    # Invoice number
    d.text((560,44),'فاتورة رقم', font=f_sm, fill=(147,197,253))
    d.text((560,60),'INV-2024-0847', font=font('IBMPlexMono-Bold.ttf',16), fill='white')

    # Client info columns
    d.text((60,114),'Billed To:', font=font('IBMPlexSerif-Bold.ttf',11), fill=(100,100,120))
    d.text((60,130),'Al-Nour Trading Co.', font=font('IBMPlexSerif-Bold.ttf',14), fill=(20,20,40))
    d.text((60,148),'Cairo Business District, Egypt', font=f_sm, fill=(100,100,120))
    d.text((60,162),'TIN: 476-83-2910', font=font('IBMPlexMono-Regular.ttf',10), fill=(100,100,120))

    d.text((400,114),'Invoice Date:', font=font('IBMPlexSerif-Bold.ttf',11), fill=(100,100,120))
    d.text((400,130),'15 January 2024', font=f_reg, fill=(20,20,40))
    d.text((400,148),'Due: 15 February 2024', font=f_sm, fill=(100,100,120))

    # Table header
    d.rectangle([60,188,740,208],fill=(239,246,255))
    for x,lbl in [(60,'#'),(80,'Description / الوصف'),(380,'Qty'),(430,'Unit Price'),(560,'VAT 14%'),(660,'Total')]:
        d.text((x+4,193),lbl,font=font('IBMPlexSerif-Bold.ttf',10),fill=(37,99,235))

    # Table rows
    rows=[('01','Web Development Services — خدمات تطوير الويب','1','EGP 45,000','EGP 6,300','EGP 51,300'),
          ('02','UI/UX Design & Branding','3','EGP 12,000','EGP 5,040','EGP 41,040'),
          ('03','Monthly Maintenance Package','12','EGP 2,500','EGP 4,200','EGP 34,200'),
          ('04','API Integration & Testing','1','EGP 18,000','EGP 2,520','EGP 20,520')]
    for i,(num,desc,qty,up,vat,total) in enumerate(rows):
        y=208+i*30; bg=(250,252,255) if i%2==0 else (255,255,255)
        d.rectangle([60,y,740,y+30],fill=bg)
        d.line([60,y,740,y],fill=(220,230,245),width=1)
        for x,txt in [(64,num),(80,desc),(380,qty),(430,up),(560,vat),(660,total)]:
            col=(37,99,235) if x==660 else (30,30,50)
            d.text((x,y+8),txt,font=font('IBMPlexMono-Regular.ttf',9) if x not in (80,) else f_sm,fill=col)

    # Totals section
    d.rectangle([60,328,740,340],fill=(239,246,255))
    d.text((560,330),'Subtotal:', font=f_sm, fill=(80,80,100))
    d.text((660,330),'EGP 126,000', font=font('IBMPlexMono-Regular.ttf',10), fill=(30,30,50))
    d.rectangle([560,342,740,370],fill=(37,99,235))
    d.text((570,350),'TOTAL DUE:', font=font('IBMPlexSerif-Bold.ttf',13), fill='white')
    d.text((650,350),'EGP 147,060', font=font('IBMPlexMono-Bold.ttf',13), fill='white')

    img.save(os.path.join(OUT,'masr-ledger.png'))
    print('✓ masr-ledger.png')

# ─────────────────────────────────────────────────────────────────
# 9. CAMPUS CARE — University Health App  (cyan)
# ─────────────────────────────────────────────────────────────────
def campus_care():
    img = Image.new('RGB',(W,H))
    d = ImageDraw.Draw(img)
    gradient_bg(d,'#013241','#0891b2')

    f_bold = font('Outfit-Bold.ttf',14)
    f_reg  = font('Outfit-Regular.ttf',11)
    f_sm   = font('InstrumentSans-Regular.ttf',10)

    # Phone mockup frame (center)
    px,py,pw,ph = 280,15,240,370
    rounded_rect(d,[px-4,py-4,px+pw+4,py+ph+4],26,fill=(10,60,80))
    rounded_rect(d,[px,py,px+pw,py+ph],22,fill=(245,252,255))
    # Notch
    rounded_rect(d,[px+80,py+6,px+160,py+22],8,fill=(10,60,80))
    # Status bar
    d.text((px+12,py+28),'9:41', font=font('InstrumentSans-Bold.ttf',11), fill=(20,60,80))
    d.text((px+180,py+28),'●●●', font=f_sm, fill=(20,60,80))

    # App header
    d.rectangle([px,py+44,px+pw,py+90],fill=(8,145,178))
    d.text((px+12,py+52),'CampusCare', font=font('Outfit-Bold.ttf',18), fill='white')
    d.text((px+12,py+72),'GIU Health Services', font=f_sm, fill=(165,243,252))

    # Nav tabs
    for i,(icon,lbl) in enumerate([('⊕','Home'),('📅','Book'),('📋','Records'),('👤','Profile')]):
        x=px+4+i*60
        col=(8,145,178) if i==1 else (120,140,150)
        d.text((x+8,py+ph-30),icon,font=font('Outfit-Regular.ttf',14),fill=col)
        d.text((x+4,py+ph-14),lbl,font=font('InstrumentSans-Regular.ttf',8),fill=col)
        if i==1: d.line([x+4,py+ph-34,x+56,py+ph-34],fill=(8,145,178),width=2)

    # Appointment booking screen
    d.text((px+12,py+100),'Book Appointment', font=font('Outfit-Bold.ttf',13), fill=(20,50,70))
    d.text((px+12,py+116),'Select a service:', font=f_sm, fill=(80,100,110))
    services=[('General Practice','Dr. Ahmed'),('Dentistry','Dr. Sara'),('Mental Health','Dr. Laila')]
    for i,(svc,doc) in enumerate(services):
        y=py+132+i*44
        rounded_rect(d,[px+12,y,px+228,y+36],8,fill=(225,248,252) if i!=1 else (8,145,178))
        tc=(20,60,80) if i!=1 else 'white'
        d.text((px+20,y+6),svc,font=font('Outfit-Bold.ttf',11),fill=tc)
        d.text((px+20,y+20),doc,font=f_sm,fill=(80,120,140) if i!=1 else (200,240,248))
        d.text((px+200,y+12),'→',font=font('Outfit-Bold.ttf',14),fill=tc)

    d.text((px+12,py+264),'Next Available:', font=f_sm, fill=(80,100,110))
    d.text((px+12,py+278),'Today, 2:30 PM', font=font('Outfit-Bold.ttf',13), fill=(8,145,178))
    rounded_rect(d,[px+12,py+298,px+228,py+326],12,fill=(8,145,178))
    d.text((px+72,py+306),'Confirm Booking', font=font('Outfit-Bold.ttf',12), fill='white')

    # Left info panel
    rounded_rect(d,[20,30,256,200],12,fill=(8,50,70))
    d.text((32,40),'HEALTH STATS', font=font('Outfit-Bold.ttf',13), fill='#22d3ee')
    for i,(lbl,val,c) in enumerate([('BMI','22.4 ✓',(52,211,153)),('Blood Type','O+',(56,189,248)),('Vaccinations','Up to date',(52,211,153)),('Appointments','3 this month',(168,85,247))]):
        y=64+i*32
        d.text((32,y),lbl,font=f_sm,fill=(100,180,200))
        d.text((130,y),val,font=font('Outfit-Bold.ttf',12),fill=c)

    # Right info panel
    rounded_rect(d,[548,30,780,200],12,fill=(8,50,70))
    d.text((560,40),'CAMPUS MAP', font=font('Outfit-Bold.ttf',13), fill='#22d3ee')
    # Mini map grid
    for x in range(560,780,20): d.line([x,60,x,195],fill=(15,70,90),width=1)
    for y in range(60,195,20): d.line([560,y,780,y],fill=(15,70,90),width=1)
    # Buildings
    for bx,by,bw,bh,bc,bl in [(570,70,50,40,(20,100,130),'MED'),
                                (630,80,60,30,(8,145,178),'LIB'),
                                (700,65,60,50,(5,100,120),'HALL'),
                                (575,125,40,50,(30,120,150),'GYM'),
                                (625,130,80,40,(8,145,178),'HLTH')]:
        d.rectangle([bx,by,bx+bw,by+bh],fill=bc)
        d.text((bx+4,by+bh//2-6),bl,font=font('DMMono-Regular.ttf',8),fill='white')
    # Health center highlight
    d.rectangle([625,130,705,170],fill=(22,211,153))
    d.text((630,148),'CLINIC',font=font('DMMono-Regular.ttf',8),fill=(5,50,30))

    # Bottom stats
    d.rectangle([20,215,780,375],fill=(8,50,70))
    d.line([20,215,780,215],fill=(8,145,178),width=2)
    d.text((32,224),'STUDENT WELLNESS OVERVIEW — GIU CAIRO 2024', font=font('Outfit-Bold.ttf',12), fill='#22d3ee')
    stats=[('1,240','Appointments\nThis Month'),('96%','Satisfaction\nRate'),('48h','Avg Response'),('12','Medical\nStaff')]
    for i,(val,lbl) in enumerate(stats):
        x=60+i*180
        d.text((x,248),val,font=font('BigShoulders-Bold.ttf',32),fill=(34,211,238))
        for j,line in enumerate(lbl.split('\n')):
            d.text((x,284+j*14),line,font=f_sm,fill=(100,180,200))

    img.save(os.path.join(OUT,'campus-care.png'))
    print('✓ campus-care.png')

# ─────────────────────────────────────────────────────────────────
# 10. ENTERPRISE BI — Business Intelligence  (amber)
# ─────────────────────────────────────────────────────────────────
def enterprise_bi():
    img = Image.new('RGB',(W,H))
    d = ImageDraw.Draw(img)
    gradient_bg(d,'#1c0a00','#92400e')

    f_bold = font('WorkSans-Bold.ttf',14)
    f_reg  = font('WorkSans-Regular.ttf',11)
    f_num  = font('WorkSans-Bold.ttf',24)
    f_sm   = font('InstrumentSans-Regular.ttf',10)
    f_mono = font('IBMPlexMono-Regular.ttf',9)

    # Top nav
    d.rectangle([0,0,W,46],fill=(15,6,0))
    d.text((20,12),'EnterpriseBI', font=font('WorkSans-Bold.ttf',20), fill='#f59e0b')
    d.text((200,16),'Dashboard', font=f_reg, fill='#fbbf24')
    d.text((290,16),'Reports', font=f_reg, fill=(120,80,30))
    d.text((360,16),'Analytics', font=f_reg, fill=(120,80,30))
    d.text((450,16),'Settings', font=f_reg, fill=(120,80,30))
    rounded_rect(d,[660,10,780,36],8,fill=(180,83,9))
    d.text((672,16),'Export Report', font=f_sm, fill='white')

    # KPI tiles
    kpis=[('$8.4M','Total Revenue','▲ 14.2% YoY',(245,158,11)),
          ('$2.1M','Operating Profit','▲ 9.8% YoY',(251,191,36)),
          ('67.3%','Gross Margin','▼ 1.2% YoY',(239,68,68)),
          ('4,820','Enterprise Clients','▲ 22.1% YoY',(245,158,11))]
    for i,(val,lbl,chg,c) in enumerate(kpis):
        x=12+i*192
        rounded_rect(d,[x,56,x+184,132],10,fill=(30,12,2))
        d.line([x,56,x,132],fill=c,width=3)
        d.text((x+14,64),val,font=f_num,fill='white')
        d.text((x+14,94),lbl,font=f_sm,fill=(180,130,60))
        col=(52,211,153) if '▲' in chg else (239,68,68)
        d.text((x+14,110),chg,font=f_sm,fill=col)

    # Main bar chart
    rounded_rect(d,[12,142,500,340],10,fill=(22,9,0))
    d.text((24,150),'Revenue by Region — Q4 2024', font=f_bold, fill='#fbbf24')
    regions=[('North Africa','84%',0.84),(('Middle East','71%',0.71)),('Europe','92%',0.92),('Americas','67%',0.67),('Asia Pacific','78%',0.78)]
    bar_colors=[(245,158,11),(251,191,36),(217,119,6),(180,83,9),(253,230,138)]
    max_h=120
    for i,((reg,pct,frac),c) in enumerate(zip(regions,bar_colors)):
        x=36+i*90; bh=int(max_h*frac); by=300-bh
        rounded_rect(d,[x,by,x+70,300],4,fill=c)
        d.text((x+4,by-16),pct,font=font('WorkSans-Bold.ttf',11),fill='white')
        # Region label (wrapped)
        words=reg.split()
        for j,w in enumerate(words):
            d.text((x+4,304+j*12),w,font=f_sm,fill=(180,130,60))

    # Donut chart
    cx,cy,r_out,r_in = 620,240,80,50
    segments=[(0.38,'#f59e0b',38),(0.27,'#fbbf24',27),(0.21,'#d97706',21),(0.14,'#92400e',14)]
    start=-90
    for frac,c,pct in segments:
        end=start+frac*360
        d.pieslice([cx-r_out,cy-r_out,cx+r_out,cy+r_out],start,end,fill=rgb(c))
        start=end
    d.ellipse([cx-r_in,cy-r_in,cx+r_in,cy+r_in],fill=(22,9,0))
    d.text((cx-20,cy-14),'67.3%',font=font('WorkSans-Bold.ttf',12),fill='#fbbf24')
    d.text((cx-22,cy+4),'Margin',font=f_sm,fill=(180,130,60))
    rounded_rect(d,[510,142,780,155],0,fill=(22,9,0))
    d.text((518,150),'Margin Breakdown', font=f_bold, fill='#fbbf24')
    for i,(frac,c,pct) in enumerate(segments):
        y=162+i*18; d.rectangle([518,y+3,530,y+13],fill=rgb(c))
        labels=['Gross','Operating','Net','Other']
        d.text((536,y),f'{labels[i]}: {pct}%',font=f_sm,fill=(200,160,80))

    # Data table bottom
    rounded_rect(d,[12,348,780,395],8,fill=(20,8,0))
    d.line([12,368,780,368],fill=(60,30,5),width=1)
    d.text((20,352),'TOP PERFORMING SEGMENTS', font=f_bold, fill='#fbbf24')
    for i,(seg,rev,gr,margin) in enumerate([('Enterprise SaaS','$3.2M','▲24%','71.2%'),
                                              ('Pro Services','$2.1M','▲18%','64.8%'),
                                              ('Support Contracts','$1.4M','▲12%','88.3%'),
                                              ('Marketplace','$0.9M','▲31%','52.1%')]):
        x=20+i*190
        d.text((x,372),seg,font=f_sm,fill=(200,150,60))
        d.text((x,384),f'{rev}  {gr}  M:{margin}',font=font('IBMPlexMono-Regular.ttf',8),fill=(255,180,60))

    img.save(os.path.join(OUT,'enterprise-bi.png'))
    print('✓ enterprise-bi.png')

# ─── RUN ALL ───────────────────────────────────────────────────────
if __name__ == '__main__':
    random.seed(42)
    sho8lana()
    cipher_case()
    deep_data_dive()
    pawkicks()
    aero_pulse()
    ai_space()
    hybrid_athlete()
    masr_ledger()
    campus_care()
    enterprise_bi()
    print('\nAll 10 thumbnails generated!')
