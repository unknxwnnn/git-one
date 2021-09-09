import tkinter
from tkinter import BOTH, IntVar

root = tkinter.Tk()
root.title('Weather Forecast')
root.iconbitmap('weather.ico')
root.geometry('400x400')
root.resizable(0, 0)

sky_color = "#76c3ef"
grass_color = "#aad207"
output_color = "#dcf0fb"
input_color = "#ecf2ae"
large_font = ("SimSun", 14)
small_font = ("SimSun", 10)


sky_frame = tkinter.Frame(root, bg=sky_color, height=250)
grass_frame = tkinter.Frame(root, bg=grass_color)
sky_frame.pack(fill=BOTH, expand=True)
grass_frame.pack(fill=BOTH, expand=True)

output_frame = tkinter.LabelFrame(sky_frame, bg=output_color, width=325, height=225)
input_frame = tkinter.LabelFrame(grass_frame, bg=input_color, width=325)
output_frame.pack(pady=30)
output_frame.pack_propagate(0)
input_frame.pack(pady=15)


city_info_label = tkinter.Label(output_frame, bg=output_color, text='Testing')
weather_label = tkinter.Label(output_frame, bg=output_color, text='Testing')
temp_label = tkinter.Label(output_frame, bg=output_color, text='Testing')
feel_label = tkinter.Label(output_frame, bg=output_color, text='Testing')
temp_min_label = tkinter.Label(output_frame, bg=output_color, text='Testing')
temp_max_label = tkinter.Label(output_frame, bg=output_color, text='Testing')
humidity_label = tkinter.Label(output_frame, bg=output_color, text='Testing')
photo_label = tkinter.Label(output_frame, bg=output_color, text='Testing')


city_info_label.pack(pady=8)
weather_label.pack()
temp_label.pack()
feel_label.pack()
temp_min_label.pack()
temp_max_label.pack()
humidity_label.pack()
photo_label.pack(pady=8)

city_entry = tkinter.Entry(input_frame, width=20, font=large_font)
submit_button = tkinter.Button(input_frame, text='Submit', font=large_font, bg=input_color)

search_method = IntVar()
search_method.set(1)
search_city = tkinter.Radiobutton(input_frame, text='Search by city name', variable=search_method, value=1, font=small_font, bg=input_color)
search_zip = tkinter.Radiobutton(input_frame, text="Search by zip code", variable=search_method, value=2, font=small_font, bg=input_color)

city_entry.grid(row=0, column=0, padx=10, pady=(10,0))
submit_button.grid(row=0, column=1, padx=10, pady=(10,0))
search_city.grid(row=1, column=0, pady=2)
search_zip.grid(row=1, column=1, padx=5, pady=2)

root.mainloop()
