from PIL import Image
from PIL import ImageOps
import pytesseract
from pdf2image import convert_from_path
import csv
import os
import fnmatch

def process_images(image):
            
        # Recognize the text as string in image using pytesserct
        text = str((pytesseract.image_to_string(image)))
        #Deletes /n and /x0c characters
        text = text.replace('\n', '')
        text = text.replace('\x0c', '')
        #As some characters don't show up if they are to high in the image, in case there is
        # a blank space, it checks if by centering the image it shows it
        if len(text) < 1: 
            new_image = ImageOps.crop(image,(0,0,200,30))
            text = str((pytesseract.image_to_string(new_image)))
        return text

def append_text(start_num, end_num):
        for i in range (start_num,end_num):
            
            # Setting the points for cropped image
            left = 0
            top = i*height/60 + i-9
            right = width 
            bottom = height/60 + i*(height/60) + i-9
            # Cropped image of above dimension
            # (It will not change original image)
            img = page.crop((left, top, right, bottom))
            


            width_1, height_1 = img.size
            
            for j in (0,1,2,4.4):
                # Setting the points for cropped image
                left = j*(width_1/5)
                top = 0
                right = width_1/5 + j*(width_1/5) 
                bottom = height_1
                 
                # Cropped image of above dimension
                # (It will not change original image)
                
                cropped_img = img.crop((left, top, right, bottom))

                text = process_images(cropped_img)
                
                #Append text in corresponding lists
                if j==0:
                    date.append(text)
                elif j==1:
                    trans_type.append(text)
                elif j==2:
                    means_of_transp.append(text)
                elif j==4.4:
                    value.append(text)

#Path of the pdf

PDF_file = [f for f in os.listdir(os.getcwd()) if fnmatch.fnmatch(f, '*.pdf')][0] 

# Store all the pages of the PDF in a variable
pages = convert_from_path(PDF_file, 500)

#Create lists for categories
date = []
time = []
trans_type = []
means_of_transp = []
value = []

image_counter = 1

for page in pages:
    
    # Size of the image in pixels (size of original image)  
    width, height = page.size

    #As the first image is different for the rest, I need to use different crop areas
    if image_counter==1:
        append_text(9, 56)
        
            
    else:
        append_text(3, 56)
        
    
    image_counter = image_counter + 1



  #Creates a csv file            
if __name__ == '__main__':
    with open('sube.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Date', 'Transaction Type', 'Means of Transportation', 'Value'])
        i=0
        while i<=len(trans_type)-1 and i<=len(date)-1 and i<=len(means_of_transp)-1 and i<=len(value)-1:
            writer.writerow([date[i],trans_type[i], means_of_transp[i], value[i]])
            i = i+1

