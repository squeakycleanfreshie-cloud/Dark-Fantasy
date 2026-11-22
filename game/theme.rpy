init offset = 10

define gui.dialogue_ypos = 60

define gui.accent_color = "#587a48"
define gui.muted_color = "#3b5230"
define gui.hover_muted_color = "#6f9a5a"
define gui.idle_color = "#8d9693"
define gui.hover_color = "#a8c796"
define gui.selected_color = "#a8c796"
define gui.insensitive_color = "#3b4538"
define gui.text_color = "#d8ddd9"
define gui.interface_text_color = "#d8ddd9"

define gui.text_font = "fonts/font2.ttf"
define gui.interface_text_font = "fonts/font2.ttf"
define gui.name_text_font = "fonts/font.otf"

define gui.quick_button_text_font = "fonts/font2.ttf"
define gui.quick_button_text_size = 22
define gui.quick_button_text_idle_color = "#8d9693"
define gui.quick_button_text_hover_color = "#a8c796"

define gui.main_menu_background = Transform("bg castle.jpg", xysize=(config.screen_width, config.screen_height), fit="fill")
define gui.game_menu_background = Solid("#0e120d")

## Dialogue
style window:
    background Solid("#0e120dd9")

style namebox:
    background Solid("#3b5230")
    padding (24, 6)

style say_label:
    font "fonts/font.otf"
    color "#a8c796"
    bold False
    size 100

style say_dialogue:
    font "fonts/font2.ttf"
    color "#d8ddd9"
    ypos 120

style quick_button_text:
    font "fonts/font2.ttf"
    idle_color "#8d9693"
    hover_color "#a8c796"
    size 22

## Main menu
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
    font "fonts/font2.ttf"
    color "#8d9693"

## Game menu frame
style game_menu_outer_frame:
    background Fixed(Solid("#0e120d"), Solid("#587a48", xsize=4, xpos=418))

style game_menu_label_text:
    font "fonts/font.otf"
    color "#a8c796"
    size 70

## Generic buttons
style button_text:
    font "fonts/font2.ttf"
    idle_color "#8d9693"
    hover_color "#a8c796"
    selected_color "#a8c796"
    insensitive_color "#3b4538"

## Save / Load
style slot_button:
    idle_background Solid("#161d14")
    hover_background Solid("#25331f")
    selected_idle_background Solid("#1d2a19")
    selected_hover_background Solid("#2f4228")

style slot_button_text:
    font "fonts/font2.ttf"
    idle_color "#8d9693"
    hover_color "#a8c796"
    selected_idle_color "#a8c796"

style slot_time_text:
    font "fonts/font2.ttf"
    color "#8d9693"

style slot_name_text:
    font "fonts/font2.ttf"
    color "#8d9693"

style page_label_text:
    font "fonts/font2.ttf"
    color "#a8c796"

style page_button_text:
    font "fonts/font2.ttf"
    idle_color "#8d9693"
    hover_color "#a8c796"
    selected_idle_color "#a8c796"
    selected_hover_color "#a8c796"

## Preferences
style pref_label_text:
    font "fonts/font.otf"
    color "#a8c796"

style check_button:
    foreground None

style radio_button:
    foreground None

style check_button_text:
    font "fonts/font2.ttf"
    idle_color "#8d9693"
    hover_color "#a8c796"
    selected_idle_color "#a8c796"
    selected_hover_color "#a8c796"

style radio_button_text:
    font "fonts/font2.ttf"
    idle_color "#8d9693"
    hover_color "#a8c796"
    selected_idle_color "#a8c796"
    selected_hover_color "#a8c796"

style slider:
    ysize 28
    left_bar Solid("#587a48")
    right_bar Solid("#25331f")
    thumb Solid("#a8c796", xsize=16, ysize=28)
    thumb_offset 8

style vscrollbar:
    xsize 16
    top_bar Solid("#161d14")
    bottom_bar Solid("#161d14")
    thumb Solid("#587a48", xsize=16, ysize=60)

style scrollbar:
    ysize 16
    left_bar Solid("#161d14")
    right_bar Solid("#161d14")
    thumb Solid("#587a48", xsize=60, ysize=16)

## History
style history_name_text:
    font "fonts/font.otf"
    color "#a8c796"

style history_text:
    font "fonts/font2.ttf"
    color "#d8ddd9"

## Popups / indicators
style confirm_frame:
    background Solid("#0e120d")

style confirm_prompt_text:
    font "fonts/font2.ttf"
    color "#d8ddd9"

style notify_frame:
    background Solid("#0e120dd9")

style notify_text:
    font "fonts/font2.ttf"
    color "#a8c796"

style skip_frame:
    background Solid("#0e120dd9")

style skip_text:
    font "fonts/font2.ttf"
    color "#a8c796"

## Choice menus
style choice_button:
    idle_background Solid("#0e120dd9")
    hover_background Solid("#3b5230")

style choice_button_text:
    font "fonts/font2.ttf"
    idle_color "#d8ddd9"
    hover_color "#ffffff"