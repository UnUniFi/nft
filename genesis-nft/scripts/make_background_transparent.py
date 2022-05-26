from PIL import Image

width = 940
height = 1024

src = Image.open('src/blue-greenback.png')
startImageHeightList = []

originPixel = src.getpixel((0,0))

for x in range(width):
  startImageHeight = 0
  for y in range(int(height/2)):
    pixel = src.getpixel((x, y))
    if originPixel == pixel:
      startImageHeight = y + 1
      continue
    else:
      break
    
  startImageHeightList.append(startImageHeight)

latterBlankStartList = []
for x in range(width):
  latterStartImageHeight = 0
  for y in range(int(height/2)):
    h = 1023 - y
    pixel = src.getpixel((x, h))
    if pixel == originPixel:
      latterStartImageHeight = h - 1
      continue
    else:
      break
    
  latterBlankStartList.append(latterStartImageHeight)

for i in range(256):
  # put appropriate folder name contains reading images
  src = Image.open('dst_iamges/' + str(i) + '.png')

  newImage = Image.new('RGBA', (width, height), (0,0,0,1))
  for x in range(width):
    for y in range(height):
      pixel = src.getpixel((x, y))
      if y < startImageHeightList[x] or y > latterBlankStartList[x]:
        continue

      newImage.putpixel((x,y), pixel)
  
  # put target folder name to export image files
  newImage.save('dst_target/' + str(i) + '.png')

print("Finished.")
