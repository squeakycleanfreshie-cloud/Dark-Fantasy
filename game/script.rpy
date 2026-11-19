# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

image bg fountain = im.Scale("bg fountain.jpg", config.screen_width, config.screen_height)

define v = Character("Vance", image="vance")
define l = Character("Lucian", image="")
define a = Character("Queen Astrid", image="astrid")
define r = Character("Runa", image="runa")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg fountain

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show vance

    # These display lines of dialogue.

    v "You've created a new Ren'Py game."

    v "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
