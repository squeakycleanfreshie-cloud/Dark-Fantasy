# text shader
define config.default_textshader = "typewriter"
default preferences.text_cps = 40

# positions
transform centerleft:
    xcenter 0.25
    yalign 1.0

transform centerright:
    xcenter 0.75
    yalign 1.0

# speaker focus
transform speaking:
    ease 0.25 zoom 1

transform idle:
    ease 0.25 zoom 0.95
# backgrounds
image bg fountain = im.Scale("bg fountain.jpg", config.screen_width, config.screen_height)
image bg castle = im.Scale("bg castle.jpg", config.screen_width, config.screen_height)

# speaker focus logic
init -1 python:
    import store

    cast = {"vance": "centerleft", "runa": "centerright"}

    def focus(tag):
        for t, pos in cast.items():
            tf = store.speaking if t == tag else store.idle
            renpy.show(t, at_list=[getattr(store, pos), tf])

    def vance_cb(event, interact=True, **kwargs):
        if event == "begin":
            focus("vance")

    def runa_cb(event, interact=True, **kwargs):
        if event == "begin":
            focus("runa")

# characters
define v = Character("Vance", image="vance", callback=vance_cb)
define r = Character("Runa", image="runa", callback=runa_cb)
define l = Character("Lucian")
define a = Character("Queen Astrid", image="astrid")

# custom cursor
init python:
    cursor_scale = 0.25
    cursor_w, cursor_h = renpy.image_size("images/cursor.png")

    config.mouse = None
    config.mouse_displayable = MouseDisplayable(
        im.FactorScale("images/cursor.png", cursor_scale),
        int(cursor_w * cursor_scale) - 2,
        2
    )

# The game starts here.
label start:
    scene bg fountain
    show vance at centerleft, idle
    show runa at centerright, idle

    v "{i}You and Runa, the castle's seer, sit by the fountain.{/i}"
    v "{i}The sky is cloudy, and it is morning.{/i}"
    v "{i}Runa has been in a trance for a while now.{/i}"
    v "{i}Runa's eyes are rolled back, her body unconscious.{/i}"
    v "Runa?"
    v "{i}She quickly snaps out of the trance she's in, present with you. Her eyes turn to look towards you.{/i}"
    r "No. It's not looking good, Vance."
    v "What?"
    r "Your fate is very bad."
    r "Your next battle is going to be unsuccessful."
    v "What?"
    r "That is all."
    v "Runa, you have to stop giving me half the story."
    r "That is all I can see into the future."
    r "What I say is all I know."
    v "I know, it's just, how am I supposed to stop this?"
    r "I do not know that, Vance. That is for you to figure out."

    return