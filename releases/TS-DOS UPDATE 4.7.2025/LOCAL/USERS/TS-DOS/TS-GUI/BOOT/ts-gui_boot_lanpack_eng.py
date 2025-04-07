import pygame  # type: ignore # The Reason Why pygame Is Inported Is That Because This Is A GUI
import sys
import os
import webbrowser

# Initialize Pygame
pygame.init()


# Function to open "About TS-DOS/TS-GUI" window
def show_version_info():
    # Create a new "About" surface
    about_width, about_height = 400, 200
    about_screen = pygame.Surface((about_width, about_height))
    about_screen.fill((255, 255, 255))  # Set white background

    # Add text
    font = pygame.font.Font(None, 36)
    title = font.render("About TS-DOS/TS-GUI", True, (0, 0, 0))  # Black text
    version = font.render("TS-DOS: 1.0.2 \n| TS-GUI: TEST", True, (0, 0, 0))

    # Draw text onto the About screen
    about_screen.blit(title, (50, 50))
    about_screen.blit(version, (50, 100))
    font = pygame.font.Font(None, 36)
    test_text_version = font.render("1.0.0", True, (0, 0, 0))  # Render the text properly
    text_lanpack = font.render("LANPACK ENG", True, (0, 0, 0))
    about_screen.blit(test_text_version, (50, 150))  # Correct placement
    about_screen.blit(text_lanpack, (50, 200))

    # Display the About screen over the main GUI
    running_about = True
    while running_about:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN):
                running_about = False  # Exit when the user presses ENTER or closes the window
        pygame.display.set_caption("About TS-DOS/TS-GUI")  # Change the window caption

        # Render the "About" window as an overlay
        screen = pygame.display.get_surface()  # Get the existing main screen
        screen.blit(about_screen, (200, 150))  # Center the "About" window on the screen
        pygame.display.flip()  # Update the display
        if not running_about:
            pygame.display.set_caption("TS-GUI TEST 1.0.0 LANPACK ENG")  # Reset the window caption

# Screen setup
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("TS-GUI TEST 1.0.0 LANPACK ENG")

# Define colors
white = (255, 255, 255)
blue = (0, 122, 204)
dark_blue = (0, 102, 180)
black = (0, 0, 0)

# Button dimensions
button_width, button_height = 120, 50
start_button_x = screen_width - button_width - 20  # Bottom-right position
start_button_y = screen_height - button_height - 20

# Font setup
font = pygame.font.Font(None, 36)

# "Start" button text
start_button_text = font.render("Start", True, white)

# App buttons properties
app_button_width, app_button_height = 180, 50
app_buttons = [
    {"label": "Internet", "x": 20, "y": 20},
    {"label": "Email", "x": 20, "y": 90},
    {"label": "TS-GUI/TS-DOS Version", "x": 20, "y": 160},
    {"label": "End TS-GUI/Start TS-DOS", "x": 20, "y": 230}
]

# Helper to draw app buttons
def draw_button(label, x, y, is_hovered):
    color = dark_blue if is_hovered else blue
    pygame.draw.rect(screen, color, (x, y, app_button_width, app_button_height))
    text = font.render(label, True, white)
    screen.blit(text, (x + (app_button_width - text.get_width()) // 2, y + (app_button_height - text.get_height()) // 2))

# Main loop
running = True
while running:
    screen.fill(white)  # Clear the screen
    mouse_x, mouse_y = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Close window
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:  # Handle clicks
            # Check for clicks on the Start button
            if start_button_x <= mouse_x <= start_button_x + button_width and start_button_y <= mouse_y <= start_button_y + button_height:
                print("Start Button Clicked!")
                print("Internet"
                "\nEmail"
                "\nTS-GUI/TS-DOS Version"
                "\nEnd TS-GUI/Start TS-DOS"
                "\nClick The X Buttion In The Top Right Corner To Exit and Stop TS-GUI")
                print("START MENU")
            
            # Check for clicks on app buttons
            for button in app_buttons:
                if button["x"] <= mouse_x <= button["x"] + app_button_width and button["y"] <= mouse_y <= button["y"] + app_button_height:
                    print(f"{button['label']} Button Clicked!")
                    if button["label"] == "End TS-GUI/Start TS-DOS":
                        print("Exiting TS-GUI... Starting TS-DOS!")
                        os.chdir('C:\\Users\\tadeo\\OneDrive\\Desktop\\LOCAL\\USERS\\TS-DOS\\ADMIN_USER\\BOOT')
                        os.system('ts-dos')  # Replace with the actual command to start TS-DOS
                        sys.exit()
                        running = False
                        
                    if button["label"] == "Internet":
                        print("Opening Internet...")
                        webbrowser.open("https://www.google.com")

                    if button["label"] == "Email":
                        print("Opening Email...")
                        os.system('start outlook')

                    if button["label"] == "TS-GUI/TS-DOS Version":
                        print("Opening TS-GUI/TS-DOS Version...")
                        show_version_info()

    # Draw the Start button
    if start_button_x <= mouse_x <= start_button_x + button_width and start_button_y <= mouse_y <= start_button_y + button_height:
        pygame.draw.rect(screen, dark_blue, (start_button_x, start_button_y, button_width, button_height))  # Hover effect
    else:
        pygame.draw.rect(screen, blue, (start_button_x, start_button_y, button_width, button_height))
    screen.blit(start_button_text, (start_button_x + (button_width - start_button_text.get_width()) // 2,
                                    start_button_y + (button_height - start_button_text.get_height()) // 2))

    # Draw app buttons
    for button in app_buttons:
        is_hovered = button["x"] <= mouse_x <= button["x"] + app_button_width and button["y"] <= mouse_y <= button["y"] + app_button_height
        draw_button(button["label"], button["x"], button["y"], is_hovered)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
