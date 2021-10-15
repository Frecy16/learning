def can_play(clock):
    print('can_play 函数被调用了')

    def handle_action(fn):
        print('handle_action 函数被调用了')

        def do_action(name, game):
            if clock < 22:
                fn(name, game)
            else:
                print('太晚了，要睡觉了，不能再玩游戏了')

        return do_action

    return handle_action


@can_play(21)
def play_game(name, game):
    print(name + '正在玩' + '《' + game + '》')


play_game('张三', '王者荣耀')
