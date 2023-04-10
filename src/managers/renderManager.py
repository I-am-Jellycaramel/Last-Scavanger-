import pygame
from pygame.locals import *

import enums.gamePhase as gamePhase
import classes.lastscavenger as ls

def render_screen(phase: gamePhase.GamePhase, ls: ls.LastScavenger):
    match phase:
        case phase.PHASE_1:
            render_background(ls)

            #게임 제목 출력
            game_title = ls.font.render("Last Scavanger", 1, ls.colorWhite)
            ls.displaySurf.blit(game_title, (40, 300))
        case _:
            pass

def render_background(ls: ls.LastScavenger):
    background = pygame.image.load("last-scavanger-game-main-screen.png")
    ls.displaySurf.blit(background, (0, 0))
