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
