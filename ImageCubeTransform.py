from PIL import Image
import os

matrices = [((1, 0, 0), (0, 1, 0), (0, 0, 1)), ((1, 0, 0), (0, 0, 1), (0, 1, 0)), ((0, 1, 0), (1, 0, 0), (0, 0, 1)), ((0, 1, 0), (0, 0, 1), (1, 0, 0)), ((0, 0, 1), (1, 0, 0), (0, 1, 0)), ((0, 0, 1), (0, 1, 0), (1, 0, 0)), ((1, 0, 0), (0, 1, 0), (0, 0, -1)), ((1, 0, 0), (0, -1, 0), (0, 0, 1)), ((-1, 0, 0), (0, 1, 0), (0, 0, 1)), ((1, 0, 0), (0, 0, 1), (0, -1, 0)), ((1, 0, 0), (0, 0, -1), (0, 1, 0)), ((-1, 0, 0), (0, 0, 1), (0, 1, 0)), ((0, 1, 0), (1, 0, 0), (0, 0, -1)), ((0, 1, 0), (-1, 0, 0), (0, 0, 1)), ((0, -1, 0), (1, 0, 0), (0, 0, 1)), ((0, 1, 0), (0, 0, 1), (-1, 0, 0)), ((0, 1, 0), (0, 0, -1), (1, 0, 0)), ((0, -1, 0), (0, 0, 1), (1, 0, 0)), ((0, 0, 1), (1, 0, 0), (0, -1, 0)), ((0, 0, 1), (-1, 0, 0), (0, 1, 0)), ((0, 0, -1), (1, 0, 0), (0, 1, 0)), ((0, 0, 1), (0, 1, 0), (-1, 0, 0)), ((0, 0, 1), (0, -1, 0), (1, 0, 0)), ((0, 0, -1), (0, 1, 0), (1, 0, 0)), ((1, 0, 0), (0, -1, 0), (0, 0, -1)), ((-1, 0, 0), (0, 1, 0), (0, 0, -1)), ((-1, 0, 0), (0, -1, 0), (0, 0, 1)), ((1, 0, 0), (0, 0, -1), (0, -1, 0)), ((-1, 0, 0), (0, 0, 1), (0, -1, 0)), ((-1, 0, 0), (0, 0, -1), (0, 1, 0)), ((0, 1, 0), (-1, 0, 0), (0, 0, -1)), ((0, -1, 0), (1, 0, 0), (0, 0, -1)), ((0, -1, 0), (-1, 0, 0), (0, 0, 1)), ((0, 1, 0), (0, 0, -1), (-1, 0, 0)), ((0, -1, 0), (0, 0, 1), (-1, 0, 0)), ((0, -1, 0), (0, 0, -1), (1, 0, 0)), ((0, 0, 1), (-1, 0, 0), (0, -1, 0)), ((0, 0, -1), (1, 0, 0), (0, -1, 0)), ((0, 0, -1), (-1, 0, 0), (0, 1, 0)), ((0, 0, 1), (0, -1, 0), (-1, 0, 0)), ((0, 0, -1), (0, 1, 0), (-1, 0, 0)), ((0, 0, -1), (0, -1, 0), (1, 0, 0)), ((-1, 0, 0), (0, -1, 0), (0, 0, -1)), ((-1, 0, 0), (0, 0, -1), (0, -1, 0)), ((0, -1, 0), (-1, 0, 0), (0, 0, -1)), ((0, -1, 0), (0, 0, -1), (-1, 0, 0)), ((0, 0, -1), (-1, 0, 0), (0, -1, 0)), ((0, 0, -1), (0, -1, 0), (-1, 0, 0))]

def applyTransformation(image,mat):
    colors = image.getcolors(image.width*image.height)

    lookup = {}
    for x in colors:
        rgb = x[1]
        out = transform(mat,rgb)
        lookup[rgb] = out
    
    for x in range(image.width):
        for y in range(image.height):
            pix = image.getpixel((x,y))
            image.putpixel((x,y), lookup[pix])


def main():
    path = input("File location to be transformed: ")
    dirname = os.path.dirname(path)
    file = os.path.split(path)[-1]
    os.chdir(dirname)
    img = Image.open(file)
    transNum = int(input("What transformation would you like to use? [1-48]")) + 1

    applyTransformation(img,matrices[transNum])

    img.show()

    img.save(file[:-4]+str(transNum)+".png")
    img.close()

    
    
def transform(mat,pixel):
    pixel = [x - 128 for x in pixel]
    
    r = pixel[0] * mat[0][0] + pixel[1] * mat[0][1] + pixel[2] * mat[0][2]
    g = pixel[0] * mat[1][0] + pixel[1] * mat[1][1] + pixel[2] * mat[1][2]
    b = pixel[0] * mat[2][0] + pixel[1] * mat[2][1] + pixel[2] * mat[2][2]
    return (r+128,g+128,b+128)

def permutefile():
    path = input("File location to be transformed: ")
    dirname = os.path.dirname(path)
    file = os.path.split(path)[-1]
    os.chdir(dirname)
    img = Image.open(file)
    img.show()
    if not os.path.exists(file[:-4]):
        os.mkdir(file[:-4])
    os.chdir(file[:-4])

    colors = img.getcolors(img.width*img.height)
    print("Saving an average of", sum(x[0] for x in colors)/len(colors), " computations over", len(colors), "unique colors.")
    
    for x in range(48):
        out = img.copy()
        applyTransformation(out,matrices[x])
        out.save(file[:-4]+str(x)+".png")
    img.close()

def topSix(path = None):
    if path == None:
        path = input("File location to be transformed: ")
    dirname = os.path.dirname(path)
    file = os.path.split(path)[-1]
    if dirname != "":
        os.chdir(dirname)
    img = Image.open(file)
    img.show()
    if not os.path.exists(file[:-4]):
        os.mkdir(file[:-4])
    os.chdir(file[:-4])

    colors = img.getcolors(img.width*img.height)
    print("Saving an average of", sum(x[0] for x in colors)/len(colors), " computations over", len(colors), "unique colors.")
    
    for x in range(6):
        out = img.copy()
        if x != 0:
            applyTransformation(out,matrices[x])
        out.save(file[:-4]+str(x)+".png")
    img.close()
    os.chdir("..")
