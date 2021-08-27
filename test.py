1 #Morse Code Translator
2 #Icon found from http://icons8.com
3 import tkinter
4 from tkinter import IntVar, END, DISABLED, NORMAL
5 from playsound import playsound
6 from PIL import ImageTk, Image
7
8 #Define window
9 root = tkinter.Tk()
10 root.title('Morse Code Translator')
11 root.iconbitmap('morse.ico')
12 root.geometry('500x350')
13 root.resizable(0,0)
14
15 #Define fonts colors
16 button_font = ('SimSun', 10)
17 root_color = "#778899"
18 frame_color = "#dcdcdc"
19 button_color = "#c0c0c0"
20 text_color = "#f8f8ff"
21 root.config(bg=root_color)
22
23 #Define funtions
24 def convert():
25 """Call the appropriate conversion function based off radio button values"""
26 #English to morse code:
27 if language.get() == 1:
28 get_morse()
29 elif language.get() == 2:
30 get_english()
31
32
33 def get_morse():
34 """Convert an English message to morse code"""
35 #String to hold morse code message
36 morse_code = ""
37
38 #Get the input text and standardize it to lower case
39 text = input_text.get("1.0", END)
40 text = text.lower()
41
42 #Remove any letters of symbols not in our dict keys
43 for letter in text:
44 if letter not in english_to_morse.keys():
45 text = text.replace(letter, '')
46
47 #Break up into individual words based on space " " and put into a list
48 word_list = text.split(" ")
49
50 #Turn each individual word in word_list into a list of letters
51 for word in word_list:
52 letters = list(word)
53 #For each letter, get the morse code representation and append it to the string
morse_code
54 for letter in letters:
55 morse_char = english_to_morse[letter]
56 morse_code += morse_char
57 #Seperate individual letters with a space
58 morse_code += " "
59 #Seperate individual words with a |
60 morse_code += "|"
61
62 output_text.insert("1.0", morse_code)
63
64
65 def get_english():
66 """Convert a morse code message to english"""
67 #String to hold English message
68 english = ""
69
70 #Get the input text
71 text = input_text.get("1.0", END)
72
73 #Remove any letters or symbols not in our dict keys
74 for letter in text:
75 if letter not in morse_to_english.keys():
76 text = text.replace(letter, '')
77
78 #Break up each word based on | and put into a list
79 word_list = text.split("|")
80
81 #Turn each word into a list of letters
82 for word in word_list:
83 letters = word.split(" ")
84 #For each letter, get the English representation and add it to the string English
85 for letter in letters:
86 english_char = morse_to_english[letter]
87 english += english_char
88 #seperate individual words with a space
89 english += " "
90
91 output_text.insert("1.0", english)
92
93
94 def clear():
95 """Clear both text fields"""
96 input_text.delete("1.0", END)
97 output_text.delete("1.0", END)
98
99
100 def play():
101 """Play tones for corresponding dots and dashes"""
102 #Determine where the morse code is
103 if language.get() == 1:
104 text = output_text.get("1.0", END)
105 elif language.get() == 2:
106 text = input_text.get("1.0", END)
107
108 #Play the tones (., -, " " , |)
109 for value in text:
110 if value == ".":
111 playsound('dot.mp3')
112 root.after(100)
113 elif value == "-":
114 playsound('dash.mp3')
115 root.after(200)
116 elif value == " ":
117 root.after(300)
118 elif value == "|":
119 root.after(700)
120
121
122 def show_guide():
123 """Show a morse code guide in a second window"""
124 #Image 'morse' needs to be a global variable to put on our window
125 #Window 'guide' needs to be global to close in another function.
126 global morse
127 global guide
128
129 #Create second window relative to the root window
130 guide = tkinter.Toplevel()
131 guide.title("Morse Guide")
132 guide.iconbitmap('morse.ico')
133 guide.geometry('350x350+'+ str(root.winfo_x()+500) + "+" + str(root.winfo_y()))
134 guide.config(bg=root_color)
135
136 #Create the image, label, and pack
137 morse = ImageTk.PhotoImage(Image.open('morse_chart.jpg'))
138 label = tkinter.Label(guide, image=morse, bg=frame_color)
139 label.pack(padx=10, pady=10, ipadx=5, ipady=5)
140
141 #Create a close button
142 close_button = tkinter.Button(guide, text="Close", font=button_font,
bg=button_color, command=hide_guide)
143 close_button.pack(padx=10, ipadx=50)
144
145 #Disabel the guide button
146 guide_button.config(state=DISABLED)
147
148
149 def hide_guide():
150 """Hide the guide"""
151 guide_button.config(state=NORMAL)
152 guide.destroy()
153
154
155 #Create our morse code dictionaries
156 english_to_morse = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..',
157 'e': '.', 'f': '..-.', 'g': '--.', 'h': '....',
158 'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..',
159 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.',
160 'q': '--.-', 'r': '.-.', 's': '...', 't': '-',
161 'u': '..--', 'v': '...-', 'w': '.--', 'x': '-..-',
162 'y': '-.--', 'z': '--..', '1': '.----',
163 '2': '..---', '3': '...--', '4': '....-', '5': '.....',
164 '6': '-....', '7': '--...', '8': '---..', '9': '----.',
165 '0': '-----', ' ':' ', '|':'|', "":"" }
166
167 morse_to_english = dict([(value, key) for key, value in english_to_morse.items()])
168
169 #Define layout
170 #Create frames
171 input_frame = tkinter.LabelFrame(root, bg=frame_color)
172 output_frame = tkinter.LabelFrame(root, bg=frame_color)
173 input_frame.pack(padx=16, pady=(16,8))
174 output_frame.pack(padx=16, pady=(8,16))
175
176 #Layout for the input frame
177 input_text = tkinter.Text(input_frame, height=8, width=30, bg=text_color)
178 input_text.grid(row=0, column=1, rowspan=3, padx=5, pady=5)
179
180 language = IntVar()
181 language.set(1)
182 morse_button = tkinter.Radiobutton(input_frame, text="English --> Morse Code",
variable=language, value=1, font=button_font, bg=frame_color)
183 english_button = tkinter.Radiobutton(input_frame, text="Morse Code --> English",
variable=language, value=2, font=button_font, bg=frame_color)
184 guide_button = tkinter.Button(input_frame, text="Guide", font=button_font,
bg=button_color, command=show_guide)
185
186 morse_button.grid(row=0, column=0, pady=(15,0))
187 english_button.grid(row=1, column=0)
188 guide_button.grid(row=2, column=0, sticky="WE", padx=10)
189
190 #Layout for the output frame
191 output_text = tkinter.Text(output_frame, height=8, width=30, bg=text_color)
192 output_text.grid(row=0, column=1, rowspan=4, padx=5, pady=5)
193
194 convert_button = tkinter.Button(output_frame, text="Convert", font=button_font,
bg=button_color, command=convert)
195 play_button = tkinter.Button(output_frame, text="Play Morse", font=button_font,
bg=button_color, command=play)
196 clear_button = tkinter.Button(output_frame, text="Clear", font=button_font,
bg=button_color, command=clear)
197 quit_button = tkinter.Button(output_frame, text="Quit", font=button_font,
bg=button_color, command=root.destroy)
198 convert_button.grid(row=0, column=0, padx=10, ipadx=50) #convert ipadx defines column
width
199 play_button.grid(row=1, column=0, padx=10, sticky="WE")
200 clear_button.grid(row=2, column=0, padx=10, sticky="WE")
201 quit_button.grid(row=3, column=0, padx=10, sticky="WE")
202
203 #Run the root window's main loop
204 root.mainloop()