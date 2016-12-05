#!/usr/local/bin/python3

from pathlib import Path

SCRIPT = Path(__file__)

interface_file = SCRIPT.with_name('interface.html')
js_file = SCRIPT.with_name('phone_format.js')
reset_css_file = SCRIPT.with_name('reset.css')
output_file = SCRIPT.with_name('inlined.html')

html = interface_file.read_text()

js_target = '<script src="phone_format.js"></script>'
css_target = '<link rel="stylesheet" src="reset.css">'

html = html.replace(
    js_target,
    '<script>{}</script>'.format(js_file.read_text())
    ).replace(
    css_target,
    '<style>{}</style>'.format(reset_css_file.read_text())
    )

output_file.write_text(html)
