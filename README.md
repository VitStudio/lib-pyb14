# SNGTOLIB
### _Lib số nguyên tố và các hàm liên quan đến số nguyên tố trong Python 3_
<div align="center">



[![Website](https://img.shields.io/badge/%20%F0%9F%8F%A1%20website-0072ff.svg?longCache=true&style=for-the-badge)](https://daivs.gitbook.io/e-docs)
[![License](https://img.shields.io/github/license/vitstudio/lib-pyb14?style=for-the-badge)](https://github.com/VitStudio/lib-pyb14/edit/main/LICENSE)
[![FORK](https://img.shields.io/github/last-commit/VitStudio/lib-pyb14?style=for-the-badge)](https://github.com/VitStudio/lib-pyb14/commit/main)

</div>

## 🛠 Development

Clone the repository

```zsh
git clone https://github.com/VitStudio/lib-pyb14.git
```

Build the library

```zsh
python setup.py bdist_wheel

# replace '0.1.2' with version
```

Install the library locally

```zsh
pip install dist/sngtolib-0.1.2-py3-none-any.whl
```
Once you have installed your Python library, you can import it using:
```zsh
import sngtolib
 #or
from sngtolib import sngto
```
Build for production

```zsh
python setup.py sdist bdist_wheel --universal --release --sign --identity="Your Name" 
# replace "Your Name" with your name
```
