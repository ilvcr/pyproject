1->一个使用 Python 来解析纯文本生成一个 HTML 页面的小程序。

2->本项目中将创建以下的代码文件，每个文件的作用简介如下：

    1-->>util.py：实现文本块生成器把纯文本分成一个一个的文本块，以便接下来对每一个文本块进行解析
    2-->>handlers.py：为文本块打上合适的 HTML 标记
    3-->>rules.py：设计一定的规则来判断每个文本块交给处理程序将要加什么标记
    4-->>markup.py：对整个文本进行解析的程序
