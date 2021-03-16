import arcade

def draw_section_outlines():
    # Draw squares on bottom
    arcade.draw_rectangle_outline(150, 150, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(450, 150, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(750, 150, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(1050, 150, 300, 300, arcade.color.BLACK)

    # Draw squares on top
    arcade.draw_rectangle_outline(150, 450, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(450, 450, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(750, 450, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(1050, 450, 300, 300, arcade.color.BLACK)


def draw_section_1():
    for row in range(30):
        x = row * 10 + 5
        for column in range(30):
                  # Instead of zero, calculate the proper x location using 'column'
            y = column * 10 + 5  # Instead of zero, calculate the proper y location using 'row'
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)


def draw_section_2():
    # Below, replace "pass" with your code for the loop.
    # Use the modulus operator and an if statement to select the color
    # Don't loop from 30 to 60 to shift everything over, just add 300 to x.
    """
    for row in range(15):
        x = row * 20 + 305
        for column in range(30):
            # Instead of zero, calculate the proper x location using 'column'
            y = column * 10 + 5  # Instead of zero, calculate the proper y location using 'row'
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)
    """
    """
    for row in range(15):
        x = row * 20 + 315
        for column in range(30):
            # Instead of zero, calculate the proper x location using 'column'
            y = column * 10 + 5  # Instead of zero, calculate the proper y location using 'row'
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.BLACK)
    """
    for row in range(30):
        x = row * 10 + 305
        for column in range(30):
            # Instead of zero, calculate the proper x location using 'column'
            y = column * 10 + 5  # Instead of zero, calculate the proper y location using 'row'
            if row % 2 == 0:
                arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)
            else:
                arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.BLACK)


def draw_section_3():
    # Use the modulus operator and an if/else statement to select the color.
    # Don't use multiple 'if' statements.
    """
    for row in range(15):
        y = row * 20 + 5
        for column in range(30):
            # Instead of zero, calculate the proper x location using 'column'
            x = column * 10 + 605  # Instead of zero, calculate the proper y location using 'row'
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)

    for row in range(15):
        y = row * 20 + 15
        for column in range(30):
            # Instead of zero, calculate the proper x location using 'column'
            x = column * 10 + 605  # Instead of zero, calculate the proper y location using 'row'
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.BLACK)
    """
    for row in range(30):
        y = row * 10 + 5
        for column in range(30):
            # Instead of zero, calculate the proper x location using 'column'
            x = column * 10 + 605  # Instead of zero, calculate the proper y location using 'row'
            if row % 2 == 0:
                arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)
            else:
                arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.BLACK)


def draw_section_4():
    # Use the modulus operator and just one 'if' statement to select the color.
    """
    for row in range(15):
        x = row * 20 + 915
        for column in range(30):
            # Instead of zero, calculate the proper x location using 'column'
            y = column * 10 + 5  # Instead of zero, calculate the proper y location using 'row'
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.BLACK)

    for row in range(15):
        y = row * 20 + 15
        for column in range(30):
            # Instead of zero, calculate the proper x location using 'column'
            x = column * 10 + 905  # Instead of zero, calculate the proper y location using 'row'
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.BLACK)

    for row in range(15):
        x = row * 20 + 905
        for column in range(15):
            # Instead of zero, calculate the proper x location using 'column'
            y = column * 20 + 5  # Instead of zero, calculate the proper y location using 'row'
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE

    """
    for row in range(30):
        x = row * 10 + 905
        for column in range(30):
            # Instead of zero, calculate the proper x location using 'column'
            y = column * 10 + 5  # Instead of zero, calculate the proper y location using 'row'
            if row % 2 == 0 and column % 2 == 0:
                arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)
            else:
                arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.BLACK)







def draw_section_5():
    # Do NOT use 'if' statements to complete 5-8. Manipulate the loops instead.
    z = -1
    a = -1
    for i in range(30):

        z += 1
        a += 1
        print(z)
        #for row in range(z):
       #     x = row * 10 + 15

        for column in range(a):
            # Instead of zero, calculate the proper x location using 'column'
            x = z * 10 + 5
            y = column * 10 + 305  # Instead of zero, calculate the proper y location using 'row'
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)

    pass


def draw_section_6():
    z = 31
    a = 0
    for i in range(30):

        z -= 1
        a += 1
        print(z)
       # for row in range(z):
        #    x = row * 10 + 305

        for column in range(a):
            # Instead of zero, calculate the proper x location using 'column'
            x = z * 10 + 295
            y = column * 10 + 305  # Instead of zero, calculate the proper y location using 'row'
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)


    pass


def draw_section_7():
    z = 0
    a = 0
    for i in range(31):

        z += 1
        a += 1
        print(z)
        #for row in range(z):
        #    x = row * -10 + 905

        for column in range(a):
            # Instead of zero, calculate the proper x location using 'column'
            y = column * -10 + 605  # Instead of zero, calculate the proper y location using 'row'
            x = z * -10 + 915
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)


    pass


def draw_section_8():
    z = 0
    a = 0
    for i in range(30):

        z += 1
        a += 1
        print(z)
        for row in range(z):
            x = z * 10 + 895

            for column in range(a):
                # Instead of zero, calculate the proper x location using 'column'
                y = column * -10 + 605  # Instead of zero, calculate the proper y location using 'row'
                arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)

    pass


def main():
    # Create a window
    arcade.open_window(1200, 600, "Lab 05 - Loopy Lab")
    arcade.set_background_color(arcade.color.AIR_FORCE_BLUE)

    arcade.start_render()

    # Draw the outlines for the sections
    draw_section_outlines()

    # Draw the sections
    draw_section_1()
    draw_section_2()
    draw_section_3()
    draw_section_4()
    draw_section_5()
    draw_section_6()
    draw_section_7()
    draw_section_8()

    arcade.finish_render()

    arcade.run()


main()