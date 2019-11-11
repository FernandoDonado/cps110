
WIDTH=700
HEIGHT=700


def makedrawing():  
    svgdata = []
    svgdata.append(f"<rect x='0' y='0' width='{WIDTH}' height='{HEIGHT}' fill='black' />")

    for x in range(0, WIDTH+1, 100):
        svgdata.append(f"<line x1='{x}' y1='0' x2='{x}' y2='{HEIGHT}' stroke='green' />")

    for y in range(0, HEIGHT+1, 100):
        svgdata.append(f"<line x1='0' y1='{y}' x2='{WIDTH}' y2='{y}' stroke='green' />")

    svgdata.append("<image x='20' y='30' xlink:href='images/duck.png' width='50' height='50' />")
    svgdata.append("<text x='10' y='20' font-family='Verdana' font-size='10' stroke='white'>Some text here</text>")
        
    svgstring = '\n'.join(svgdata)
    return HTML_PAGE.format(WIDTH, HEIGHT, svgstring)


HTML_PAGE = """
<!DOCTYPE html>
<html>
<body>

<svg width="{0}" height="{1}">
  {2}
</svg>

</body>
</html>
"""

drawing = makedrawing()
with open('demo.html', 'w') as f:
    f.write(drawing)
    
