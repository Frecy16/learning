# 开放封闭原则：已经写好的代码最好不要改动了

def can_play(fn):
    def inner(name, game, *args, **kwargs):
        # print(args)
        clock = kwargs.get('clock', 23)
        # if args[0] >= 22:
        #     print('太晚了，不能再玩了')
        if clock >= 22:
            print('太晚了，不能再玩了')
        else:
            fn(name, game)

    return inner


@can_play
def play_game(name, game):
    print('{} 正在玩儿 {}'.format(name, game))


x = play_game('李逍遥', '王者荣耀')
# print(x)
