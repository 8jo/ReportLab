from matplotlib.tests.test_mathtext import fonts

__author__ = 'air'

#coding = gbk

from reportlab.pdfbase import pdfmetrics

from reportlab.pdfbase.cidfonts import CIDFont,CIDTypeFace,findCMapFile

enc = 'GB-EUC-H'

findCMapFile(enc)

face = CIDTypeFace('STSong-Light')

pdfmetrics.registerTypeFace(face)

pdfmetrics.registerFont(CIDFont('STSong-Light',enc))


fonts.addMapping('STSong-Light',0,0,'STSong-Light')

fonts.addMapping('STSong-Light',0,1,'STSong-Light')

fonts.addMapping('STSong-Light',1,0,'STSong-Light')

fonts.addMapping('STSong-Light',1,1,'STSong-Light')

import copy

from reportlab.platypus import Paragraph,SimpleDocTemplate,PageBreak

from reportlab.lib.styles import getSampleStyleSheet

stylesheet = getSampleStyleSheet()

normalStyle = copy.deepcopy(stylesheet['Normal'])

normalStyle.fontName = 'StSong-Light-GB-EUC-H'

normalStyle.fontSize = 20

story = []

story.append(Paragraph("<b>你好</b>,中文",normalStyle))



doc = SimpleDocTemplate(hello.pdf)

doc.build(story)

