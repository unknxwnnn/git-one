import tkinter
from tkcalendar import DateEntry

root = tkinter.Tk()
root.title('APOD Photo Viewer')
root.iconbitmap('rocket.ico')

text_font = ('Times New Roman', 14)
nasa_blue = "#043c93"
nasa_light_blue = "#7aa5d3"
nasa_red = "#ff1923"
nasa_white = "#ffffff"
root.config(bg=nasa_blue)

input_frame = tkinter.Frame(root, bg=nasa_blue)
output_frame = tkinter.Frame(root, bg=nasa_blue)
input_frame.pack()
output_frame.pack(padx=50, pady=(0,25))

calendar = DateEntry(input_frame, width=10, font=text_font, background=nasa_blue, foreground=nasa_white)
submit_button = tkinter.Button(input_frame, text="Submit", font=text_font, bg=nasa_light_blue)
full_button = tkinter.Button(input_frame, text="Full Photo", font=text_font, bg=nasa_light_blue)
save_button = tkinter.Button(input_frame, text="Save Photo", font=text_font, bg=nasa_light_blue)
quit_button = tkinter.Button(input_frame, text="Exit", font=text_font, bg=nasa_red, command=root.destroy)

calendar.grid(row=0, column=0, padx=5, pady=10)
submit_button.grid(row=0, column=1, padx=5, pady=10, ipadx=35)
full_button.grid(row=0, column=2, padx=5, pady=10, ipadx=25)
save_button.grid(row=0, column=3, padx=5, pady=10, ipadx=25)
quit_button.grid(row=0, column=4, padx=5, pady=10, ipadx=25)

picture_data = tkinter.Label(output_frame, text='testing')
picture_explanation = tkinter.Label(output_frame, text="testing")
picture_label = tkinter.Label(output_frame, text='testing')

picture_data.grid()
picture_explanation.grid()
picture_label.grid()


root.mainloop()
