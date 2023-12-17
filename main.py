from managers import GameManager

def main():    
    game_manager = GameManager(
        width=1920,
        height=1080,
        caption="JUMP",
        fullscreen=True
        )

    game_manager.run()

if __name__ == "__main__":
    main()