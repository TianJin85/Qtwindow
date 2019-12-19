### 将.ui文件转为.py文件
##### 方法一：
    ```bash
    python -m PyQt5.uic.pyuic demo.ui -o demo.py
    ```

#### 方法二：
    ```bash
    pyuic5 demo.u -o demo.py
    ```
    

#### 尺寸策略（zisePolicy）
    sizeHint(期望尺寸)
    对于大多数控件来说，sizeHint的是只读的
    读取期望尺寸
    self.pushButton.sizeHint().width()
    self.pushButton.sizeHint().height()

QTushButton width:77 height 32
QTextEdit width:256 height:192

最小期望尺寸
self.pushButton.minimumSizeHint().width()
self.pushButton.minimumSizeHint().heigth()
QTextEdit 78

#### 窗口类型
    有3种窗口
    ```bash
    QMainWindow
    QWidget
    QDialog
    ```
    QMainWindow:可以包含菜单栏，工具栏状态栏和标题栏，是最常见的窗口形式
    QDialog:是对话窗口的基类。没有菜单栏，工具栏，标题栏。
    QWidget:不确定窗口的用途，就使用QWidget
    
