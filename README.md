# Notepad++ Markdown Script

## Requirements

* [Python Script for Notepad++](http://npppythonscript.sourceforge.net/)
 
## Installation

Copy `lib/markdown` folder to `%APPDIR%\Notepad++\plugins\PythonScript\lib\` and
`scripts/*` to `%APPDIR%\Notepad++\plugins\PythonScript\scripts\`.

## Usage

Navigate to menu Plugins -> Python Script -> Scripts -> markdown. You can also place
that script on your toolbar or in "Python Script" menu. Refer to Python Script for
Notepad++ documentation for more info how to do that.

## Known problems

Notepad++ recognizes only two major encodings: single-byte (ANSI) and multi-byte (UTF-8 etc).
Because of that, I had to assume some encoding for single-byte chars - I chose cp1250, because
it suites me best. If you use some other encoding, you have to modify `scripts/markdown.py`.

And above all: use UTF-8 ;)

## Suggested companion

[Markdown syntax highlighting for Notepad++](https://github.com/thomsmits/markdown_npp).
Optionally, if you don't use white background, [here](https://github.com/leafnode/markdown_npp)
you have highlighting with Monokai theme

## Included libraries

* [Python-Markdown](https://github.com/waylan/Python-Markdown) (BSD license)

## License

* BSD (see LICENSE.md)
