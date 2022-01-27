pole = [['ладья_ч.png', 'конь_ч.png', 'слон_ч.png', 'королева_ч.png', 'король_ч.png', 'слон_ч.png', 'конь_ч.png',
         'ладья_ч.png'],
        ['пешка_ч.png', 'пешка_ч.png', 'пешка_ч.png', 'пешка_ч.png', 'пешка_ч.png', 'пешка_ч.png', 'пешка_ч.png',
         'пешка_ч.png'],
        ['-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-'],
        ['пешка.png', 'пешка.png', 'пешка.png', 'пешка.png', 'пешка.png', 'пешка.png', 'пешка.png', 'пешка.png'],
        ['ладья.png', 'конь.png', 'слон.png', 'королева.png', 'король.png', 'слон.png', 'конь.png', 'ладья.png']]

positive = [(50, 187, 800, 105), (50, 787, 800, 105), (350, 387, 200, 100), (350, 587, 200, 100)]

tmbgbl, tmbgw, tmsbl, tmsw = 30, 30, 5, 5

'''
            pygame.image.save(screen, "data\\screenshot.png")
            im = Image.open("data\\screenshot.png")
            im2 = im.filter(ImageFilter.GaussianBlur(radius=3))
            im2.save('data\\screenshot.png')
            im3 = load_image('screenshot.png')
            screen.blit(im3, (0, 0))
'''