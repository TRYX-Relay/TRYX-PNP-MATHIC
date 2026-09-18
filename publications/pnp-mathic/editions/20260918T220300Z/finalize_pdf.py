import fitz
from docx import Document
p=fitz.open()
cover=fitz.open('Splash.pdf')
p.insert_pdf(cover,from_page=0,to_page=0)
src=fitz.open('Rendered_Source.pdf')
p.insert_pdf(src,from_page=1)
def spans(pg):
 return [s for b in pg.get_text('dict')['blocks'] if 'lines' in b for l in b['lines'] for s in l['spans']]
toc=[[1,'Splash',1],[1,'Title and contents',2]]
entries=[q.text for q in Document('Problem_No_Problem_Layout_Source.docx').paragraphs if q.style.name=='Heading 1' and (q.text[:1].isdigit() or q.text=='References')]
for title in entries:
 target,s=next((i,s) for i in range(2,len(p)) for s in spans(p[i]) if s['text'].strip()==title)
 e=next(s for s in spans(p[1]) if s['text']==title)
 n=str(target)
 p[1].insert_text((551-fitz.get_text_length(n,fontname='tiro',fontsize=11),e['origin'][1]),n,fontname='tiro',fontsize=11)
 r=fitz.Rect(e['bbox']);r.x1=551
 p[1].insert_link({'kind':fitz.LINK_GOTO,'from':r,'page':target,'to':fitz.Point(0,s['bbox'][1])})
 toc.append([1,title,target+1])
for i in range(1,len(p)):
 assert p[i].insert_textbox(fitz.Rect(518,758,559,775),str(i),fontname='helv',fontsize=9,align=2,color=(.35,.35,.35))>=0
p.set_toc(toc)
p.set_page_labels([{'startpage':0,'prefix':'Splash','style':''},{'startpage':1,'prefix':'','style':'D','firstpagenum':1}])
p.set_metadata({'title':'Problem No Problem','author':'Virgil Lee Gattenby'})
p.save('Rebuilt_Paginated.pdf',garbage=4,deflate=True)
p.close()
p=fitz.open('Rebuilt_Paginated.pdf')
for i in range(2,len(p)):
 assert p[i].get_pixmap(clip=fitz.Rect(0,0,612,750)).samples==src[i].get_pixmap(clip=fitz.Rect(0,0,612,750)).samples
