# 这是一个用python写的小球从窗口中间安地球的重力向下掉落并并碰到窗口下面按篮球的弹力和垂直速度反弹，球可以被鼠标拖动的程序。
# 你需要提供以下参数：
# 窗口宽度
# 窗口高度
# 小球半径
# 重力加速度
# 弹力系数

# 导入pygame模块
import pygame

# 初始化pygame
pygame.init()

# 设置窗口大小和标题
window_width = 800  # 窗口宽度
window_height = 600  # 窗口高度
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Bouncing Ball")

# 设置颜色常量
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# 设置小球的初始位置和速度
ball_radius = 30  # 小球半径
ball_x = window_width // 2  # 小球初始横坐标为窗口中心
ball_y = ball_radius  # 小球初始纵坐标为半径高度
ball_vx = 0  # 小球初始横向速度为0
ball_vy = 1000  # 小球初始纵向速度为0

# 设置重力加速度和弹力系数
gravity = 9.8  # 重力加速度
bounce_factor = 0.8  # 弹力系数

# 设置时钟对象和帧率
clock = pygame.time.Clock()
FPS = 60

# 设置一个标志，表示小球是否被鼠标拖动
dragging = False

# 主循环
running = True
while running:
    # 处理事件
    for event in pygame.event.get():
        # 如果按鼠标右键让球到鼠标
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            ball_x, ball_y = event.pos
            ball_vx = 0
            ball_vy = 0
        # 如果点击关闭按钮，退出程序
        if event.type == pygame.QUIT:
            running = False

        # 如果按下鼠标左键，检查是否点击了小球，如果是，设置拖动标志为真，并记录鼠标位置和小球位置的偏移量
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_x, mouse_y = event.pos  # 获取鼠标位置
            distance = ((mouse_x - ball_x) ** 2 + (mouse_y - ball_y) ** 2) ** 0.5  # 计算鼠标位置和小球位置的距离
            if distance <= ball_radius:  # 如果距离小于等于小球半径，说明点击了小球
                dragging = True  # 设置拖动标志为真
                offset_x = mouse_x - ball_x  # 记录横向偏移量
                offset_y = mouse_y - ball_y  # 记录纵向偏移量

        # 如果松开鼠标左键，设置拖动标志为假，并根据鼠标移动的距离和时间计算小球的速度
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            if dragging:  # 如果之前在拖动小球
                dragging = False  # 设置拖动标志为假
                mouse_x, mouse_y = event.pos  # 获取鼠标位置
                # 计算鼠标移动的距离
                delta_x = mouse_x - (ball_x + offset_x)
                delta_y = mouse_y - (ball_y + offset_y)
                # 计算鼠标移动的时间
                delta_t = clock.get_time() / 1000
                # 根据距离和时间计算小球的速度
                ball_vx = delta_x / delta_t
                ball_vy = delta_y / delta_t

    # 更新状态
    if dragging:  # 如果正在拖动小球
        mouse_x, mouse_y = pygame.mouse.get_pos()  # 获取鼠标位置
        # 根据偏移量更新小球位置
        ball_x = mouse_x - offset_x
        ball_y = mouse_y - offset_y
    else:  # 如果没有拖动小球
        # 根据重力加速度更新小球纵向速度
        ball_vy += gravity * clock.get_time() / 1000
        # 根据速度更新小球位置
        ball_x += ball_vx * clock.get_time() / 1000
        ball_y += ball_vy * clock.get_time() / 1000

    # 处理碰撞
    if ball_x < ball_radius:  # 如果小球碰到左边界
        ball_x = ball_radius  # 限制小球位置
        ball_vx = -ball_vx * bounce_factor  # 反转并衰减小球横向速度

    if ball_x > window_width - ball_radius:  # 如果小球碰到右边界
        ball_x = window_width - ball_radius  # 限制小球位置
        ball_vx = -ball_vx * bounce_factor  # 反转并衰减小球横向速度

    if ball_y < ball_radius:  # 如果小球碰到上边界
        ball_y = ball_radius  # 限制小球位置
        ball_vy = -ball_vy * bounce_factor  # 反转并衰减小球纵向速度

    if ball_y > window_height - ball_radius:  # 如果小球碰到下边界
        ball_y = window_height - ball_radius  # 限制小球位置
        ball_vy = -ball_vy * bounce_factor  # 反转并衰减小球纵向速度

    # 绘制画面
    window.fill(BLACK)  # 填充背景色为黑色
    pygame.draw.circle(window, RED, (int(ball_x), int(ball_y)), int(ball_radius))  # 绘制红色的小球
    pygame.display.flip()  # 更新屏幕

    # 控制帧率
    clock.tick(FPS)

# 退出pygame
pygame.quit()