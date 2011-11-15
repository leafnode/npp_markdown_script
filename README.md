# Notepad++ Markdown Script

## Requirements

* Python Script for Notepad++ [1]
 
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

Markdown syntax highlighting for Notepad++ [2]. Optionally, if you don't use white background, here
you have highlighting with Monokai theme: [3]

## Included libraries

* Python-Markdown [4] (BSD license)

## License

* BSD (see LICENSE.md)

[1]: http://npppythonscript.sourceforge.net/
[2]: https://github.com/thomsmits/markdown_npp
[3]: https://github.com/leafnode/markdown_npp
[4]: https://github.com/waylan/Python-Markdown
