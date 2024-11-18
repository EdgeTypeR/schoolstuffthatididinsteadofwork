import curses
import math
import time

def draw_donut(win):
    # Setup
    curses.curs_set(0)  # Hide the cursor
    win.nodelay(1)      # Make getch non-blocking
    win.timeout(100)    # Refresh every 100 milliseconds

    # Constants for the donut
    a = 1
    b = 1
    theta_spacing = 0.07
    phi_spacing = 0.02

    while True:
        # Clear the window
        win.clear()
        
        # Draw the donut
        for theta in range(0, int(2 * math.pi / theta_spacing)):
            for phi in range(0, int(2 * math.pi / phi_spacing)):
                # Calculate the coordinates
                theta = theta * theta_spacing
                phi = phi * phi_spacing
                
                # 3D coordinates
                x = math.sin(theta)
                y = math.cos(theta)
                z = math.sin(phi)
                ooz = 1 / (z + 2)  # Perspective division
                xp = int((curses.COLS // 2) + (a * ooz * x * 30))  # Scale x
                yp = int((curses.LINES // 2) - (b * ooz * y * 15))  # Scale y

                # Calculate luminance
                L = (x * y * z) + 2
                if L > 0:
                    # Set character based on luminance
                    char = '@' if L > 2 else ' '
                    if 0 <= xp < curses.COLS and 0 <= yp < curses.LINES:
                        win.addch(yp, xp, char)

        # Refresh the window to display the donut
        win.refresh()

        # Rotate
        a += 0.05
        b += 0.05

        # Check for exit condition (e.g., a key press)
        if win.getch() != -1:
            break

def main():
    curses.wrapper(draw_donut)

if __name__ == "__main__":
    main()
