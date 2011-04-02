#!/usr/bin/python

from Tkinter import *
import Image,ImageTk,sys,ImageFilter,os,medianfilter,threshold,operators,os,time



def main(path):


	name = os.path.basename(path)

	print "Process Started on",name
	start = time.time()

	img = Image.open(path)

	# Convert image to 8-bit if it isn't
	if img.format == 'L': im = img
	else: im = img.convert('L')

	# Threshold unblurred image
	#tm = threshold.thresh(im)

	# Use custom median filter (functional, but slow)
	#m = medianfilter.main(im)

	print "Blurring Started"
	filterstart = time.time()

	# use ImageFilter median filter
	m = im.filter(ImageFilter.MedianFilter(11))

	print "Burring Complete: Time = ",time.time()-filterstart,"ms"

	# Threshold blurred image
	t = threshold.thresh(m)

	# Save everything
	im.save("../out/3-1.jpg")
	#tm.save("../out/3-3.jpg")
	m.save("../out/3-2.jpg")
	t.save("../out/3-4.jpg")

	# Apply various edge-detection filters to the image
	for i in ['roberts']:
	#, 'sobel', 'roberts', 'scharr']:
		#x = operators.main(im, i)
		#y = operators.main(m, i)
		#z = operators.main(tm, i)
		p = operators.main(t, i)
		#x.save("../out/3-1" + i + ".jpg")
		#y.save("../out/3-2" + i + ".jpg")
		#z.save("../out/3-3" + i + ".jpg")
		p.save("../out/3-4" + i + ".jpg")

	print "Process Complete: Time = ",(time.time()-start)*1000,"ms"
	print p
	return p	

