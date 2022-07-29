import os

ui_list = os.listdir('engine/ui')

for ui in ui_list:
    new_name = ui.replace("ui", "py")
    os.system(f"pyuic5 engine/ui/{ui} -o engine/widget/ui/{new_name}")
