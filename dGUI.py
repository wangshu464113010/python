# GUI界面基础的基础的基础
# tkinter模块
import tkinter as tk
btn = tk.Button()  # 按钮
btn['text'] = 'Check me'
# 布局管理器(几何体管理器)pack
def clicked():
    print('I was clicked!')

btn['command'] = clicked
btn.pack()
tk.Button(text='Click me too!', command=clicked).pack()
top = tk.Tk()  # 创建一个充当主窗口的顶级组件(控件)
tk.mainloop()  # 调用该函数进入Tkinter主时间循环，而不是直接退出程序



