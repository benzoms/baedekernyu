
sem_loc = 'flo_s23'

pagecount = 27
#format: Fall '23 NYC
title = "Spring '23 Florence"
#<h3 class="magtitle" style="text-align:center;">{title}</h3>

titleblock = f"""\n<div id="allmag">
<button class="nav-btn" style="float:left;" onclick="plusDivs(-1)">&#10094;</button>
<div class="magazine-viewer">\n"""

pagenum = 1

with open(f'{sem_loc}.html','w') as f: 
    with open(f'htmlblocks/htmlblock1.txt','r') as g:
        f.writelines([g.read(), titleblock])

with open(f'{sem_loc}.html','a') as f:       
    for i in range(1, pagecount+1):
        img_elem_str = f"""<img class="mySlides" src="https://raw.githubusercontent.com/benzoms/baedekernyu/main/magsrcimgs/{sem_loc}/{i}.png" style="width:100%">\n"""
        f.write(img_elem_str)

with open(f'{sem_loc}.html','a') as f: 
    with open(f'htmlblocks/htmlblock2.txt','r') as g:
        f.writelines(g.read())


    