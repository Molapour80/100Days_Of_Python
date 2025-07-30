import os
import msvcrt
import time

# Game settings
width = 60
height = 20
paddle_size = 3
ball_pos = [width // 2, height // 2]
ball_dir = [1, 1]
paddle1_pos = height // 2
paddle2_pos = height // 2
score1 = 0
score2 = 0

def clear_screen():
    os.system('cls')

def draw():
    clear_screen()
    print(f"Player 1: {score1}  Player 2: {score2}")
    print('-' * (width + 2))
    
    for y in range(height):
        line = [' '] * width
        # Draw paddles
        if y in range(paddle1_pos - paddle_size // 2, paddle1_pos + paddle_size // 2 + 1):
            line[0] = '|'
        if y in range(paddle2_pos - paddle_size // 2, paddle2_pos + paddle_size // 2 + 1):
            line[-1] = '|'
        # Draw ball
        if y == ball_pos[1] and 0 <= ball_pos[0] < width:
            line[ball_pos[0]] = 'O'
        
        print('|' + ''.join(line) + '|')
    
    print('-' * (width + 2))

def get_key():
    if not msvcrt.kbhit():
        return None
    
    try:
        key = msvcrt.getch()
        # Handle special keys (arrows)
        if key == b'\xe0':
            arrow = msvcrt.getch()
            if arrow == b'H':  # Up arrow
                return 'up'
            elif arrow == b'P':  # Down arrow
                return 'down'
        # Handle normal keys
        return key.decode('ascii').lower()
    except:
        return None

def update():
    global ball_pos, ball_dir, score1, score2
    
    # Move ball
    ball_pos[0] += ball_dir[0]
    ball_pos[1] += ball_dir[1]
    
    # Ball collision with top/bottom
    if ball_pos[1] <= 0 or ball_pos[1] >= height - 1:
        ball_dir[1] *= -1
    
    # Ball collision with paddles
    if ball_pos[0] == 1 and paddle1_pos - paddle_size // 2 <= ball_pos[1] <= paddle1_pos + paddle_size // 2:
        ball_dir[0] *= -1
    elif ball_pos[0] == width - 2 and paddle2_pos - paddle_size // 2 <= ball_pos[1] <= paddle2_pos + paddle_size // 2:
        ball_dir[0] *= -1
    
    # Scoring
    if ball_pos[0] <= 0:
        score2 += 1
        ball_pos = [width // 2, height // 2]
        ball_dir = [1, 1]
    elif ball_pos[0] >= width - 1:
        score1 += 1
        ball_pos = [width // 2, height // 2]
        ball_dir = [-1, 1]

def main():
    global paddle1_pos, paddle2_pos
    
    print("Text Pong - Player 1 (W/S) vs Player 2 (Up/Down)")
    print("Press any key to start...")
    while not msvcrt.kbhit():
        pass
    msvcrt.getch()  # Clear the initial key press
    
    while True:
        draw()
        
        key = get_key()
        
        # Process input
        if key == 'w' and paddle1_pos > paddle_size // 2:
            paddle1_pos -= 1
        elif key == 's' and paddle1_pos < height - 1 - paddle_size // 2:
            paddle1_pos += 1
        elif key == 'up' and paddle2_pos > paddle_size // 2:
            paddle2_pos -= 1
        elif key == 'down' and paddle2_pos < height - 1 - paddle_size // 2:
            paddle2_pos += 1
        elif key == 'E':
            break
        
        update()
        time.sleep(0.05)

if __name__ == "__main__":
    main()