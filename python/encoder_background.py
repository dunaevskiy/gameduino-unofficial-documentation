from PIL import Image
import gameduino
import gameduino.prep as gdprep
import gameduino.sim as gdsim

# User config
##################################################
# Choose image path and output file
filename_image = "images/encoder_background.png"
filename_output = "output/encoder_background.h"

# Parser
##################################################
(parse_image_pic, parse_image_chr, parse_image_pal) = gdprep.encode(Image.open(filename_image))
hdr = open(filename_output, "w")
gdprep.dump(hdr, "image_pic", parse_image_pic)
gdprep.dump(hdr, "image_chr", parse_image_chr)
gdprep.dump(hdr, "image_pal", parse_image_pal)

# Preview of gameduino display
##################################################
image = Image.open(filename_image).convert("RGB")
(image_pic, image_chr, image_pal) = gdprep.encode(image)
gd = gdsim.Gameduino()
gd.wrstr(gameduino.RAM_PIC, image_pic)
gd.wrstr(gameduino.RAM_CHR, image_chr)
gd.wrstr(gameduino.RAM_PAL, image_pal)
gd.im().save("preview/encoder_background_preview.png")
