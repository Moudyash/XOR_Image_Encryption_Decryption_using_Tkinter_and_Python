import tkinter as tk
import os
from tkinter import filedialog
from tkinter import messagebox
from tkinter import PhotoImage
import time

key = 25

# Encrypt function
def encrypt():
    # Open a file dialog to choose the image to encrypt
    path = filedialog.askopenfilename()

    # try block to handle exception
    try:

        # open file for reading purpose
        fin = open(path, 'rb')

        # storing image data in variable "image"
        image = fin.read()
        fin.close()

        # converting image into byte array to
        # perform encryption easily on numeric data
        image = bytearray(image)

        # performing XOR operation on each value of bytearray
        for index, values in enumerate(image):
            image[index] = values ^ key

        # opening file for writing purpose
        fin = open(path, 'wb')

        # writing encrypted data in image
        fin.write(image)
        fin.close()

        file_name = os.path.basename(path)
        directory = os.path.dirname(path)

        # change file extension
        new_path = os.path.join(directory, os.path.splitext(file_name)[0] + '.bin')
        os.rename(path, new_path)








        print('Encryption Done...')
        # Show a dialog saying that the encryption is done
        messagebox.showinfo("Encryption Complete", "The image has been encrypted successfully!")
        # Return to the main screen

        show_main_screen()

    except Exception:
        print('Error caught : ', Exception.__name__)


# Decrypt function
def decrypt():
    path = filedialog.askopenfilename()

    messagebox.showinfo("Encryption Complete", "The image has been encrypted successfully!")
    # try block to handle the exception
    try:
        # take path of image as a input
        file_name = os.path.basename(path)
        directory = os.path.dirname(path)

        # change file extension
        new_path = os.path.join(directory, os.path.splitext(file_name)[0] + '.jpg')
        os.rename(path, new_path)
        # open file for reading purpose
        fin = open(new_path, 'rb')

        # storing image data in variable "image"
        image = fin.read()
        fin.close()

        # converting image into byte array to perform decryption easily on numeric data
        image = bytearray(image)

        # performing XOR operation on each value of bytearray
        for index, values in enumerate(image):
            image[index] = values ^ key

        # opening file for writing purpose
        fin = open(new_path, 'wb')

        # writing decryption data in image
        fin.write(image)
        fin.close()
        print('Decryption Done...')


    except Exception:
        print('Error caught : ', Exception.__name__)

    # Decrypt function
    show_main_screen()


def show_main_screen():
    # Clear the screen
    for widget in main_frame.winfo_children():
        widget.destroy()

    # Show the "Encrypt" button
    encrypt_button = tk.Button(main_frame, text="Encrypt", command=encrypt)
    encrypt_button.pack()

    # Show the "Decrypt" button
    decrypt_button = tk.Button(main_frame, text="Decrypt", command=decrypt)
    decrypt_button.pack()


# Show the loading screen
def show_loading_screen():
    # Clear the screen
    for widget in main_frame.winfo_children():
        widget.destroy()

    # Show the "Encrypt" button
    encrypt_button = tk.Button(main_frame, text="Encrypt", command=encrypt)
    encrypt_button.pack()

    # Show the "Decrypt" button
    decrypt_button = tk.Button(main_frame, text="Decrypt", command=decrypt)
    decrypt_button.pack()

    # Show the loading screen


def show_loading_screen():
    # Clear the screen
    for widget in main_frame.winfo_children():
        widget.destroy()

    # Show a message saying that the image is being encrypted
    message = tk.Label(main_frame, text="Encrypting image...")
    message.pack()

    # Create the main window


root = tk.Tk()
root.title("encrypto")
root.geometry("600x400")
root.minsize("600","400")
root.maxsize("1920","1080")
#root.wm_iconbitmap(r'C:\Users\Medo\Desktop\De\icon.png')
main_frame = tk.Frame(root)
main_frame.pack()

# Show the main screen
show_main_screen()

# Run the main loop
root.mainloop()

