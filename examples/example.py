# import libraries
from st7920 import ST7920
import time
from PIL import Image

# setup display
lcd = ST7920(spi_bus=0, spi_device=0)

# activate cursor
lcd.display_on(cursor=True)
# set cursor to (0,0)
lcd.home()
# write text
lcd.write_text("Line 1")
time.sleep(2)

# actiavte blinking cursor
lcd.display_on(cursor=True, blink=True)
# write text at (1,0)
lcd.write_at(1, 0, "Line 2")
time.sleep(2)

# deactivate cursor
lcd.display_on(cursor=False)
# shift display to the right
lcd.shift_display_right()
time.sleep(1)

# shift display to the left
lcd.shift_display_left()
time.sleep(1)

# clear display
lcd.clear()
# set cursor to home
lcd.home()
time.sleep(1)

# load example picture
image = Image.open("picture.bmp").convert("1")
# draw picture on display
lcd.draw_image(image)
time.sleep(5)

# clear display
lcd.clear()
# turn display off
lcd.display_off()
# close connection with display
lcd.close()