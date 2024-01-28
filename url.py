import pyshorteners as ps

url = "https://www.flipkart.com/samsung-evo-plus-64-gb-microsdxc-class-10-130-mb-s-memory-card/p/itmcb599cd8a1f60?pid=ACCG9NPXHEGZ2YK8&lid=LSTACCG9NPXHEGZ2YK81MI55U&marketplace=FLIPKART&store=6bo%2Fjdy&srno=b_1_2&otracker=browse&fm=organic&iid=302ceafe-ec7c-4f62-a81a-0fda5c160ff1.ACCG9NPXHEGZ2YK8.SEARCH&ppt=hp&ppn=homepage&ssid=8rcikboohs0000001706001609494"

u=ps.Shortener().tinyurl.short(url)

print(u)

    