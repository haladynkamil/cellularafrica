from PIL import Image

# dobra to we sprobuj dojechac do tego zeby z obrazka miec [[x.y].[r,g,b]]

def get_rgba(image_name):
    im = Image.open(str(image_name))
    rgb_data = []
    pix = im.load()
    for x in range(im.size[0]):
        rgb_data.append([])
        for y in range(im.size[1]):
            rgb_data[x].append(pix[x,y])
    return rgb_data
    # print(rgb_data[x][y])

rgb_data = get_rgba("main.jpg")
print(rgb_data[0][0])
