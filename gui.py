import io
import tkinter as tk
import urllib.request
from PIL import ImageTk, Image

        

def value_1():
    global x
    x = 1
    root.destroy()

def value_2():
    global x
    x = 2
    root.destroy()

def value_3():
    global x 
    x = 3
    root.destroy()

def value_4():
    global x
    x = 4
    root.destroy()

def value_5():
    global x
    x = 5
    root.destroy()
    
def value_6():
    global x
    x = 6 
    root.destroy()          
# Create the main window
root = tk.Tk()

# Set the window title
root.title("AI-Personal-Trainer")
root.configure(background='blue')
root.geometry("1900x1080")

# Create the label widget
label = tk.Label(root, text="Choose Exercise", font=("Arial", 32))
label.grid(row=1, column=1, pady=20)

img = Image.open("C:/Users/akash/Documents/AI-PROJECT/images/img.png")
img = ImageTk.PhotoImage(img)
label1 = tk.Label(root, image=img,width=200,height=200)
label1.grid(row=3, column=1, pady=20)
label1.pack

label2 = tk.Label(root, text="Trainer", font=("Arial", 20), background="cyan")
label2.grid(row=4, column=1, pady=0)

# Download the images from URLs
url1 = "file:///C:/Users/akash/Documents/AI-PROJECT/images/image1.png"
url2 = "file:///C:/Users/akash/Documents/AI-PROJECT/images/image2.png"
url3 = "file:///C:/Users/akash/Documents/AI-PROJECT/images/image3.png"
url4 = "file:///C:/Users/akash/Documents/AI-PROJECT/images/image4.png"
url5 = "file:///C:/Users/akash/Documents/AI-PROJECT/images/image5.png"
url6 = "file:///C:/Users/akash/Documents/AI-PROJECT/images/image6.png"
with urllib.request.urlopen(url1) as u:
    image1_data = u.read()
image1 = ImageTk.PhotoImage(Image.open(io.BytesIO(image1_data)))

with urllib.request.urlopen(url2) as u:
    image2_data = u.read()
image2 = ImageTk.PhotoImage(Image.open(io.BytesIO(image2_data)))

with urllib.request.urlopen(url3) as u:
    image3_data = u.read()
image3 = ImageTk.PhotoImage(Image.open(io.BytesIO(image3_data)))

with urllib.request.urlopen(url4) as u:
    image4_data = u.read()
image4 = ImageTk.PhotoImage(Image.open(io.BytesIO(image4_data)))

with urllib.request.urlopen(url5) as u:
    image5_data = u.read()
image5 = ImageTk.PhotoImage(Image.open(io.BytesIO(image5_data)))

with urllib.request.urlopen(url6) as u:
    image6_data = u.read()
image6 = ImageTk.PhotoImage(Image.open(io.BytesIO(image6_data)))

# Create the button widgets with images
button1 = tk.Button(root, image=image1, width=400, height=200 ,borderwidth=4,command=value_1)
button2 = tk.Button(root, image=image2, width=400, height=200 ,borderwidth=4,command=value_2)
button3 = tk.Button(root, image=image3, width=400, height=200 ,borderwidth=4,command=value_3)
button4 = tk.Button(root, image=image4, width=400, height=200 ,borderwidth=4,command=value_4)
button5 = tk.Button(root, image=image5, width=400, height=200 ,borderwidth=4,command=value_5)
button6 = tk.Button(root, image=image6, width=400, height=200 ,borderwidth=4,command=value_6)

# Place the buttons in a grid layout
button1.grid(row=2, column=2, padx=80, pady=20)
button2.grid(row=2, column=3, padx=80, pady=20)
button3.grid(row=3, column=2, padx=80, pady=10)
button4.grid(row=3, column=3, padx=80, pady=10)
button5.grid(row=4, column=2, padx=80, pady=10)
button6.grid(row=4, column=3, padx=80, pady=10)

# Center the label and buttons horizontally
root.grid_columnconfigure(0, weight=1)
label.grid(sticky="ew")
button1.grid(sticky="ew")
button2.grid(sticky="ew")
button3.grid(sticky="ew")
button4.grid(sticky="ew")
button5.grid(sticky="ew")
button6.grid(sticky="ew")


# Start the main event loop
root.mainloop()