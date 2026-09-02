# -*- coding: utf-8 -*-
"""Monta deck.html embarcando fontes e logotipos do branding book do cliente."""
import base64, io, re, os
B=r"C:\Users\RCX\AppData\Local\Temp\claude\C--Users-RCX-Desktop-Projetos\0e9549bd-443a-4740-9376-c793c98ff232\scratchpad\brand"
F=os.path.join(B,"Fontes","Fontes")
L=os.path.join(B,"Logos","Logos","Cl\u00ednica","SVG")

def b64(p):
    with open(p,'rb') as f: return base64.b64encode(f.read()).decode('ascii')

def svg(name):
    s=io.open(os.path.join(L,name),encoding='utf-8').read()
    s=re.sub(r'<\?xml[^>]*\?>\s*','',s)
    s=re.sub(r'\s*id="[^"]*"','',s)
    s=re.sub(r'\s*data-name="[^"]*"','',s)
    s=s.replace('<svg ','<svg fill="currentColor" ',1)
    return re.sub(r'\n\s*','',s).strip()

fonts={
 '__SCOTCH_ROMAN__': os.path.join(F,"Scotch Text","Positype - Scotch Text Roman.otf"),
 '__SCOTCH_SEMI__':  os.path.join(F,"Scotch Text","Positype - Scotch Text SemiBold.otf"),
 '__SCOTCH_ITALIC__':os.path.join(F,"Scotch Text","Positype - Scotch Text Italic.otf"),
 '__NM_BOOK__':      os.path.join(F,"Neue Montreal","PPNeueMontreal-Book.ttf"),
 '__NM_MEDIUM__':    os.path.join(F,"Neue Montreal","PPNeueMontreal-Medium.ttf"),
}
B64 = {k: b64(p) for k, p in fonts.items()}
SVGS = {'__WORDMARK__': svg("CHH_logosAsset 13.svg"),
        '__SYMBOL__':   svg("CHH_logosAsset 14.svg"),
        '__MARKMINI__': svg("CHH_logosAsset 14.svg")}

for src, out in [("deck.template.html","deck.html"), ("app.template.html","index.html")]:
    if not os.path.exists(src): continue
    html = io.open(src, encoding='utf-8').read()
    for k, v in list(B64.items()) + list(SVGS.items()):
        html = html.replace(k, v)
    assert not re.findall(r'__[A-Z_]+__', html), (out, re.findall(r'__[A-Z_]+__', html)[:3])
    io.open(out,'w',encoding='utf-8').write(html)
    print(out + ":", round(os.path.getsize(out)/1024/1024, 2), "MB")
