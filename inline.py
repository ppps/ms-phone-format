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
    f'<script>{js_file.read_text()}</script>'
    ).replace(
    css_target,
    f'<style>{reset_css_file.read_text()}</style>'
    )

output_file.write_text(html)
