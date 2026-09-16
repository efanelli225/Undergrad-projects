# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 16:03:40 2026

@author: evafa
"""
import os
import tkinter.filedialog
from breezypythongui import EasyFrame
import numpy as np
from PIL import Image
from scipy.ndimage import gaussian_filter

class Image_Processor(EasyFrame):
    def __init__(self):
        """Sets up the window and widgets."""
        EasyFrame.__init__(self, title="Image Processor")
        self.label = self.addLabel(text="Please select the folder your images are located in.", row=0, column=0, columnspan=1, sticky="NSEW")
        self.addButton(text="Select Folder", row=0, column=1, command=self.selectFolder)
        self.outputArea = self.addTextArea("", row=1, column=0, columnspan=2, width=60, height=10)

    def selectFolder(self):
        """Select a folder and process all images inside it."""
        folder_path = tkinter.filedialog.askdirectory(parent=self)

        if folder_path:
            self.outputArea["state"] = "normal"
            self.outputArea.setText(f"Selected folder: {folder_path}")
            self.outputArea["state"] = "disabled"
            self.processFolder(folder_path)
        else:
            self.outputArea["state"] = "normal"
            self.outputArea.setText(f"No folder selected.")
            self.outputArea["state"] = "disabled"

    def processFolder(self, folder_path):
        # Create output folder next to the input folder
        parent_dir = os.path.dirname(folder_path)
        input_name = os.path.basename(folder_path)
        output_folder = os.path.join(parent_dir, f"{input_name}_processed")
        output_folder = os.path.normpath(output_folder)
        os.makedirs(output_folder, exist_ok=True)

        i = 0                                                           # image counter
        # iterate for each image in folder
        for file in os.listdir(folder_path):
            
            image_path = os.path.join(folder_path, file)                # path to image
            
            # skips non-image files
            if not file.lower().endswith(('.png', '.jpg', '.jpeg', '.tif', '.bmp')):
                continue
            
            img1 = Image.open(image_path)                               # opens image
            imgar = np.asarray(img1).copy()                             # converts image to numpy array
            
            smooth = gaussian_filter(imgar, sigma=20)                   # smooths data
            smooth[smooth[:,:,0] > 100] = 255                           # white pixels
            smooth[smooth[:,:,0] < 100] = 0                             # black pixels
            img2 = Image.fromarray(smooth)                              # converts array to pillow image object
            save_path = os.path.join(output_folder, f"Image_{i}.jpeg")  # new image path to be saved
            img2.save(save_path)                                        # saves new image to output folder
                                        
            i += 1
            self.outputArea["state"] = "normal"
            current = self.outputArea.getText()
            self.outputArea.setText(current + f"Image {i} processed.")
            self.outputArea["state"] = "disabled"

        self.outputArea["state"] = "normal"
        current = self.outputArea.getText()
        self.outputArea.setText(current + f"Image processing complete. View your processed images at: \n{output_folder}")
        self.outputArea["state"] = "disabled"
        
def main():
    Image_Processor().mainloop()

if __name__ == "__main__":
    main()

