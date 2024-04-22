import tkinter as tk

# by_script settable parameters & options (no parameters validation)
window_size_converter = 0.8  # min rational value is 0.35
result_box_length = 7
default_unknown_command_line1 = "Unknown command: "
default_unknown_command_line2 = ",type: [h]elp"


def execute(event=None, result_box_counter=0):
    def command_list(command):

        def help_me():
            pass

        def a1():
            return "a1 ok"

        def a2():
            return "a2 ok"

        if command == "a1":
            return a1()
        elif command == 'a2':
            return a2()
        elif command == 'h':
            return help_me()
        else:
            return default_unknown_command_line1 + command + default_unknown_command_line2
        #return command_list_result

    try:
        command = command_box.get("1.0", "end-1c").strip()
        command_box.delete("1.0", tk.END)

        if command:
            result = command_list(command)
            current_content = results_box.get("1.0", tk.END).splitlines()

            if len(current_content) >= result_box_length:
                results_box.delete("1.0", "2.0")
            results_box.insert(tk.END, result + '\n')
            results_box.see(tk.END)

    except Exception as e:
        result = str(e)
        results_box.insert(tk.END, result + '\n')
        results_box.see(tk.END)


window = tk.Tk()
window.title("UL Database")
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_width = int(screen_width * window_size_converter)
window_height = int(screen_height * window_size_converter)
center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)
window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

command_box = tk.Text(window, width=50, height=10)
command_box.pack()
command_box.bind('<Return>', execute)

results_box = tk.Text(window, width=50, height=10)
results_box.pack()

window.mainloop()
