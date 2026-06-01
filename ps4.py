from bs4 import BeautifulSoup
htmlcode="""
<html>

<body>
    <h1>Html</h1>
    <p>Simple Html</p>
    <b>
    <p>1</p>
    <p>2</p>
    <p>2</p>
    </b>
    <i>Piyush</i>
    <img src="pics/ch.jpg">
    <img src="pics/view.jpg">

</body>
</html>
"""
soup = BeautifulSoup(htmlcode, 'html.parser')
divs=soup.find_all("img")
for d in divs:
    print(d)