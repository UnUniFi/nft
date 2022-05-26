from PIL import Image, ImageMath

width = 940
height = 1024

src = Image.open('src/yellow-greenback.png')
h, s, v = src.convert('HSV').split()

for i in range(256):
  _h = ImageMath.eval('(h + i) % 256', h=h, i=i).convert('L')
  dst = Image.merge('HSV', (_h, s, v)).convert('RGB')
  dst.save('dst_yellow_greenback/' + str(i) + '.png')
  print(dst.getpixel((0, 0)))
  

# width = 940
# height = 1024

# src = Image.open('src/blue.png')
# startImageHeightList = []

# for x in range(width):
#   startImageHeight = 0
#   for y in range(int(height/2)):
#     pixel = src.getpixel((x, y))
#     if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
#       startImageHeight = y + 1
#       continue
#     else:
#       break
    
#   startImageHeightList.append(startImageHeight)

# latterBlankStartList = []
# for x in range(width):
#   latterStartImageHeight = 0
#   for y in range(int(height/2)):
#     h = 1023 - y
#     pixel = src.getpixel((x, h))
#     if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
#       latterStartImageHeight = h - 1
#       continue
#     else:
#       break
    
#   latterBlankStartList.append(latterStartImageHeight)

# for i in range(256):
#   src = Image.open('dst_blue/' + str(i) + '.png')
#   h, s, v = src.convert('HSV').split()

#   newImage = Image.new('RGBA', (width, height), (0,0,0,0))
#   for x in range(width):
#     for y in range(height):
#       pixel = src.getpixel((x, y))
#       if y == startImageHeightList[x]:
#         print(x,y)
#         print(pixel)

#       if y < startImageHeightList[x] or y > latterBlankStartList[x]:
#         continue

#       # print(x, y)
#       # print(pixel)
#       newImage.putpixel((x,y), pixel)
  
#   newImage.save('dst_revised_blue_transparent/' + str(i) + '.png')
#   break