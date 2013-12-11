#! /usr/bin/env python

# import Image from PIL http://www.pythonware.com/library/pil/handbook/introduction.htm
import Image

def ImageCreator(location_list,origin,scale,image_name,pkg_path,image_path):
	pixels=[]
	moved_origin=[]
	i=0

	for locations in location_list:
		moved_origin=([locations[0]+origin[0], locations[1]+origin[1]])
		pixels.append([moved_origin[0]*scale, moved_origin[1]*scale])

	print "Opening images"
	img_map = Image.open(image_path+image_name)
	img_cross = Image.open(pkg_path+"/config/cross.png")
	print "Resizing cross"
	resized_cross = img_cross.resize((25,25))

	while i < len(pixels):
		print "Pasting the cross over the image"
		img_map.paste(resized_cross, (int(pixels[i][0]), int(pixels[i][1])))
		print str(int(pixels[i][0]))+" , "+str(int(pixels[i][1]))
		i = i + 1
	
	img_map.save(pkg_path+"/config/map_with_cross.png")

	print "Image is ready"