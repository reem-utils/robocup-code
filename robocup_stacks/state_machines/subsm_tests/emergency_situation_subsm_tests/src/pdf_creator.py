# Sample platypus document
# From the FAQ at reportlab.org/oss/rl-toolkit/faq/#1.1

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.rl_config import defaultPageSize
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas

PAGE_HEIGHT=defaultPageSize[1]
PAGE_WIDTH=defaultPageSize[0]
styles = getSampleStyleSheet()
Title = "EMERGENCY SITUATION FROM REEM"
pageinfo = ""

# def myFirstPage(canvas, doc,file_location):
#     canvas.saveState()
#     canvas.setFont('Times-Bold',16)
#     canvas.drawCentredString(PAGE_WIDTH/2.0, PAGE_HEIGHT-108, Title)
#     canvas.setFont('Times-Roman',9)
#     canvas.drawImage(file_location+"map_with_cross.png")
#     canvas.restoreState()
    
'''
def myLaterPages(canvas, doc):
    canvas.saveState()
    canvas.setFont('Times-Roman', 9)
    # canvas.drawString(inch, 0.75 * inch,"Page %d %s" % (doc.page, pageinfo))
    canvas.restoreState()

'''
def create_pdf(file_location):
    doc = SimpleDocTemplate(file_location+'reem2.pdf')
    Story = []
    style = styles["Normal"]
    bogustext = ("There is an emergency situation in kitchen.")
    p = Paragraph(bogustext, style)
    im=Image(file_location+"map_with_cross.png")
    Story.append(p)
    Story.append(Spacer(1, 12))
    Story.append(im)
    Story.append(Spacer(1,0.2*inch))
    doc.build(Story)

# create_pdf('chen')

# if __name__=='__main__':
#     create_pdf('something')
    