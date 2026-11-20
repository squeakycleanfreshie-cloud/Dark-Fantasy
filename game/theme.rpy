init offset = 10

define gui.dialogue_ypos = 60

define gui.accent_color = '#587a48'
define gui.muted_color = '#3b5230'
define gui.hover_muted_color = '#6f9a5a'
define gui.quick_button_text_font = "fonts/font2.ttf"
define gui.quick_button_text_size = 22
define gui.quick_button_text_idle_color = "#8d9693"
define gui.quick_button_text_hover_color = "#a8c796"
define gui.interface_text_font = "fonts/font2.ttf"

define gui.main_menu_background = Transform("bg fountain.jpg", xysize=(config.screen_width, config.screen_height), fit="fill")


style window:
    background Solid("#0e120dd9")

style namebox:
    background Solid("#3b5230")
    padding (24, 6)

style say_label:
    font "fonts/font.otf"
    color "#a8c796"
    bold False
    size 80

style say_dialogue:
    font "fonts/font2.ttf"
    color "#d8ddd9"
    ypos 100

style main_menu_frame:
    background Fixed(Solid("#0e120d"), Solid("#587a48", xsize=4, xalign=1.0))

style navigation_button_text:
    font "fonts/font2.ttf"
    idle_color "#8d9693"
    hover_color "#a8c796"
    selected_color "#a8c796"
    size 40
    outlines [(2, "#0e120d", 0, 0)]

style main_menu_title:
    font "fonts/font.otf"
    color "#e8d4c4"
    size 200
    outlines [(3, "#3b5230", 0, 0)]

style main_menu_version:
    color "#8d9693"

style quick_button_text:
    font "fonts/font2.ttf"
    idle_color "#8d9693"
    hover_color "#a8c796"
    size 22