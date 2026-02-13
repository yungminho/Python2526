import pygame, sys, random, math, time

WIDTH, HEIGHT = 1000, 640
FPS = 144
WIN_SCORE = 11

PADDLE_W, PADDLE_H = 14, 110
BALL_RADIUS = 10
BASE_BALL_SPEED = 360.0
PADDLE_SPEED = 480.0

PERK_SIZE = 42
PERK_DURATION = 4.0

NEON = {
    "bg1": (10, 8, 20),
    "accent": (0, 200, 255),
    "glow": (60, 0, 120),
    "white": (245,245,250)
}

def clamp(v, a, b): return max(a, min(b, v))

class Paddle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.w = PADDLE_W
        self.h = PADDLE_H
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
        self.speed = PADDLE_SPEED
        self.frozen_until = 0.0
        self.enlarge_until = 0.0
        self.inverted_until = 0.0

    def update(self, dy, dt):
        if time.time() < self.frozen_until:
            dy = 0
        if time.time() < self.inverted_until:
            dy = -dy
        self.y += dy * self.speed * dt
        self.h = PADDLE_H * (1.6 if time.time() < self.enlarge_until else 1.0)
        self.y = clamp(self.y, 0, HEIGHT - self.h)
        self.rect.update(int(self.x), int(self.y), int(self.w), int(self.h))

    def center(self):
        return self.y + self.h / 2

    def draw(self, surf):
        glow = pygame.Surface((self.w+20, int(self.h)+20), pygame.SRCALPHA)
        pygame.draw.rect(glow, (NEON["accent"][0], NEON["accent"][1], NEON["accent"][2], 80), glow.get_rect(), border_radius=8)
        for i in range(3):
            surf.blit(glow, (self.x-10, self.y-10), special_flags=pygame.BLEND_ADD)
        pygame.draw.rect(surf, NEON["white"], self.rect, border_radius=3)

class Ball:
    def __init__(self):
        self.reset()

    def reset(self, direction=None):
        self.x = WIDTH / 2
        self.y = HEIGHT / 2
        angle = random.uniform(-0.35, 0.35)
        direction = random.choice([-1, 1]) if direction is None else direction
        self.speed = BASE_BALL_SPEED
        self.vx = math.cos(angle) * self.speed * direction
        self.vy = math.sin(angle) * self.speed
        self.speed_boost_until = 0.0
        self.trail = []
        self.vy += random.uniform(-50, 50)

    def update(self, dt):
        speed_mult = 1.0
        if time.time() < self.speed_boost_until:
            speed_mult = 1.9
        self.x += self.vx * speed_mult * dt
        self.y += self.vy * speed_mult * dt

        self.trail.insert(0, (self.x, self.y, 0.8))
        if len(self.trail) > 24:
            self.trail.pop()

        if self.y - BALL_RADIUS <= 0:
            self.y = BALL_RADIUS
            self.vy = -self.vy
        if self.y + BALL_RADIUS >= HEIGHT:
            self.y = HEIGHT - BALL_RADIUS
            self.vy = -self.vy

    def draw(self, surf):
        for i,(tx,ty,life) in enumerate(self.trail):
            alpha = int(140 * (1 - i/len(self.trail)))
            r = int(BALL_RADIUS * (1 - i/ (len(self.trail)*1.2)))
            if r <= 0: continue
            s = pygame.Surface((r*2, r*2), pygame.SRCALPHA)
            pygame.draw.circle(s, (NEON["accent"][0],NEON["accent"][1],NEON["accent"][2],alpha), (r,r), r)
            surf.blit(s, (tx-r, ty-r), special_flags=pygame.BLEND_ADD)
        pygame.draw.circle(surf, NEON["white"], (int(self.x), int(self.y)), BALL_RADIUS)

class Perk:
    COLORS = {
        'enlarge': (255,180,60),
        'freeze': (60,160,255),
        'speed': (255,70,70),
        'invert': (190,60,255)
    }
    ICONS = {
        'enlarge': 'E',
        'freeze': 'F',
        'speed': 'S',
        'invert': 'I'
    }
    def __init__(self):
        self.active = False
        self.type = None
        self.rect = pygame.Rect(0,0,PERK_SIZE,PERK_SIZE)
        self.spawn_time = 0.0

    def spawn(self):
        self.type = random.choice(list(self.COLORS.keys()))
        self.rect.x = random.randint(160, WIDTH-160)
        self.rect.y = random.randint(80, HEIGHT-80)
        self.spawn_time = time.time()
        self.active = True

    def draw(self, surf, font):
        if not self.active: return
        t = (time.time() - self.spawn_time)
        pulse = 1 + 0.08*math.sin(t*6)
        s = pygame.Surface((int(self.rect.w*pulse), int(self.rect.h*pulse)), pygame.SRCALPHA)
        color = self.COLORS[self.type]
        pygame.draw.rect(s, (color[0],color[1],color[2],160), s.get_rect(), border_radius=8)
        surf.blit(s, (self.rect.centerx - s.get_width()/2, self.rect.centery - s.get_height()/2), special_flags=pygame.BLEND_ADD)
        pygame.draw.rect(surf, color, self.rect, border_radius=6)
        txt = font.render(self.ICONS[self.type], True, (20,20,20))
        surf.blit(txt, txt.get_rect(center=self.rect.center))

    def expired(self):
        return (time.time() - self.spawn_time) > 6.2

def draw_neon_bg(surf, t):
    surf.fill(NEON["bg1"])
    band = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    for i in range(0, HEIGHT, 8):
        a = int(10 * (1 + math.sin((i/40.0) + t*1.2)))
        pygame.draw.rect(band, (20,10,40,a), (0,i,WIDTH,4))
    surf.blit(band, (0,0), special_flags=pygame.BLEND_ADD)
    for y in range(10, HEIGHT, 36):
        pygame.draw.rect(surf, (60,60,80), (WIDTH//2-2, y, 4, 20))

def draw_text_center(surf, text, size, y, fontname, color=NEON["white"], bold=False):
    font = pygame.font.SysFont(fontname, size, bold=bold)
    r = font.render(text, True, color)
    surf.blit(r, r.get_rect(center=(WIDTH//2, y)))

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("PYPONG")
    clock = pygame.time.Clock()

    font_large = pygame.font.SysFont('Arial', 56, bold=True)
    font_med = pygame.font.SysFont('Arial', 28, bold=False)
    font_small = pygame.font.SysFont('Arial', 18)

    left = Paddle(48, HEIGHT//2 - PADDLE_H//2)
    right = Paddle(WIDTH - 48 - PADDLE_W, HEIGHT//2 - PADDLE_H//2)
    ball = Ball()
    perk = Perk()
    next_perk = time.time() + random.uniform(3,7)

    score_l = 0
    score_r = 0
    winner = None
    running = True
    show_menu = True
    paused = False
    vs_ai = True
    ai_level = 1
    last_time = time.time()

    def reset_round(serving=None):
        nonlocal ball, left, right
        ball.reset(serving)
        left.y = HEIGHT//2 - left.h/2
        right.y = HEIGHT//2 - right.h/2
        left.rect.y = int(left.y)
        right.rect.y = int(right.y)
        left.frozen_until = 0
        right.frozen_until = 0
        left.enlarge_until = 0
        right.enlarge_until = 0
        left.inverted_until = 0
        right.inverted_until = 0
        ball.trail = []

    def ai_move(paddle, level, dt):
        if time.time() < paddle.frozen_until:
            return
        if abs(ball.vx) < 1e-3:
            target = HEIGHT / 2
        else:
            t = (paddle.x - ball.x) / ball.vx
            if t < 0:
                t = 0.5
            proj_y = ball.y + ball.vy * t
            period = HEIGHT - 2 * BALL_RADIUS
            if period > 0:
                prod = (proj_y - BALL_RADIUS) % (2 * period)
                proj_y = BALL_RADIUS + abs(prod)
                if proj_y > HEIGHT - BALL_RADIUS:
                    proj_y = 2 * (HEIGHT - BALL_RADIUS) - proj_y
            difficulty = {1: 0.28, 2: 0.15, 3: 0.06}[level]
            error = random.uniform(-HEIGHT * difficulty, HEIGHT * difficulty)
            target = proj_y + error

        dy = 0
        if paddle.center() < target - 6:
            dy = 1
        elif paddle.center() > target + 6:
            dy = -1

        spd_mult = 1.0 + 0.08 * level
        paddle.speed = PADDLE_SPEED * spd_mult
        paddle.update(dy, dt)

    last_hit = None

    while running:
        now = time.time()
        dt = now - last_time
        last_time = now
        if dt > 0.06: dt = 0.06

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    if show_menu:
                        running = False
                    else:
                        paused = not paused
                if show_menu:
                    if e.key == pygame.K_1:
                        vs_ai = False; show_menu = False; paused = False; score_l=0; score_r=0; winner=None; reset_round()
                    if e.key == pygame.K_2:
                        vs_ai = True; ai_level = 1; show_menu=False; paused=False; score_l=0; score_r=0; winner=None; reset_round()
                    if e.key == pygame.K_3:
                        vs_ai = True; ai_level = 2; show_menu=False; paused=False; score_l=0; score_r=0; winner=None; reset_round()
                    if e.key == pygame.K_4:
                        vs_ai = True; ai_level = 3; show_menu=False; paused=False; score_l=0; score_r=0; winner=None; reset_round()
                else:
                    if e.key == pygame.K_r:
                        score_l = 0; score_r = 0; winner = None; reset_round()
                    if e.key == pygame.K_m:
                        show_menu = True; paused = False

        keys = pygame.key.get_pressed()

        if not show_menu and not paused and winner is None:
            left_dy = 0
            if keys[pygame.K_w]: left_dy -= 1
            if keys[pygame.K_s]: left_dy += 1
            left.update(left_dy, dt)

            if vs_ai:
                ai_move(right, ai_level, dt)
            else:
                right_dy = 0
                if keys[pygame.K_UP]: right_dy -= 1
                if keys[pygame.K_DOWN]: right_dy += 1
                right.update(right_dy, dt)

            ball.update(dt)

            ball_rect = pygame.Rect(int(ball.x - BALL_RADIUS), int(ball.y - BALL_RADIUS), BALL_RADIUS*2, BALL_RADIUS*2)
            if ball.vx < 0 and left.rect.colliderect(ball_rect):
                off = (ball.y - left.center()) / (left.h / 2)
                ball.vx = abs(ball.vx)
                scale = BASE_BALL_SPEED / 5.0
                ball.vy += off * 3 * scale
                ball.x = left.rect.right + BALL_RADIUS
                last_hit = 'left'

            if ball.vx > 0 and right.rect.colliderect(ball_rect):
                off = (ball.y - right.center()) / (right.h / 2)
                ball.vx = -abs(ball.vx)
                scale = BASE_BALL_SPEED / 5.0
                ball.vy += off * 3 * scale
                ball.x = right.rect.left - BALL_RADIUS
                last_hit = 'right'

            if ball.x < -40:
                score_r += 1
                if score_r >= WIN_SCORE:
                    winner = "PRAWY"
                reset_round(1)
            if ball.x > WIDTH + 40:
                score_l += 1
                if score_l >= WIN_SCORE:
                    winner = "LEWY"
                reset_round(-1)

            if not perk.active and time.time() > next_perk:
                perk.spawn()
            if perk.active:
                if perk.expired():
                    perk.active = False
                    next_perk = time.time() + random.uniform(3,7)
                else:
                    if perk.rect.colliderect(ball_rect):
                        t = perk.type

                        if last_hit is None:
                            collector = left if ball.vx < 0 else right
                            opponent = right if ball.vx < 0 else left
                        else:
                            if last_hit == 'left':
                                collector = left
                                opponent = right
                            else:
                                collector = right
                                opponent = left

                        if t == 'enlarge':
                            collector.enlarge_until = time.time() + PERK_DURATION
                        elif t == 'freeze':
                            opponent.frozen_until = time.time() + PERK_DURATION
                        elif t == 'speed':
                            ball.speed_boost_until = time.time() + PERK_DURATION
                            ball.vx *= 1.25
                            ball.vy *= 1.15
                        elif t == 'invert':
                            opponent.inverted_until = time.time() + PERK_DURATION

                        perk.active = False
                        next_perk = time.time() + random.uniform(4, 9)

            if time.time() > ball.speed_boost_until:
                cur_speed = math.hypot(ball.vx, ball.vy)
                if cur_speed > BASE_BALL_SPEED * 0.98:
                    factor = 0.995
                    ball.vx *= factor
                    ball.vy *= factor

        draw_neon_bg(screen, time.time()*0.6)

        left.draw(screen)
        right.draw(screen)
        ball.draw(screen)
        if perk.active:
            perk.draw(screen, font_med)

        score_surf_l = font_large.render(str(score_l), True, NEON["white"])
        score_surf_r = font_large.render(str(score_r), True, NEON["white"])
        screen.blit(score_surf_l, (WIDTH//2 - 180, 24))
        screen.blit(score_surf_r, (WIDTH//2 + 120, 24))

        fps_text = font_small.render(f"FPS: {int(clock.get_fps())}", True, (200,200,200))
        screen.blit(fps_text, (12, 8))

        mode_text = "1vAI" if vs_ai else "1v1"
        ai_text = f"AI Lvl: {ai_level}" if vs_ai else ""
        screen.blit(font_small.render(mode_text + ("  " + ai_text if ai_text else ""), True, (200,200,200)), (12, 30))
        screen.blit(font_small.render("M - Menu | ESC - Pause | R - Reset", True, (200,200,200)), (12, HEIGHT-26))

        if show_menu:
            overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
            overlay.fill((6,6,12,220))
            screen.blit(overlay, (0,0))
            draw_text_center(screen, "PYPONG", 72, HEIGHT//2 - 120, 'Arial', NEON["accent"], True)
            draw_text_center(screen, "1 — 2 Graczy    2 — AI Easy    3 — AI Medium    4 — AI Hard", 28, HEIGHT//2 - 30, 'Arial')
            draw_text_center(screen, "Sterowanie: W/S  oraz Góra/Dół", 22, HEIGHT//2 + 10, 'Arial')
            draw_text_center(screen, "Naciśnij 1/2/3/4 aby rozpocząć", 20, HEIGHT//2 + 60, 'Arial')
        elif paused:
            overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
            overlay.fill((10,10,20,160))
            screen.blit(overlay, (0,0))
            draw_text_center(screen, "PAUZA", 64, HEIGHT//2 - 30, 'Arial', NEON["accent"], True)
            draw_text_center(screen, "ESC - kontynuuj | M - menu | R - restart", 20, HEIGHT//2 + 30, 'Arial')
        if winner:
            overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
            overlay.fill((6,6,12,200))
            screen.blit(overlay, (0,0))
            draw_text_center(screen, f"{winner} WYGRYWA!", 64, HEIGHT//2 - 20, 'Arial', NEON["accent"], True)
            draw_text_center(screen, "Naciśnij R, aby zrestartować | M - Menu", 20, HEIGHT//2 + 40, 'Arial')

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
