# use config() to create a Tkinter toggle button
try:
    # Python2
    import Tkinter as tk
except ImportError:
    # Python3
    import tkinter as tk
def toggle():
    '''
    use
    t_btn.config('text')[-1]
    to get the present state of the toggle button
    '''
    if t_btn.config('text')[-1] == 'True':
        t_btn.config(text='False')
    else:
        t_btn.config(text='True')
root = tk.Tk()
t_btn = tk.Button(text="True", width=12, command=toggle)
t_btn.pack(pady=5)
root.mainloop()