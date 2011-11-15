import markdown

txt = editor.getTextRange(0, (editor.getLength()-1))

cp = editor.getCodePage()

if cp == 65001:
	enc = 'utf-8'
	
else:
	enc = 'cp1250'

txt = txt.decode(enc)
	
html = markdown.markdown(txt).encode('utf-8')

editor.selectAll()
editor.replaceSel(html.decode('utf-8').encode(enc))