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

class FileDialogDemo(EasyFrame):
    def __init__(self):
        """Sets up the window and widgets."""
        EasyFrame.__init__(self, title="File Dialog Demo")
        self.addButton(text="Select Folder", row=0, column=0, command=self.selectFolder)

    def selectFolder(self):
        """Select a folder and process all images inside it."""
        folder_path = tkinter.filedialog.askdirectory(parent=self)

        if folder_path:
            print("Selected folder:", folder_path)
            self.processFolder(folder_path)
        else:
            print("No folder selected.")

    def processFolder(self, folder_path):
        # output folder to save processed images
        output_folder = 'C:/Users/evafa/OneDrive/Desktop/Research/processed_images/'
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
            # optional plots image
            # plt.imshow(imgar)
            # plt.show()
            img2 = Image.fromarray(smooth)                              # converts array to pillow image object
            save_path = os.path.join(output_folder, f"Image_{i}.jpeg")  # new image path to be saved
            img2.save(save_path)                                        # saves new image to output folder
                                        
            i += 1
        print('Complete.')
        
def main():
    FileDialogDemo().mainloop()

if __name__ == "__main__":
    main()
