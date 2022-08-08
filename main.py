from tkinter.ttk import Combobox
import qrcode as qr
from tkinter import *

win = Tk()
window_height = 350
window_width = 500
screen_width = win.winfo_screenwidth()
screen_height = win.winfo_screenheight()
x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2) - 50) 
url_var = StringVar()
out_var = StringVar()
colour_var = StringVar()
colour_bg_var = StringVar()
qr = qr.QRCode(version = 1, box_size = 10, border = 5)

def save_btn_func():
    qr.add_data(url_var.get())
    qr.make(fit = True)
    img = qr.make_image(fill_color = colour_var.get(),
                        back_color = colour_bg_var.get())
    img.save(f'{out_var.get()}.png')

# URL
target_label = Label(win, text='Target Url -', font=('calibre',15,'bold'))
target_label.grid(row=1, column=1, padx=10, pady=10)
url_entry = Entry(win, width=40,textvariable=url_var, font=('calibre',10,'italic'), bd=3)
url_entry.grid(row=1, column=2, padx=5, pady=10)

# URL Colour Selector
clr_select_lbl = Label(win, text='Select QRcode Colour - ')
clr_select_lbl.grid(row=2, column=1, pady=10, padx=10)

choose_colour = Combobox(win, textvariable = colour_var)
choose_colour.set('Black')
choose_colour['values'] = ('White' ,'Black', 'Red', 'Green', 'Blue', 'Grey')
choose_colour['state'] = 'readonly'
choose_colour.grid(row=2, column=2, padx=10, pady=10)

# URL Bg Selector
clr_select_lbl_bg = Label(win, text='Select QRcode BG Colour - ')
clr_select_lbl_bg.grid(row=3, column=1, pady=10, padx=10)

choose_colour_bg = Combobox(win, textvariable = colour_bg_var)
choose_colour_bg.set('Black')
choose_colour_bg['values'] = ('White', 'Black', 'Red', 'Green', 'Blue', 'Grey')
choose_colour_bg['state'] = 'readonly'
choose_colour_bg.grid(row=3, column=2, padx=10, pady=10)

# Output filename
out_label = Label(win, text='Output File Name', font=('calibre',15,'bold'))
out_label.grid(row=4, column=1, padx=10, pady=10)
output_file_name = Entry(win, width=40,textvariable=out_var, font=('calibre',10,'italic'), bd=3)
output_file_name.grid(row=4, column=2, padx=10, pady=10)

# Save button
save_btn = Button(win, text='Save Image', font=('calibre',10,'bold'), command=save_btn_func)
save_btn.grid(row=5, column=2)

# Window Settings
win.resizable(False, False)
win.geometry(f"{window_width}x{window_height}+{x_cordinate}+{y_cordinate}")
win.title('QR Code Generator')
win.mainloop()