from pathlib import Path
from html import escape

root = Path(__file__).resolve().parent
index = root / 'index.html'
if not index.exists():
    raise SystemExit('Place this script beside the existing index.html in the GitHub Pages repository, then run it.')
s=index.read_text(encoding='utf-8')

def swap(old,new):
    global s
    if old in s:s=s.replace(old,new)
    elif new in s:pass
    else:print('Review manually: missing expected content:',old[:65])

swap('a Zambian Computer Science graduate-level developer','a Zambian final-year Computer Science student and developer')
swap('I studied Computer Science at the <strong>University of Zambia</strong>, specialising in Networking and Information Security.','I am completing my Computer Science studies at the <strong>University of Zambia</strong> (2022–2026), with a focus on Networking and Information Security.')
swap('<a href="#experience">Experience</a>','<a href="#experience">Experience</a><a href="#skills">Skills</a>')

skills={
'Networking & infrastructure':['Access Control','Internet Protocol (IP)','Network Automation','Packet Switching','Route Management','Routing Protocols','Software Defined Networking (SDN)','Wide Area Networks'],
'Cybersecurity':['Ethical Hacking','Penetration Testing','Social Engineering','Threat Management','Vulnerability Assessment','Vulnerability Scanning'],
'Cloud, AI & emerging technologies':['Amazon Web Services (AWS)','Artificial Intelligence (AI)','Generative AI','Prompt Engineering','Internet of Things (IoT)','Virtualization'],
'IT operations':['Operational Reporting','Service Quality','Uptime'],
'Development & tools':['Java','Scheme (DrRacket)','SQL','HTML5','CSS','JavaScript','Linux / Ubuntu','Windows','GitHub','Cisco Packet Tracer','ProjectLibre','Microsoft Office','Ticketing systems','Computer servicing and maintenance','Report writing and analysis']}

def tags(items):return '<div class="skill-row">'+''.join('<span class="skill">'+escape(item)+'</span>' for item in items)+'</div>'
blocks=''.join('<div class="box"><h3>'+escape(k)+'</h3>'+tags(v)+'</div>' for k,v in skills.items())
section='<section class="section" id="skills"><div class="shell"><div class="eyebrow">Credly-evidenced & practical technical skills</div><h2>Technical capabilities</h2><p class="muted">The first four categories comprise 23 skills shown with Credly evidence. Additional tools are drawn from the CV and projects.</p><div class="two">'+blocks+'</div></div></section>'
if 'id="skills"' not in s:
    swap('<section class="section" id="certifications">',section+'<section class="section" id="certifications">')
swap('Cisco CyberOps Associate; Cisco Ethical Hacker</h3><p>2025','Cisco CyberOps Associate; Cisco Ethical Hacker</h3><p>2026')
swap('CCNA Introduction to Networks; Cisco IT Essentials</h3><p>2024','CCNA Introduction to Networks (2025); Cisco IT Essentials (2024)</h3><p>2024–2025')
swap('<div class="timeline-entry"><h3>NDG Linux Essentials','<div class="timeline-entry"><h3>CCNA 2 — Enterprise Networking, Security, and Automation; CCNA 3 — Switching, Routing, and Wireless Essentials</h3><p>2026 · course titles as recorded in CV</p></div><div class="timeline-entry"><h3>NDG Linux Essentials')
swap('<h3>CyberOps Associate</h3><p>Cisco Networking Academy</p><span class="badge-year">2025','<h3>CyberOps Associate</h3><p>Cisco Networking Academy</p><span class="badge-year">2026')
swap('<h3>Ethical Hacker</h3><p>Cisco Networking Academy</p><span class="badge-year">2025','<h3>Ethical Hacker</h3><p>Cisco Networking Academy</p><span class="badge-year">2026')
swap('<h3>CCNA: Introduction to Networks</h3><p>Cisco Networking Academy</p><span class="badge-year">2024','<h3>CCNA: Introduction to Networks</h3><p>Cisco Networking Academy</p><span class="badge-year">2025')
if 'Additional Cisco training (2026)' not in s:
    swap('</div><p class="badge-note"><strong>Badge image note:</strong>','</div><div class="box" style="margin-top:22px"><h3>Additional Cisco training (2026)</h3><p>CCNA 2 — Enterprise Networking, Security, and Automation<br>CCNA 3 — Switching, Routing, and Wireless Essentials</p><p class="muted">Course names are reproduced as supplied in the CV; confirm exact course titles with the issuer.</p></div><p class="badge-note"><strong>Badge image note:</strong>')
index.write_text(s,encoding='utf-8')
print('Updated index.html. Existing project catalog, styling and links preserved.')
