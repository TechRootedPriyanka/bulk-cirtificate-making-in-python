import xlrd
import smtplib
import os
import sys
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

# Meant to convert full names to abbreviations
def shorten( text, _max ):
    t = text.split(" ")
    text = ''
    if len(t)>1:
        for i in t[:-1]:
            text += i[0] + '.'
    text += ' ' + t[-1]
    if len(text) < _max :
        return text
    else :
        return -1

# Add name, institute and project to certificate
def make_certi( ID, name, institute, project ):
    img = Image.open("...\\Template.jpg") #image path here
    draw = ImageDraw.Draw(img)
    # Load font
    font = ImageFont.truetype("...\\Lato-Black.ttf", 60) # To change font size & font style

    # Check sizes and if it is possible to abbreviate
    # if not the IDs are added to an error list
    if ( len( name ) > 30 ):
        name = shorten( name, 30 )
    if ( len( institute ) > 30 ):
        institute = shorten( institute, 30 )
    if ( len( project ) > 20 ):
        project = shorten( project, 20 )

    if name == -1 or project == -1 or institute == -1 :
        return -1
    else:
        # Insert text into image template
        draw.text( (729, 729), name, (0,0,0), font=font )     #to edit location and color
        #draw.text( (600, 580), institute, (0,0,255), font=font )  #for instute
        #draw.text( (450, 685), project, (0,0,255), font=font )    #for project

        if not os.path.exists( '...\\certificates' ) :    # store the certi
            os.makedirs( '...\\certificates' )

        # Save as a PDF
        img.save( 'certificates\\'+str(ID)+'.pdf', "PDF", resolution=100.0)
        return 'certificates\\'+str(ID)+'.pdf'

# Email the certificate as an attachment


if __name__ == "__main__":
    error_list = []
    error_count = 0

    os.chdir(os.path.dirname(os.path.abspath((sys.argv[0]))))

    # Read data from an excel sheet from row 2
    Book = xlrd.open_workbook('...\\List.xlsx')   # list of name
    WorkSheet = Book.sheet_by_name('Sheet1')
    """
My added  code
    """


    """
My added  code
    """
    num_row = WorkSheet.nrows - 1
    row = 0

    while row < num_row:
        row += 1
        
        ID = WorkSheet.cell_value( row, 0 )
        name = WorkSheet.cell_value( row, 1 )
        institute = WorkSheet.cell_value( row, 2 )
        receiver = WorkSheet.cell_value( row, 3 )
        project = WorkSheet.cell_value( row, 4 )
        
        # Make certificate and check if it was successful
        filename = make_certi( ID, name, institute, project )
        
        # Successfully made certificate
        if filename != -1:
            #email_certi( filename, receiver )
            print ("Sent to " + ID)
        # Add to error list
        else:
            error_list.append( ID )
            error_count += 1

    # Print all failed IDs
    print (str(error_count) + " Errors- List:" + ','.join(error_list))
